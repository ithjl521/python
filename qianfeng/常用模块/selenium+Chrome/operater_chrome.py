from selenium import webdriver
import time

# 模拟操作google浏览器

path = r'chromedriver.exe'
# 模拟创建浏览器对象
browser = webdriver.Chrome(executable_path=path)

# 打开百度
url = 'https://www.baidu.com/'
browser.get(url)
time.sleep(3)

# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往输入框写文字
my_input.send_keys('中国')
time.sleep(2)
#查找搜索按钮
button = browser.find_elements_by_class_name('s_btn')[0]
# 点击搜索按钮
button.click()
time.sleep(3)


# 关闭浏览器
browser.quit()




