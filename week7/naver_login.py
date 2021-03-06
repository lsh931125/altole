from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://nid.naver.com/nidlogin.login')

driver.execute_script("document.getElementsByName('id')[0].value = ''")
driver.execute_script("document.getElementsByName('pw')[0].value = ''")

driver.find_element_by_xpath('//*[@id="log.login"]').click()