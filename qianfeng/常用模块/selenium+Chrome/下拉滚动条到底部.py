from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#构建一个chrome对象
browser = webdriver.Chrome('chromedriver.exe', options=chrome_options)

url = 'http://sc.chinaz.com/tupian/bangongrenwu.html'
browser.get(url)
time.sleep(2)

# 截图
browser.save_screenshot('a.png')
# 保存源代码到文件
html = browser.page_source
with open(r'a.html','w',encoding='utf8') as fp:
	fp.write(html)


# 让浏览器执行简单的JS代码，模拟滚动到底部
js = 'document.documentElement.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)


# 再次截图
browser.save_screenshot('b.png')
# 获取网页代码，保存到文件
html = browser.page_source
with open(r'b.html','w',encoding='utf8') as fp:
	fp.write(html)

browser.quit()



