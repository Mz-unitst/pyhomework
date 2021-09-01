import requests
from bs4 import BeautifulSoup
import codecs
import csv
import re
from fake_useragent import UserAgent
import json
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
import pandas as pd


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
        dics={}
        lst=[]
        fiel={'城市','GDP'}
        #dics.update(fiel)
        #print("2")
        lst.append(fiel)
        #print(dics)
        for i in cities:
            cnt = cnt + 1
            if(cnt < 3):
                continue
                # writer = csv.DictWriter(f,fieldnames=fieldname)
                # writer.writeheader()
            city = i.find('a').string
            #print(city)
            prices = i.find_all('td')
            tmp_price = prices[2].string

            price = tmp_price.replace(',', '')
            #print("city:", city, "\tprice:", price)
            t={city:price}
            #print(t)
            dics.update(t)
            ttt=[city,price]
            print(ttt)
            lst.append(ttt)
            # print(dic)
            # tmppp = str(city + ' ')
            # tmp=str(price+tmppp)
            # print(type(pr))
            # print("tmp_gbk:", tmp)
            # tmp_unicode = tmp.decode('utf-8')
            # tmp_gbk = tmp_unicode.encode('gbk')
            # writer.writerow(dic)
            #f.close()
        #print(dics)
        with open(fp, "w",newline='') as f:
            writer = csv.writer(f)
            print(lst)
            #for i in range(len(lst)):
              # print(lst[i])
            #   csv 可以list!!
            writer.writerows(lst)

       # print(dics)
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
    #print("?")
    frame = pd.read_csv(r'C:\Users\mzz\Desktop\gdp.csv', encoding='GBK')
    tl = Timeline()
    map = Map()
    for i in range(1998, 2018):
        map0 = (
            Map()
                .add("省份", frame[['地区', str(str(i) + '年')]].values.tolist(), "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="各省{}年GDP（亿元）".format(i)),
                visualmap_opts=opts.VisualMapOpts(
                    is_piecewise=True,
                    pieces=[
                        {"min": 0, "max": 10000, "label": "1~10000", "color": "cyan"},
                        {"min": 10001, "max": 20000, "label": "10001~20000", "color": "yellow"},
                        {"min": 20001, "max": 50000, "label": "20001~50000", "color": "orange"},
                        {"min": 50001, "max": 80000, "label": "50001~80000", "color": "coral"},
                        {"min": 80001, "max": 120000, "label": "80001~12000", "color": "red"},
                    ]), ))
        tl.add(map0, "{}年".format(i))
    tl.render(r'C:\Users\mzz\Desktop\1998~2017年全国各地区GDP.html')
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
