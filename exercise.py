import plotly_express as px  # import plotly.express as px
import plotly.graph_objects as go
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import hypertools as hyp
import pandas as pd

#bar chart

# # Create the data
# categories = ['1', '2', '3', '4', '5', '6', 'X']
# values = [0, 6, 22, 33, 24, 12, 3]
# 
# # Create the bar chart
# plt.bar(categories, values)
# 
# # Set the title and labels
# plt.title('Bar Chart of Categories')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# 
# # Show the plot
# #加标题！！！！！！
# plt.title('TSNE, clutering by KMeans')
# plt.show()

# another bar chart
#方式2：
# df3 = {'strate_mom':0.154795344855160, 'psych_mom':0.235914838267283, 'isace': 0.00462006957930888, 'isserver':0.0170685498888039, 'serve_depth':0.0327175260371862, 'serve_width':0.0539408804051049, 'return_depth':0.0289050427262831, 'speed_mph':0.0995767306286590, 'double_fault':0.00693010436896332, 'break_pt_won':0.00554408349517065 , 'unf_err':0.0176594210577689, 'winner':0.0177901414730189, 'rest_variable':0.0792326024227123, 'chushi_shitou_cha':0.245304664794576}
# df5 = pd.DataFrame({"variables": df3.keys(), "importance": df3.values()})
# print(df5.values)
# print(df5)
# row=[]
# column=[]
# for i in df5.values:
#     row.append(i[0])
#     column.append(i[1])
# fg4=px.bar(df5, x='variables', y='importance', color='importance')
# fg4.show()

# df5.plot(kind='barh',rot=0)
# plt.show()

#结果为：
#         key  value
# 0     Korea     23
# 1   England    118
# 2   chinese    109
# 3    German     66
# 4  American     88
# 5     Japan      5

#第三个分组的bar chart！！！很重要
# fig = px.bar(df4,   # 带绘图数据
#              x="sex",  # x轴
#              y="total_bill",   # y轴
#              color="smoker",  # 颜色设置
#              barmode="group",  # 柱状图4种模式之一
#              facet_row="time",  #  行
#              facet_col="day",  # 列
#              category_orders={
#                  "day": ["Thur", "Fri", "Sat", "Sun"],
#                  "time": ["Lunch", "Dinner"]   # 分类顺序设置
#                              }
#             )
# fig.show()


# # GDP数据
# gapminder=px.data.gapminder()
# print(gapminder.head())
# #餐厅数据
# tips = px.data.tips()
# tips.head()
# #鸢尾花
# iris=px.data.iris()
# print(type(iris))
# print(iris.head())

# # scattter
# categories = ['1', '2', '3', '4', '5', '6', 'X']
# values = [0, 6, 22, 33, 24, 12, 3]
# fg1=px.scatter(x=categories, y=values)
# fg1.show()
# fg2=px.scatter(iris, x='sepal_width', y='sepal_length', color='sepal_length', hover_data='petal_length')
# fg2.show()
# #
# # from sklearn import datasets
# # data = datasets.load_digits(n_class=5)
# # df = data.data
# # hue = data.target.astype('str')
# # hyp.plot(df, '.', hue=hue, ndims=3,legend=[0,1,2,3,4],size=[7,5])

# # data=pd.read_excel(io=r"E:\matlab2023a\toolbox\Drcluster_v3\test1.xlsx")
# # hyp.plot(data)
# # plt.show()

# data=pd.read_excel(io=r"E:\MCM-ICM\清风数学建模课件和代码（全套下载后请解压)\正课 配套的课件和代码\第10讲.聚类模型\代码和例题数据\1999年全国31个省份城镇居民家庭平均每人全年消费性支出数据  - 副本.xlsx")
# fg3=px.scatter(data, x='省份', y='省份', color='分类')
# fg3.show()



import numpy as np
import matplotlib.pyplot as plt

# 成绩数据
results = [
    {"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
    {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}
]

# 数据长度
data_length = len(results[0])

# 极坐标根据数据长度进行等分
angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)

# 标签
labels = [key for key in results[0].keys()]

# 分数
score = [[v for v in result.values()] for result in results]

# 使雷达图数据封闭
score_a = np.concatenate((score[0], [score[0][0]]))
score_b = np.concatenate((score[1], [score[1][0]]))
angles = np.concatenate((angles, [angles[0]]))
labels = np.concatenate((labels, [labels[0]]))

# 设置图形的大小
fig = plt.figure(figsize=(8, 6), dpi=100)

# 新建一个子图
ax = plt.subplot(111, polar=True)

# 绘制雷达图
ax.plot(angles, score_a, color='g', label="同学 A")
ax.plot(angles, score_b, color='b', label="同学 B")

# 设置雷达图中每一项的标签显示
ax.set_thetagrids(angles*180/np.pi, labels)

# 设置雷达图的0度起始位置
ax.set_theta_zero_location('N')

# 设置雷达图的坐标刻度范围
ax.set_rlim(0, 100)

# 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
ax.set_rlabel_position(270)

# 设置标题和图例
ax.set_title("计算机专业大一（上）")
plt.legend(["同学 A", "同学 B"], loc='best')

# 显示图形
plt.show()
