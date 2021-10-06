# 写一个应对ajax动态加载的爬虫
# @Time   :2021/10/6 15:52
# @Author :wcz
# @File   :js_spider.py
import json
import requests

import re
import time


url = 'https://huaban.com/boards/36260008/'
# 这个用于获取第一页20张图片
board_url = 'https://huaban.com/boards/36260008/?kufa3cli&max=2424854609&limit=20&wfl=1'
ajax_headers = {'Host':'huaban.com','Accept':'application/json','X-Request':'JSON','X-Requested-With':'XMLHttpRequest'}

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
page_1_text = requests.get(url,headers=headers).text

regex = 'pins":(.*?)};'

id_lists=[]

def get_ajax_page(url): # 这个函数用于解析每一个包含20张图片的ajax页面
    page_text = requests.get(url,ajax_headers).text
    pin_id = re.search(regex,page_text,re.S)
    id_dict = json.loads(pin_id.group(1))
    for each_pic in id_dict:
        print(each_pic['file']['key'])
        id_lists.append(each_pic["pin_id"])
    return id_lists[-1] # 函数返回最后一个pin_id 也是下一个请求页面的参数之一

ajax_url2 = 'https://huaban.com/boards/36260008/?kufanmvg&max=1115574017&limit=20&wfl=1' #ajax_url2 中max参数为上一个页面最后一个
# pin_id填入，然后请求 得到这个页面的key(图片下载规则：https://hbimg.huabanimg.com/+key+_fw658/format/webp得到下载地址) pin_id的最后一个再用于请求下一个页面.

get_ajax_page(ajax_url2)




