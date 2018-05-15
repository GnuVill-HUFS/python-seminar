from selenium import webdriver

browser = webdriver.Chrome()
# 크롬일때

#browser = webdriver.Edge()
# Edge일때

web = 'http://music.naver.com/'
browser.get(web)


ranks = browser.find_elements_by_class_name('num')
music_titles = browser.find_elements_by_class_name('m_ell')

artists = browser.find_elements_by_class_name('_artist')

all_info = []
for i in range(9):
    all_info.append([ranks[i].text, music_titles[i].text, artists[i].text])

for rank, title, artist in all_info:
    print(str(rank) + ' 순위 ' + '제목 : ' + str(title) + ' 가수 : '+ str(artist))

browser.quit()