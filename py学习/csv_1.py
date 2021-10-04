# 学习用csv（纯文本）的方式存放爬虫取得的数据
# @Time   :2021/10/4 22:39
# @Author :wcz
# @File   :csv_1.py

"""csv与excel文件有多个不同点：所有值都是字符串类型；不能设置字体颜色等；不能指定单元格长宽高，合并单元格等；没有多个工作表；不能嵌入图片等。"""

import csv
import os

# 使用csv的writerow写入一行 writerows写入多行

data1=[[1,2,3,4,5],["a",'b','c','d','e'],['i','j','k','h','i']]


os.mkdir("d:\\pyproject\\csv_test")
with open("d:\\pyproject\\csv_test\\c1.csv","w",newline='') as f:
    write1 = csv.writer(f) # 这里重点
    for each_row in data1:
        write1.writerow(each_row)
        # 这个是单行的写入
with open('d:\\pyproject\\csv_test\\c2.csv','w',newline='') as f2:
    write2 = csv.writer(f2)
    write2.writerows(data1)
    # 如果不添加newline='' 每次写入一个row会多一行空格的





