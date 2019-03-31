import time
import random
from selenium import webdriver
import chromedriver_binary
options = webdriver.ChromeOptions()

#headlessの場合
#options.add_argument('--headless --disable-infobars')

#ユーザ(kumag)のプロファイルでchrome起動(不正アクセス防止対策)
options.add_argument("--user-data-dir=C:\\Users\\kumag\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()

###楽天検索を30回行う###

#検索語を用意
#search_word_list = ["よろしく","お願い","いたします","お礼","メール","打ち方","参考","サザエ","ツブ貝","アワビ"]
search_word_list = ["柿の種", "英語", "通訳", "数学", "算数", "テスト", "小学生", "体操服", "ランドセル", "ニート", "サザエさん","マッチョ","炭焼き","イカスミ","たこ焼き","大阪","観光地","ミミズ","虫歯","痛み止め","睡眠薬","マクラ"]

#タイムスリープ用乱数(1～5)
#randomモジュールの関数randrange(start, stop, step)は、range(start, stop, step)の要素からランダムに選ばれた要素（整数int型）を返す。


#対象サイトに接続
driver.get('https://websearch.rakuten.co.jp/')

#1秒待機
time.sleep(random.randrange(1, 6))

#検索語の数だけ検索を実施する（30回を超えたらループを抜ける）
for search_word in search_word_list:

    #検索フォームの要素(qt)をsearch_boxに取得
    search_box = driver.find_element_by_name("qt")
    time.sleep(random.randrange(1, 6))

    #検索語を入力する
    search_box.clear()
    time.sleep(random.randrange(1, 6))

    search_box.send_keys(search_word)
    time.sleep(random.randrange(1, 6))

    #検索を実行（検索ボタンをクリック、なぜかclick()ではできなかった）
    search_box.submit()
    time.sleep(random.randrange(1, 6))

#検索が終わり次第ウィンドウを閉じる
time.sleep(random.randrange(5,15))
driver.close()

#強制終了扱い？
#driver.close()