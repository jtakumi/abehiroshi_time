import os
import webbrowser
import time
import datetime
import csv
from csv import writer

url=[
    'http://abehiroshi.la.coocan.jp/',
    'https://www.google.com/',
    'https://www.yahoo.co.jp/',
    'https://www.youtube.com/',
    'https://www.amazon.co.jp/'
    ]
name=[
    '阿部寛',
    'Google',
    'Yahoo Japan',
    'Youtube',
    'Amazon'
]

today=datetime.date.today()
d1=today.strftime('%y-%m-%d')

def mkdir():
    mk='mkdir '+ d1
    os.system(mk)    

def work():
    now=datetime.datetime.now()
    now_t=now.strftime('%H-%M-%S')
    fn=d1 +  '\opening_time_' + now_t + 'data.csv'
    with open(fn,'w',encoding='utf-8-sig') as fc:
        for i in range(len(url)):
            s=time.perf_counter()
            webbrowser.open(url[i])
            f=time.perf_counter()
            print(name[i],file=fc)
            print(f-s,"s",file=fc)

def main():
    mkdir()
    work()

if __name__ == '__main__':
    main()