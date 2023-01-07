from pyecharts.datasets import register_url
from pyecharts.charts import Map, Bar,Map3D
from pyecharts import options as opts
import os

register_url("https://echarts-maps.github.io/echarts-countries-js/")
prov = ['British Columbia','Alberta','Saskatchewan','Manitoba','Ontario','Quebec','New Brunswick','Prince Edward Island','Nova Scotia','Newfoundland and Labrador','Nunavut','Northwest Territories','Yukon']
datas = [100,200,300,400,500,600,700,800,900,110,120,130,140]
c = Map(init_opts=opts.InitOpts(width='1700px',height='1500px',page_title='Canada map'))

for i in range(13):
    c.add(prov[i],[[prov[i],datas[i]]],"加拿大")
c.set_global_opts(title_opts=opts.TitleOpts(title="Canada"))
c.render()

#c = (
 #   Map(init_opts=opts.InitOpts(width='1700px',height='1500px',page_title='Canada map'))

  #  .add("商家A", [["Nova Scotia", 100]], "加拿大")
   # .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    #.render()
#)
os.system("render.html")