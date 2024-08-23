from selenium import webdriver
import time

URL = 'https://portal.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(3)


enter_email = driver.find_element_by_xpath('//*[@id="input-16"]')
enter_email.send_keys('helange2020@gmail.com')
time.sleep(2)

enter_password = driver.find_element_by_xpath('//*[@id="input-19"]')
enter_password.send_keys('Aptcoder#123')
time.sleep(2)


click_log_in = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/button/span')
click_log_in.click()

time.sleep(6)
driver.close()
