# @Time   :2021/10/10 10:55
# @Author :wcz
# @File   :sele1.py

from  selenium import webdriver

# 可以通过以下函数定位元素
'''
find_element_by_class_name 通过类名称定位
find_element_by_id 通过id定位
find_...by_css_selector 通过css选择器
find_...by_tag_name
find_...by_xpath
find_..._by_link_text 靠链接的文本来定位

'''

browser=webdriver.Chrome()

browser.get('http://www.baidu.com')

'''把上面定位element改为find_elements_...可以返回一个list包括所有符合条件的元素
 再调用以下方法可以提取需要的信息：
 element.get_attribute获取属性
 element.text 获取文本
 element.tag_name
 element.id '''

'''ActionChains类 用于在页面上进行鼠标模拟操作 单击 双击 右键单击 拖拽 按住'''

'''
click(element) 单击某个节点
click_and_hold(element)单击某个节点然后不放
context_click(...)右键单击某个节点
double_click(..)双击某个节点
drag_and_drop(source,target)按住某个节点拖拽到另一个节点
drag_and_drop_by_offset(source,xoffset,yoffset),沿x y轴拖动距离
key_down 按下特殊键 
(只能按下ctrl alt shift 还有字母键 如ctrl+c)
key_up 释放特殊键
move_to_element(element)鼠标移动到某个节点
在一段时间内暂停输入 pause(second)
perform（） 执行多个操作
release() 释放鼠标
reset_actions() 重置操作

'''

'''
如果出现了弹窗
可以先用以下方法获得对话框 alert=driver.switch_to_alert()
对于alert对象可以调用以下方法：
alert.accept() 确定 
alert.dismiss()关闭对话框
alert.send_keys() 传入值
text()获取对话框文本

'''

'''页面截图 driver.save_screenshot'''

# 窗口的切换是使用driver.switch_to_window("窗口名")
# 也可以 for handle in driver.window_handles:
    #driver.switch_to_window(handle)

# driver.forward()
# driver.back()