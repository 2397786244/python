# 这个文件用于爬取星座运势并储存在csv中
# @Time   :2021/10/5 12:36
# @Author :wcz
# @File   :csv_3.py

import csv
import re

import requests
import bs4

url = 'http://www.xzw.com/fortune'

headers=['星座','生日时间','运势评分','今日运势']

ua_headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'}

page_text=requests.get(url,headers=ua_headers).text

page_bs4=bs4.BeautifulSoup(page_text,'lxml')

xz_list = page_bs4.find("div",attrs={"class":'alb'})
xz = xz_list.find_all(name="strong")
'''for each_xz in xz:
    print(each_xz.text)'''
birth= xz_list.find_all(name='small')
regex_score = '<em class="star_m"><em style="width:(.*?%)"></em></em>'

getscore = re.findall(regex_score,page_text, re.S)
print(getscore)
today=[]

