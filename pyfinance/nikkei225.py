﻿# -*- coding: utf-8 -*-

import cStringIO
import codecs

bom_utf8 = unicode(codecs.BOM_UTF8, "utf-8")

nikkei225_string = """
#精密機器関連
4543 テルモ
7731 ニコン
7733 オリンパス
7762 シチズンHD
#陸運業関連
9001 東武鉄道
9005 東京急行電鉄
9007 小田急電鉄
9008 京王電鉄
9009 京成電鉄
9020 東日本旅客鉄道
9021 西日本旅客鉄道
9022 東海旅客鉄道
9062 日本通運
9064 ヤマトHD
#輸送用機器関連
6902 デンソー
7003 三井造船
7012 川崎重工業
7201 日産自動車
7202 いすゞ自動車
7203 トヨタ自動車
7205 日野自動車
7211 三菱自動車
7261 マツダ
7267 ホンダ
7269 スズキ
7270 富士重工業
#保険業関連
8630 NKSJホールディングス
8725 MS&ADインシュアランス
8729 ソニーフィナンシャルHD
8750 第一生命保険
8766 東京海上HD
8795 T&DHD
#不動産業関連
8801 三井不動産
8802 三菱地所
8803 平和不動産
8804 東京建物
8815 東急不動産
8830 住友不動産
#非鉄金属関連
5701 日本軽金属
5706 三井金属
5707 東邦亜鉛
5711 三菱マテリアル
5713 住友金属鉱山
5714 DOWAHD
5715 古河機械金属
5801 古河電気工業
5802 住友電気工業
5803 フジクラ
#電気機器関連
4902 コニカミノルタHD
6479 ミネベア
6501 日立製作所
6502 東芝
6503 三菱電機
6504 富士電機HD
6506 安川電機
6508 明電舎
6674 ジーエス・ユアサ
6701 NEC
6702 富士通
6703 OKI
6752 パナソニック
6753 シャープ
6758 ソニー
6762 TDK
6767 ミツミ電機
6770 アルプス電気
6773 パイオニア
6841 横河電機
6857 アドバンテスト
6952 カシオ計算機
6954 ファナック
6971 京セラ
6976 太陽誘電
7735 大日本スクリーン製造
7751 キヤノン
7752 リコー
8035 東京エレクトロン
#電気ガス業関連
9501 東京電力
9502 中部電力
9503 関西電力
9531 東京ガス
9532 大阪ガス
#鉄鋼関連
5401 新日本製鐵
5405 住友金属工業
5406 神戸製鋼所
5407 日新製鋼
5411 ジェイエフイーHD
5541 大平洋金属
#倉庫運輸関連
9301 三菱倉庫
#繊維製品関連
3101 東洋紡
3103 ユニチカ
3105 日清紡HD
3401 帝人
3402 東レ
#石油石炭関連
5002 昭和シェル石油
5020 JXホールディングス
#水産農林業関連
1332 日本水産
1334 マルハニチロHD
#食料品関連
2002 日清製粉グループ本社
2269 明治HD
2282 日本ハム
2501 サッポロHD
2502 アサヒビール
2503 キリンHD
2531 宝HD
2801 キッコーマン
2802 味の素
2871 ニチレイ
2914 JT
#情報通信業関連
4689 ヤフー
4704 トレンドマイクロ
9412 スカパーJSATHD
9432 日本電信電話
9433 KDDI
9437 NTTドコモ
9602 東宝
9613 NTTデータ
9766 コナミ
9984 ソフトバンク
#証券商品先物関連
8601 大和証券グループ本社
8604 野村HD
8628 松井証券
#小売業関連
3086 J.フロントリテイリング
3099 三越伊勢丹HD
3382 セブン&アイ・HD
8233 高島屋
8252 丸井グループ
8267 イオン
8270 ユニー
9983 ファーストリテイリング
#鉱業関連
1605 国際石油開発帝石
#建設業関連
1721 コムシスHD
1801 大成建設
1802 大林組
1803 清水建設
1812 鹿島
1925 大和ハウス工業
1926 ライト工業
1928 積水ハウス
1963 日揮
6366 千代田化工建設
#空運業関連
9202 全日本空輸
#銀行業関連
8303 新生銀行
8304 あおぞら銀行
8306 三菱UFJ
8308 りそなHD
8309 中央三井トラスト・HD
8316 三井住友
8331 千葉銀行
8332 横浜銀行
8354 ふくおか
8355 静岡銀行
8411 みずほ
#金属製品関連
3436 SUMCO
5901 東洋製罐
#機械関連
5631 日本製鋼所
6103 オークマ
6113 アマダ
6301 コマツ
6302 住友重機械工業
6305 日立建機
6326 クボタ
6361 荏原
6367 ダイキン工業
6471 日本精工
6472 NTN
6473 ジェイテクト
7004 日立造船
7011 三菱重工業
7013 IHI
#海運業関連
9101 日本郵船
9104 商船三井
9107 川崎汽船
#化学関連
3405 クラレ
3407 旭化成
4004 昭和電工
4005 住友化学
4041 日本曹達
4042 東ソー
4061 電気化学工業
4063 信越化学工業
4183 三井化学
4188 三菱ケミカルHD
4208 宇部興産
4272 日本化薬
4452 花王
4901 富士フイルムHD
4911 資生堂
#卸売業関連
2768 双日
8001 伊藤忠商事
8002 丸紅
8015 豊田通商
8031 三井物産
8053 住友商事
8058 三菱商事
#医薬品関連
4151 協和発酵キリン
4502 武田薬品工業
4503 アステラス製薬
4506 大日本住友製薬
4507 塩野義製薬
4519 中外製薬
4523 エーザイ
4568 第一三共
#パルプ紙関連
3861 王子製紙
3864 三菱製紙
3865 北越紀州製紙
3893 日本製紙グループ本社
#その他製品関連
7911 凸版印刷
7912 大日本印刷
7951 ヤマハ
#その他金融業関連
8253 クレディセゾン
#サービス業関連
4324 電通
9681 東京ドーム
9735 セコム
#ゴム製品関連
5101 横浜ゴム
5108 ブリヂストン
#ガラス土石関連
3110 日東紡
5201 旭硝子
5202 日本板硝子
5214 日本電気硝子
5232 住友大阪セメント
5233 太平洋セメント
5301 東海カーボン
5332 TOTO
5333 日本ガイシ
"""


def _parseTickList(ticklist_str):
    Industry_Type = []
    Tick_Codes = {}
    i = -1

    for line in ticklist_str:
        line = unicode(line.strip(), "utf-8")
#        line = line.stript()

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
