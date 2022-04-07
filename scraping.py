
"""
ヤフーフィナンシャルから為替情報を取得
CSVにして記録
@author: keish
"""


from bs4 import BeautifulSoup
import urllib.request as req
import datetime
import time
import threading

def task():

    #scraping from yahoo 
    url_0="https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
    res = req.urlopen(url_0)
    soup = BeautifulSoup(res, 'html.parser');
    d0 = soup.select_one(".stoksPrice").string #(1)
    print(d0)
    url_1="https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX"
    res = req.urlopen(url_1) 
    soup = BeautifulSoup(res, 'html.parser');
    vals = soup.select_one("#USDJPY_detail_bid").findAll(text=True)
    d1=''.join(vals)
    print(d1)
    # 日時の取得
    now = datetime.datetime.now()
    print(now)
    file_name =r'C:\Users\keish\Desktop\proglaming/sc.csv'
 
    with open(file_name, mode='a', encoding='utf-8') as f:
        f.write('{},{},\n'.format(now.strftime("%Y,%m,%d,%H,%M"),d1))
        print(d1)
        
    
    print(d1,now)
    time.sleep(2)

def schedule(interval, f, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)
    


schedule(5,task())

