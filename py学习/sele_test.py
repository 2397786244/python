# 定位元素 鼠标移动等操作学习
# @Time   :2021/10/10 11:36
# @Author :wcz
# @File   :sele_test.py

from selenium import webdriver

# url = 'https://www.gushiwen.cn/'
# browser=webdriver.Chrome()

# browser.get(url)
'''id_list = browser.find_elements_by_id("btnYiwen2eec662bc115")
print(id_list)''' # 通过id定位

'''class_list = browser.find_elements_by_class_name('contson')
for each_class in class_list: 通过class定位 返回的是WebElement的列表 可以通过for in 来继续操作'''

# 下面通过xpath来定位
from lxml import etree

'''get_resp = browser.find_elements_by_xpath('//div[@class="sons"]//div[@class="yizhu"]')
print(get_resp)'''

# 对于页面上文本链接的定位
#使用text_link
'''get_textlink = browser.find_element_by_link_text('作者')

print(get_textlink)'''
import time
time.sleep(1)
# 以下是对浏览器的操作 通过webdriver
'''browser.refresh()
browser.set_window_size(1200,800)
tlink = browser.find_element_by_link_text("作者")
tlink.click()'''

# 以上完成了对指定页面的textlink的点击操作，并完成了设置浏览器页面大小

from selenium.webdriver.common.action_chains import ActionChains

nbuoj_url = 'http://www.nbuoj.com'

browser1 = webdriver.Chrome()

browser1.get(nbuoj_url)

get_login = browser1.find_element_by_xpath('//ul[@class="nav pull-right"]/li/a')

ActionChains(browser1).move_to_element(get_login).perform()

# 鼠标悬停在登录按钮上
time.sleep(1)

# 以下完成了自动登录nbuoj.com

uid_enter = browser1.find_element_by_name('uid')

uid_enter.send_keys('这里输入你的账号')

pwd_enter = browser1.find_element_by_name('password')

pwd_enter.send_keys('这里输入密码')

login_bottom = browser1.find_element_by_name('submit')

login_bottom.click()