import os
import webbrowser
import time
import datetime
import csv
from csv import writer
import urllib.request
from operator import itemgetter

url=[
    'http://abehiroshi.la.coocan.jp/',
    'https://www.google.com/',
    'https://www.yahoo.co.jp/',
    'https://www.youtube.com/',
    'https://www.amazon.co.jp/',
    'https://www.j-storm.co.jp/s/js/artist/J0004?ima=0000'
    ]
name=[
    '阿部寛',
    'Google',
    'Yahoo Japan',
    'Youtube',
    'Amazon',
    'JSTORM 嵐'
]

ret=[]

today=datetime.date.today()
d1=today.strftime('%y-%m-%d')

def mkdir():
    mk='mkdir '+ d1
    os.system(mk) 
    smk='mkdir ' +  d1 + '.\sort'
    os.system(smk)


def git():
    add='git add ' + d1 + '\.'
    os.system(add)   

def work():
    now=datetime.datetime.now()
    now_t=now.strftime('%H-%M-%S')
    fn=d1 +  '\loading_time_' + now_t + 'data.csv'
    #ただweb上のファイルを読み込むだけ
    with open(fn,'w',encoding='utf-8-sig') as fc:
        for i in range(len(url)):
            com=urllib.request.urlopen(url[i])
            s=time.perf_counter()
            com.read()
            f=time.perf_counter()
            com.close()
            ret.append(f-s)
            print(name[i],f-s,"s",file=fc)
    return now_t

def sort(now_t):
    global name
    global ret
    sdata=list(zip(name,ret))
    sdata.sort(key=itemgetter(1))
    fn=d1 +  '\sort\loading_time_' + now_t + 'sort.csv'
    name,ret=zip(*sdata)
    with open(fn,'w',encoding='utf-8-sig') as fc:
        for j in range(len(name)):
            print(name[j],ret[j],'s',file=fc)
def main():
    mkdir()
    now_t=work()
    sort(now_t)
    git()
    webbrowser.open(url[0])

if __name__ == '__main__':
    main()