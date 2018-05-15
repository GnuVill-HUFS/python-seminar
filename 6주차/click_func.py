from selenium import webdriver

browser = webdriver.Chrome()
# 크롬일때

#browser = webdriver.Edge()
# Edge일때

web = 'http://naver.com/'
browser.get(web)

menus = browser.find_elements_by_class_name('an_item')
temp = None
for m in menus:
    if '뮤직' in m.text:
        temp = m

temp.click()