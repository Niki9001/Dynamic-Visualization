from pyecharts.charts import Bar,Line,Grid
from pyecharts import options as opts
import os
import pandas as pd
from pyecharts.charts import Geo
cate = ['Apple','Huawei','Xiaomi','Oppo','Samsung']
data1 = [123,153,89,107,98]
data2 = [56,77,93,68,45]



attr = cate
value = data1

geo =(Geo().add_schema(maptype="加拿大"))

#geo.add(attr, value,maptype='china', visual_text_color="#FF0000", geo_normal_color="#6E6E6E", geo_emphasis_color='#F5D0A9',
 #       symbol_size=8, effect_scale=5, is_visualmap=True)

geo.render()
os.system("render.html")
