from selenium import webdriver
import time

URL = 'https://portal.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(3)


click_register = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/div/div[2]/div/a/span')
click_register.click()
time.sleep(3)

enter_email_id = driver.find_element_by_id('input-19')
enter_email_id.click()
enter_email_id.send_keys('8830627731')
time.sleep(4)
register = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[4]/form/button')
register.click()
time.sleep(2)

enter_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/form/div/div[1]')
enter_otp.click()

time.sleep(20)
verify_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/form/button/span')
verify_otp.click()


time.sleep(3)
driver.close()
