import pandas as pd
import numpy as np
import os
from pyecharts.charts import Map, Bar,Timeline
from pyecharts import options as opts
df = pd.read_excel('AllGender.xlsx')
time1 = df['Year']
prov1= df['Geography']
numb1 = df['None']
time = []
prov = []
numb = []
for i in time1:
    d = str(i)
    time.append(d)
for i in prov1:
    prov.append(i)
for i in numb1:
    numb.append(i)
c = {'time':time,
     'pro':prov,
    'numb':numb
}
df1 = pd.DataFrame(c)

#print(df1)
timeline = Timeline(init_opts=opts.InitOpts(width='720px',height='350px'))
maps = Map(init_opts=opts.InitOpts(theme='light'))
for time in df1['time'].unique():
    # 选择对应时间的省份
    data = df1[df1['time'] == time]



    # 添加值
    maps.add(time,
             [list(z) for z in zip(data['pro'], data['numb'])],
             '加拿大')

    maps.set_global_opts(

        # 图表标题
        title_opts=opts.TitleOpts(
            # 标题
            title="Canada Edu",
            subtitle='No certificate, diploma or degree rate in total population',
            # 标题位置
            pos_left="left",
            # 标题字体大小设置为 20
            title_textstyle_opts=opts.TextStyleOpts(font_size=20)
        ),

        # 视觉映射值设置
        visualmap_opts=opts.VisualMapOpts(
            # 最大值
            max_=58,
            # 最小值
            min_=13,
            # 视觉映射显示
            is_show=True,
            # 是否为分段形
            #is_piecewise=True,
            # 组件映射维度
            dimension=0,
        ),

        # 图例设置
        legend_opts=opts.LegendOpts(
            # 显示图例，就是各个时间的切换按钮
            is_show=True,
            # 图例设置为单选模式
            selected_mode='single',
            # 图例的位置
            pos_top='5%', pos_right='5%',
            # 图例的布局朝向，垂直
            orient='vertical',
            # 图例形状
            legend_icon='circle'
        ),

        # 工具箱设置
        toolbox_opts=opts.ToolboxOpts(
            # 是否显示工具栏组件
            is_show=True,
            # 布局朝向
            orient='vertical',
            # 离上边距的距离
            pos_top='40%',
            pos_left='87%',

            # 配置各个工具箱
            feature=opts.ToolBoxFeatureOpts(

                # 保存工具
                opts.ToolBoxFeatureSaveAsImageOpts(
                    # 是否显示
                    is_show=True,
                    # 提示语
                    title="保存为图片",
                ),

                # 还原工具
                opts.ToolBoxFeatureRestoreOpts(
                    # 是否显示该工具
                    is_show=True,
                    # 提示语
                    title="还原",
                ),

                # 数据视图工具
                opts.ToolBoxFeatureDataViewOpts(
                    # 是否显示该工具
                    is_show=True,
                    # 提示语
                    title="数据视图",
                    # 是否不可编辑
                    is_read_only=False,
                ),

                # 缩放工具配置项，直角坐标系适用
                opts.ToolBoxFeatureDataZoomOpts(
                    # 是否显示该工具。
                    is_show=False,
                    # 提示语
                    zoom_title="区域缩放",
                    # 提示语
                    back_title="区域缩放还原",
                ),

                # 图表类型切换，适用于直角坐标系
                opts.ToolBoxFeatureMagicTypeOpts(
                    # 是否显示该工具
                    is_show=False,
                    # 启用的动态类型
                    type_=['stack', 'line', 'bar', 'tiled'],
                ),

                # 工具箱选框组件配置项
                opts.ToolBoxFeatureBrushOpts(
                    # 选择显示哪些选框
                    type_=[]
                ),
            )
        ),
    )

maps.render()
os.system("render.html")
