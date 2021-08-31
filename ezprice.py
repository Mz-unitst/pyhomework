import requests
from bs4 import BeautifulSoup
import pandas as pd
import codecs
import csv
import re
from fake_useragent import UserAgent
import json


url = 'https://www.gotohui.com/top/'
#header = {"User-Agent":str(ua.chrome())}
fpath = "C:\\Users\\mzz\\Desktop\\ezprice.csv"
tmp_path = "C:\\Users\\mzz\\Desktop\\ez.html"
fp = "C:\\Users\\mzz\\Desktop\\shuju1.csv"
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84",
    "X-Amzn-Trace-Id": "Root=1-612e1135-05c820655a52316846399ba7"}


class spi():
    def __init__(self):
        self.url = url
        #self.header = header
        self.html = ''
        # self.frame=pd.read_csv()

    def getHTMLText(self, url):
        try:
            print("start")
            r = requests.get(url, timeout=10, headers=h)
            self.html = r.content.decode('utf-8')
            print("len:", len(self.html))
            r.raise_for_status()
            self.parseHTMLText(html=self.html)
        except BaseException:
            return "fail to get HTML!"

    def parseHTMLText(self, html):
        # with open()
        soup = BeautifulSoup(html, "html.parser")
        cities = soup.find_all('tr')
        print("len of cities", len(cities))
        cnt = 0
        for i in cities:
            cnt = cnt + 1
            if(cnt < 3):
                continue
            with open(fp, "a") as f:
                print(cnt)
                # i.decode('gbk')
                fieldname={'城市','GDP'}
                writer = csv.DictWriter(f,fieldnames=fieldname)
                writer.writeheader()
                city = i.find('a').string
                # print(city)
                prices = i.find_all('td')
                tmp_price = prices[2].string

                price = tmp_price.replace(',', '')
                print("city:", city, "\tprice:", price)
                dic={city:price}
                print(dic)
                # tmppp = str(city + ' ')
                # tmp=str(price+tmppp)
                # print(type(pr))
                # print("tmp_gbk:", tmp)
                # tmp_unicode = tmp.decode('utf-8')
                # tmp_gbk = tmp_unicode.encode('gbk')
                writer.writerow(dic)
            #f.close()
        print("success to parse HTML")
        # print(tables[0].prettify)

    def saveHTMl(self, path, html):
        try:
            with open('C:\\Users\\mzz\\Desktop\\ez.html', "w", encoding='utf-8') as ff:
                ff.write(html)
            print("success to save")
        except BaseException:
            return "fail to save HTML"

    def run(self):
        self.getHTMLText(url=self.url)
        # self.parseHTMLText(html=self.html)


if __name__ == "__main__":
    s = spi()
    # print("run")
    s.run()
    # s.getHTMLText(url=url)
   # print("?")
    a = r'''
    r=requests.get(url=url,headers=h,timeout=10)
    r.encoding=r.apparent_encoding
    print(type(r.text))
    r.raise_for_status()
    html=r.text
    with open(r'C:\Users\mzz\Desktop\2.txt',"w",encoding='utf-8') as f:
        f.write(str(r.text))
    print(len(html))

    '''
