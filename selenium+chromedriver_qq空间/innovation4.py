from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
driver = webdriver.Chrome(chrome_options=options)
url ='https://www.innovation4.cn/library/FileData/29267?page=1'
driver.get(url)
text = driver.find_element_by_id('pf1').text
print(text.decode('utf-8'))
driver.close()