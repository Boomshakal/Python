from  selenium import webdriver
import time
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('https://user.qzone.qq.com')
user ='362169885'
password ='lhm9223572309'

browser.switch_to_frame('login_frame')
log = browser.find_element_by_id("switcher_plogin")
log.click()
time.sleep(1)
username = browser.find_element_by_id('u')
username.send_keys(user)
ps = browser.find_element_by_id('p')
ps.send_keys(password)
btn = browser.find_element_by_id('login_button')
time.sleep(1)
btn.click()
time.sleep(2)
browser.get('https://user.qzone.qq.com/{}'.format(username))

friendAction = browser.find_element_by_id('tab_menu_friend')
b=[]
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html,"html.parser")
a = soup.find_all('a', attrs={'data-clicklog': 'nick'})
b = soup.find_all('div', attrs={'class': 'f-info'})

for i in range(len(a)):
    if(b[i].text == None):
        b[i].text = '无法显示'
    print(':' +b[i].text + '\n')
