# @Time   :2021/10/3 20:59
# @Author :wcz
# @File   :spider_city_code.py

import requests
import re
import bs4

url = 'http://www.weather.com.cn/textFC/db.shtml'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

city_page = requests.get(url,headers=headers).content

page_text = city_page.decode('utf-8','ignore')


get_city_bs4 = bs4.BeautifulSoup(city_page,'lxml')

#以下得到国内除华北外分区域的城市网页后缀

addr_lists=[]
region_ul = get_city_bs4.find("div",attrs={'class': 'lqcontentBoxheader'})
region_list=region_ul.find_all(name="a")

for each_region in region_list:
    addr_lists.append("http://weather.com.cn" + each_region["href"])
# print(addr_lists) 这里测试各个省直辖市的url

for each_url in addr_lists:
    get_page = requests.get(each_url,headers=headers).content
    get_page.decode("utf-8","ignore")
    cities = bs4.BeautifulSoup(get_page,"lxml")
    cities_div = cities.find("div",attrs={'class':'conMidtab3'})
    cities_list = cities_div.find_all(name="a")

    for each_a in cities_list:
        if each_a.get("href") is not None and each_a.text != "详情":
            print(each_a.text + each_a.get("href"))
            #到此输出的内容中为城市名+带有城市编号的url 后续通过正则表达式可以取得编码


