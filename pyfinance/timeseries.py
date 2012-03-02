from copy import deepcopy
import numpy as np
import sqlite3
import datetime


class TickerCodeError(Exception):
    pass


def _convertArrayType(data, mode="numpy"):
    """
    convert list <=> numpy ndarray
    mode = "numpy" or "list"
    """
    if mode == "numpy":
        return np.array(data)
    else:
        return np.array(data).tolist()


class TimeSeries():

    def __init__(self, dates, data):
        if len(dates) != len(data):
            raise ValueError, "the lengths of dates and data must be equal"
        self.dates = deepcopy(dates)
        self.data = deepcopy(data)

    def __len__(self):
        return len(self.dates)

    def __getitem__(self, i):
        return [self.dates[i], self.data[i]]

    def __setitem__(self, i, args):
        self.dates[i] = args[0]
        self.data[i] = args[1]

    def __str__(self):
        s = []
        for i in xrange(len(self)):
            temp_s = "%s %s" % (self.dates[i].__str__(),
                                 self.data[i].__str__())
            s.append(temp_s)
        return s.__str__()

    def __iter__(self):
        for i in xrange(len(self)):
            yield self[i]

    def sort(self, reverse=False):
        temp = sorted(zip(self.dates, self.data), reverse=reverse)
        self.dates = [t[0] for t in temp]
        self.data = [t[1] for t in temp]


class TickTimeSeries(TimeSeries):
    def __init__(self, dates, data, tick_id, mode="numpy"):
        self.tick_id = tick_id
        self._mode = mode
        TimeSeries.__init__(self, dates, _convertArrayType(data, mode))

    def convertArrayType(self, mode="numpy"):
        self._mode = mode
        self.data = _convertArrayType(self.data, mode)

    def sort(self, reverse=False):
        TimeSeries.sort(self, reverse)
        self.convertArrayType(mode=self._mode)

    def dumpToSQL(self, db_name):
        db = sqlite3.connect(db_name)

        # attempt to create a table
        try :
            db.execute("CREATE TABLE ticklist(tick_id)")
            db.execute("CREATE TABLE tickdata(tick_id, date, open_v, high_v,\
                    low_v, close_v, volume)")
            db.execute("CREATE UNIQUE INDEX tick_idx on tickdata(tick_id,date)")
            db.execute("CREATE UNIQUE INDEX data_idx on tickdata(tick_id,date)")
        except sqlite3.OperationalError:
            pass

        # insert tick_id to ticklist
        sql_cmd = "insert or replace into ticklist values (?)"
        db.execute(sql_cmd, (self.tick_id,))

        sql_cmd = """insert or replace into tickdata(tick_id, date, open_v,
        high_v, low_v, close_v, volume) values (?, ?, ?, ?, ?, ?, ?)"""
        #print sql_cmd
        for s in self:
            # insert data
            db.execute(sql_cmd, (self.tick_id, str(s[0]), s[1][0], s[1][1],
                    s[1][2], s[1][3], s[1][4]))

        # finalize
        db.commit()
        db.close()


def getTickIDsFromSQL(db_name):
    db = sqlite3.connect(db_name)
    ids = db.execute("SELECT tick_id FROM ticklist").fetchall()
    ids = [i[0] for i in ids]
    db.close()
    return ids


def getTickDataFromSQL(db_name, tick_id, begin_date=None, end_date=None):
    # get data from sqlite database
    db = sqlite3.connect(db_name)

    # first check if the requested tick_id exists
    sql_cmd = "select tick_id from ticklist where tick_id=?"
    iid = db.execute(sql_cmd, (tick_id,)).fetchone()
    if iid == None:
        db.close()
        raise TickerCodeError, "Ticker Code %s not found" % tick_id

    # get tick data
    sql_cmd = "select * from tickdata where tick_id=?"
    query_values = [tick_id]

    if begin_date:
            sql_cmd += " and date >= ?"
            query_values.append(str(begin_date))

    if end_date:
            sql_cmd += " and date <= ?"
            query_values.append(str(end_date))

    # execute sql command
    res = db.execute(sql_cmd, query_values).fetchall()
    db.close()

    # create a TickTimeSeries
    dates = []
    data = []
    for r in res:
        dates.append(_str2date(r[1]))
        data.append(r[2:])

    return TickTimeSeries(dates, data, tick_id)


def _str2date(s):
    """ convert strings to date object
    2010-10-29 to datetime.date(2010, 10, 29)"""
    temp = [int(ss) for ss in s.split("-")]
    date = datetime.date(temp[0], temp[1], temp[2])
    return date
