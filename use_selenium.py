from selenium import webdriver
driver = webdriver.PhantomJS('C:/Users/DELL/Downloads/phantomjs-2.1.1-windows/bin')
driver.get('https://www.instagram.com/accounts/login/')
dom = driver.find_element_by_xpath('//')
import pdb
pdb.set_trace()
username = dom.find_element_by_name('username')
password = dom.find_element_by_name('password')
login_button = dom.find_element_by_xpath('//[@class="_qv64e _gexxb _4tgw8 _njrw0"]')
username.clear()
password.clear()
username.send_keys('your username')
password.send_keys('your password')
login_button.click()
driver.get('https://www.instagram.com/accounts/login')
if 'logged-in' in driver.page_source:
    print('Logged in')