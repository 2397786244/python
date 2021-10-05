# 学习csv的dictwriter csv的读取
# @Time   :2021/10/5 12:06
# @Author :wcz
# @File   :csv_2.py

import csv
import os

headers=['id','name','birth','phonenumber','location']
data_1=[{'id':'1','name':'wcz','birth':'020714','phonenumber':"19857252150",'location':"zjhz"},{'id':'2','name':'xc','birth':'000000','phonenumber':"123456789",'location':"zjhz"}]
# os.mkdir('d:\\pyproject\\csv_test')
"""with open("d:\\pyproject\\csv_test\\c3.csv", 'w', newline="") as f1:
    writer1 = csv.DictWriter(f1,headers)
    writer1.writeheader()
    for each_row in data_1:
        writer1.writerow(each_row)"""
'''以上完成了对c3.csv的以字典方式写入 注意writer1=csv.DictWriter(f1,headers),writer1.writeheader()'''

'''接下来实现csv的读取操作'''

with open("d:\\pyproject\\csv_test\\c3.csv") as f2:
    reader1 = csv.reader(f2)
    # print(list(reader1)[0][1])  即打印b1单元格内容 name
    '''for each_row in reader1:
        print(each_row[1])  打印每一行内容'''
    '''for each_row in reader1:
        print(reader1.line_num,each_row) 这个与上一行代码的区别 这里打印会带1,2,3这样的行号
    '''

    reader2=csv.DictReader(f2)
    for each_row in reader2:
        # print(each_row['name']) 这里可以打印key所对应的所有值 把csv的首行作为表头
        print(each_row)  # 这里是打印键值对 例如：{'id': '1', 'name': 'wcz', 'birth': '020714', 'phonenumber': '19857252150', 'location': 'zjhz'}

