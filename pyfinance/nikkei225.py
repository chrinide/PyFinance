﻿# -*- coding: utf-8 -*-

import cStringIO
import codecs

bom_utf8 = unicode(codecs.BOM_UTF8, "utf-8")

nikkei225_string = """
#水産関連の日経225採用銘柄
1332 日本水産株式会社
#鉱業関連の日経225採用銘柄
1601 国際石油開発帝石ホールディングス株式会社
#建設関連の日経225採用銘柄
1721 コムシスホールディングス株式会社
1801 大成建設株式会社
1802 株式会社大林組
1803 清水建設株式会社
1812 鹿島建設株式会社
1861 株式会社熊谷組
1925 大和ハウス工業株式会社
1928 積水ハウス株式会社
1963 日揮株式会社
#食品関連の日経225採用銘柄
2001 日本製粉株式会社
2002 株式会社日清製粉グループ本社
2202 明治製菓株式会社
2261 明治乳業株式会社
2282 日本ハム株式会社
2501 サッポロホールディングス株式会社
2502 アサヒビール株式会社
2503 キリンホールディングス株式会社
2531 宝ホールディングス株式会社
2602 日清オイリオグループ株式会社
2768 双日株式会社 
2779 株式会社三越 
2801 キッコーマン株式会社 
2802 味の素株式会社 
2871 株式会社ニチレイ 
2914 日本たばこ産業株式会社（ＪＴ） 
#繊維関連の日経225採用銘柄
3101 東洋紡績株式会社 
3103 ユニチカ株式会社 
3105 日清紡績株式会社 
3110 日東紡績株式会社 
3382 株式会社セブン＆アイ 
3401 帝人株式会社 
3402 東レ株式会社 
3404 三菱レイヨン株式会社 
3405 株式会社クラレ 
3407 旭化成株式会社 
#紙パルプ関連の日経225採用銘柄
3861 王子製紙株式会社 
3864 三菱製紙株式会社 
3865 北越製紙株式会社 
3893 株式会社日本製紙 
#化学関連の日経225採用銘柄
4004 昭和電工株式会社 
4005 住友化学株式会社 
4021 日産化学工業株式会社 
4041 日本曹達株式会社 
4042 東ソー株式会社 
4045 東亞合成株式会社 
4061 電気化学工業株式会社 
4063 信越化学工業株式会社 
4151 協和発酵工業株式会社 
4183 三井化学株式会社 
4188 株式会社三菱ケミカルホールディングス 
4208 宇部興産株式会社 
4272 日本化薬株式会社 
4452 花王株式会社 
4901 富士フイルムホールディングス株式会社 
4902 コニカミノルタホールディングス株式会社 
4911 株式会社資生堂 
#医薬品関連の日経225採用銘柄
4502 武田薬品工業株式会社 
4503 アステラス製薬株式会社 
4506 大日本住友製薬株式会社 
4507 塩野義製薬株式会社 
4519 中外製薬株式会社 
4523 エーザイ株式会社 
4543 株式会社テルモ 
4568 第一三共株式会社 
#石油関連の日経225採用銘柄
5001 新日本石油株式会社 
5002 昭和シェル石油株式会社 
5016 新日鉱ホールディングス株式会社 
#ゴム関連の日経225採用銘柄
5101 横浜ゴム株式会社 
5108 株式会社ブリヂストン 
#窯業関連の日経225採用銘柄
5201 旭硝子株式会社 
5202 日本板硝子株式会社 
5232 住友大阪セメント株式会社 
5233 太平洋セメント株式会社 
5301 東海カーボン株式会社 
5332 ＴＯＴＯ株式会社 
5333 日本ガイシ株式会社 
#鉄鋼関連の日経225採用銘柄
5401 新日本製鐵株式会社 
5405 住友金属工業株式会社 
5406 株式会社神戸製鋼所 
5411 JFEホールディングス株式会社 
#非鉄、金属製品関連の日経225採用銘柄
5701 日本軽金属株式会社 
5706 三井金属鉱業株式会社 
5707 東邦亜鉛株式会社 
5711 三菱マテリアル株式会社 
5713 住友金属鉱山株式会社 
5714 DOWAホールディングス株式会社 
5715 古河機械金属株式会社 
5801 古河電気工業株式会社 
5802 住友電気工業株式会社 
5803 株式会社フジクラ 
5901 東洋製缶株式会社 
#機械関連の日経225採用銘柄
5631 株式会社日本製鋼所 
6103 オークマホールディングス株式会社 
6301 株式会社小松製作所
6302 住友重機械工業株式会社 
6326 株式会社クボタ 
6361 株式会社荏原製作所 
6366 千代田化工建設株式会社 
6367 ダイキン工業株式会社 
6471 日本精工株式会社 
6472 NTN株式会社 
7004 日立造船株式会社 
7011 三菱重工業株式会社 
6473 株式会社ジェイテクト 
#電力関連の日経225採用銘柄
9501 東京電力株式会社 
9502 中部電力株式会社 
9503 関西電力株式会社 
#ガス関連の日経225採用銘柄
9531 東京瓦斯（東京ガス）株式会社 
9532 大阪瓦斯（大阪ガス）株式会社 
#サービス関連の日経225採用銘柄
9605 東映株式会社 
4324 株式会社電通 
9681 株式会社東京ドーム 
9735 セコム株式会社 
9737 株式会社CSKホールディングス 
9766 コナミ株式会社 
4704 トレンドマイクロ株式会社 
#電気機器関連の日経225採用銘柄
6701 日本電気株式会社（ＮＥＣ） 
6702 富士通株式会社 
6703 沖電気工業株式会社 
6752 松下電器産業株式会社 
6753 シャープ株式会社 
6758 ソニー株式会社 
6762 ＴＤＫ株式会社 
6764 三洋電機株式会社 
6767 ミツミ電機株式会社 
6770 アルプス電気株式会社 
6773 パイオニア株式会社 
6796 クラリオン株式会社 
6841 横河電機株式会社 
6857 株式会社アドバンテスト 
6902 株式会社デンソー 
6952 カシオ計算機株式会社 
6501 株式会社日立製作所 
6502 株式会社東芝 
6503 三菱電機株式会社 
6504 富士電機ホールディングス株式会社 
6508 株式会社明電舎 
6674 株式会社ジーエス・ユアサ コーポレーション 
6954 ファナック株式会社 
6971 京セラ株式会社 
6976 太陽誘電株式会社 
6991 松下電工株式会社 
6479 ミネベア株式会社 
#造船関連の日経225採用銘柄
7003 三井造船株式会社 
7012 川崎重工業株式会社 
7013 株式会社IHI（石川島播磨重工業株式会社） 
#自動車関連の日経225採用銘柄
7201 日産自動車株式会社 
7202 いすゞ自動車株式会社 
7203 トヨタ自動車株式会社 
7205 日野自動車株式会社 
7211 三菱自動車株式会社 
7261 マツダ株式会社 
7267 本田技研工業株式会社 
7269 スズキ株式会社 
7270 富士重工業株式会社 
#輸送用機器関連の日経225採用銘柄
7231 トピー工業株式会社
#精密機器関連の日経225採用銘柄
7731 株式会社ニコン 
7733 オリンパス株式会社 
7751 キヤノン株式会社 
7752 株式会社リコー 
7762 シチズンホールディングス株式会社 
#その他製造関連の日経225採用銘柄
7911 凸版印刷株式会社 
7912 大日印刷株式会社 
7951 ヤマハ株式会社 
#商社関連の日経225採用銘柄
8001 伊藤忠商事株式会社 
8002 丸紅株式会社 
8003 株式会社トーメン 
8031 三井物産株式会社 
8035 東京エレクトロン株式会社 
8053 住友商事株式会社 
8058 三菱商事株式会社 
#小売業関連の日経225採用銘柄
8233 株式会社高島屋 
3099 株式会社三越伊勢丹ホールディングス 
8252 株式会社丸井グループ 
8253 株式会社クレディセゾン 
8267 イオン株式会社 
9983 株式会社ファーストリテイリング（ユニクロ） 
#銀行関連の日経225採用銘柄
8303 株式会社新生銀行 
8306 株式会社三菱UFJフィナンシャル・グループ 
8308 株式会社りそなホールディングス 
8309 中央三井トラスト・ホールディングス株式会社 
8316 株式会社三井住友フィナンシャルグループ 
8331 株式会社千葉銀行 
8332 株式会社横浜銀行 
8355 株式会社静岡銀行 
8403 住友信託銀行株式会社 
8404 みずほ信託銀行株式会社 
#その他金融関連の日経225銘柄
8411 株式会社みずほフィナンシャルグループ 
8583 三菱UFJニコス株式会社 
#証券関連の日経225採用銘柄
8601 株式会社大和証券グループ本社 
8603 株式会社日興コーディアルグループ 
8604 野村ホールディングス株式会社 
8606 新光証券株式会社 
#保険関連の日経225採用銘柄
8752 三井住友海上火災保険株式会社 
8755 株式会社損害保険ジャパン（損保ジャパン） 
8766 株式会社ミレアホールディングス 
8795 株式会社Ｔ＆Ｄホールディングス 
#不動産関連の日経225採用銘柄
8801 三井不動産株式会社 
8802 三菱地所株式会社 
8803 平和不動産株式会社 
8830 住友不動産株式会社 
#鉄道・バス関連の日経225採用銘柄
9001 東武鉄道株式会社 
9005 東京急行電鉄株式会社 
9007 小田急電鉄株式会社 
9008 京王電鉄株式会社 
9009 京成電鉄株式会社 
9020 東日本旅客鉄道株式会社（ＪＲ東日本） 
9021 西日本旅客鉄道株式会社（ＪＲ西日本） 
#陸運関連の日経225採用銘柄
9062 日本通運株式会社 
9064 ヤマトホールディングス株式会社 
#海運関連の日経225採用銘柄
9101 日本郵船株式会社 
9104 株式会社商船三井 
9107 川崎汽船株式会社 
#空運関連の日経225採用銘柄
9202 全日本空輸株式会社（ＡＮＡ） 
9205 日本航空株式会社（ＪＡＬ） 
#倉庫関連の日経225採用銘柄
9301 三菱倉庫株式会社
#情報・通信関連の日経225採用銘柄
9984 ソフトバンク株式会社 
9432 日本電信電話株式会社（ＮＴＴ） 
9433 ＫＤＤＩ株式会社 
9437 株式会社ＮＴＴドコモ 
9613 株式会社ＮＴＴデータ 
4689 ヤフー株式会社 
4795 スカパーJSAT株式会社 
"""


def _parseTickList(ticklist_fp):
    Industry_Type = []
    Tick_Codes = {}
    i = -1

    for line in ticklist_fp:
        line = unicode(line.strip(), "utf-8")

        if len(line) == 0:
            continue

        if line[0] in bom_utf8:
            line = line[1:]

        if line[0] == "#":
            Industry_Type.append((line[1:], []))
            i = i + 1
        elif line[0] in "0123456789":
            splt = line.split()
            tick_id = int(splt[0])
            company_name = splt[1]
            Tick_Codes[tick_id] = company_name
            Industry_Type[i][1].append(tick_id)

    return Industry_Type, Tick_Codes


def getNikkei225():
    nikkei225_fp = cStringIO.StringIO(nikkei225_string)
    return _parseTickList(nikkei225_fp)

tick_codes = getNikkei225()[1]

def getNameFromID(tick_ids):
    tick_names = [tick_codes[tick_id] for tick_id in tick_ids]
    return tick_names
