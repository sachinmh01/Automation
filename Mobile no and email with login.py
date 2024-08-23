from selenium import webdriver
import time

URL = 'https://test.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(3)

login_with_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/div[1]/div/div[1]/div/div')
login_with_otp.click()
time.sleep(3)

enter_button = driver.find_element_by_xpath('//*[@id="input-16"]')
enter_button.send_keys('8830627731')
time.sleep(4)


click_log_in = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/button/span')
click_log_in.click()
time.sleep(3)

enter_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/form/div/div[1]')
enter_otp.click()

time.sleep(20)
verify_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/form/button/span')
verify_otp.click()

time.sleep(10)
driver.close()
