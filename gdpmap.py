import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline

frame = pd.read_csv(r'C:\Users\mzz\Desktop\2.csv', encoding='GBK')
tl = Timeline()
map=Map()
for i in range(2011, 2021):
    map0 = (
        Map()
            .add("省份", frame[['地区', str(i) + '年']].values.tolist(), "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-{}年GDP（亿元）".format(i)),
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
tl.render(r'C:\Users\mzz\Desktop\2010~2019年全国各地区GDP.html')
