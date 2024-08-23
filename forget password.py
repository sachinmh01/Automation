from selenium import webdriver
import time

URL = 'https://portal.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(3)


click_log_in = driver.find_element_by_class_name('text-subtitle-2')
click_log_in.click()

time.sleep(3)
driver.close()
