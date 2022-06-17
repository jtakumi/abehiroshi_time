import os
import webbrowser
import time
import datetime
import csv
from csv import writer
import urllib.request
from operator import itemgetter

from requests import request

url=[
    'http://abehiroshi.la.coocan.jp/',
    'https://www.google.com/',
    'https://www.yahoo.co.jp/',
    'https://www.youtube.com/',
    'https://www.amazon.co.jp/',
    'https://www.j-storm.co.jp/s/js/artist/J0004?ima=0000',
    'https://twitter.com/home',
    'https://www.apple.com/',
    'https://www.hololive.tv/',
    'https://www.nijisanji.jp/',
    'https://www.tesla.com/ja_jp',
    'https://toyota.jp/index.html',
    'https://www.nicovideo.jp/',
    'https://www.nintendo.co.jp/',
    'https://www.cygames.co.jp/',
    'https://umamusume.jp/',
    'https://priconne-redive.jp/',
    'https://www.aeon.info/',
    'https://www.pixiv.net/',
    'https://www.starbucks.co.jp/',
    'https://github.com/',
    'https://spitz-web.com/',
    'https://www.mrchildren.jp/',
    'https://www.instagram.com/',
    'https://yorushika.com/',
    'https://www.walmart.com/',
    'https://www.microsoft.com/ja-jp/',
    'https://reissuerecords.net/',
    'https://zutomayo.net/',
    'https://www.kantei.go.jp/',
    'https://www.jbd.co.jp/',
    'https://www.usa.gov/',
    'https://pmarusama.com/',
    'https://www.u-tokyo.ac.jp/ja/index.html',
    'https://www.ua.emb-japan.go.jp/itprtop_ja/index.html',
    'https://rivian.com/',
    'https://www.bing.com/',
    'https://www.mod.go.jp/msdf/kure/info/gallery/20201001-2_101mdkaitai.html',
    'https://colopl.co.jp/alicegearaegis/lp/countdown/homepage/',
    'https://speedsample.blog.fc2.com/',
    'http://natori-yuko.main.jp/',
    'https://global.yamaha-motor.com/jp/showroom/event/tokyo-motorshow-2019-bs/',
    "https://jp.investing.com/"
    ]
name=[
    '阿部寛',
    'Google',
    'Yahoo Japan',
    'Youtube',
    'Amazon',
    'JSTORM 嵐',
    'twitter',
    'Apple',
    'ホロライブプロダクション',
    'にじさんじ公式サイト',
    'テスラ日本語版サイト',
    'トヨタ自動車',
    'ニコニコ動画',
    '任天堂',
    'Cygames',
    'ウマ娘',
    'プリンセスコネクト Re:Dive',
    'AEON',
    'Pixiv',
    'Starbucks japan',
    'Github',
    'スピッツ',
    'Mr.Children',
    'Instagram',
    'ヨルシカ',
    'Walmart',
    'Microsoft 日本語サイト',
    '米津玄師',
    'ずっと真夜中でいいのに。',
    '首相官邸ホームページ',
    '日本ビジネス開発',
    'アメリカ政府',
    'P丸様。HP',
    '東京大学',
    'ウクライナ大使館',
    'RIVIAN',
    'Bing',
    '海上自衛隊第101掃海隊',
    'はさみメンテナンス株式会社(架空)',
    '爆速テンプレート(FC2)',
    '名取裕子',
    'ヤマハ発動機特設サイト',
    "Investing.com jp ver"
]

ret=[]

today=datetime.date.today()
d1=today.strftime('%y-%m-%d')

def mkdir():
    mk='mkdir '+ d1
    os.system(mk) 
    smk='mkdir ' +  d1 + '.\sort'
    os.system(smk)


def work():
    #実行した時間をファイル名とする
    now=datetime.datetime.now()
    now_t=now.strftime('%H-%M-%S')
    fn=d1 +  '\loading_time_' + now_t + 'data.csv'
    #403対策
    headers = { "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0" }
    #ただweb上のファイルを読み込むだけ
    with open(fn,'w',encoding='utf-8-sig') as fc:
        for i in range(len(url)):
            request=urllib.request.Request(url[i],headers=headers)
            try:
                com=urllib.request.urlopen(request)
            except Exception as e:
                print(url[i])
                print(e)
            else:
                s=time.perf_counter()
                com.read()
                f=time.perf_counter()
                com.close()
                ret.append(f-s)
                #サイト名と処理時間を書き出し
                print(name[i],f-s,"s",file=fc)
    return now_t

def sort(now_t):
    #昇順で並べ替え
    global name
    global ret
    sdata=list(zip(name,ret))
    sdata.sort(key=itemgetter(1))
    fn=d1 +  '\sort\loading_time_' + now_t + 'sort.csv'
    name,ret=zip(*sdata)
    with open(fn,'w',encoding='utf-8-sig') as fc:
        for j in range(len(name)):
            print(name[j],ret[j],'s',file=fc)

def git():
    add='git add .'
    os.system(add) 
    gcm='git commit -m ' + d1
    os.system(gcm)  

def runtime_file(now_t,runtime,func):
    rfn= d1 + '\_runtime' + d1 + now_t + 'txt'
    with open(rfn,'w',encoding='utf-8-sig') as rf:
        for r in range(1,len(runtime)):
            #前の時間と比べるために添え字を１からスタートしている
            print(func[r-1],file=rf)
            print(runtime[r]-runtime[r-1],'s',file=rf)
        print('total',file=rf)
        print(runtime[-1]-runtime[0],file=rf)


def main():
    #処理実行時間の検証
    runtime=[]
    func=['mkdir','work','sort']
    runtime.append(time.perf_counter())
    mkdir()
    runtime.append(time.perf_counter())

    now_t=work()
    runtime.append(time.perf_counter())

    sort(now_t)
    runtime.append(time.perf_counter())

    runtime_file(now_t,runtime,func)
    git()

    #すべてが完了したら阿部寛のホームページを開く
    webbrowser.open(url[0])

if __name__ == '__main__':
    main()