from selenium import webdriver
import time

URL = 'https://test.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(3)


click_register = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/div/div[2]/div/a/span')
click_register.click()
time.sleep(3)

enter_email_id = driver.find_element_by_id('input-19')
enter_email_id.click()
enter_email_id.send_keys('sachinhelange123@gmail.com')
time.sleep(4)
register = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[4]/form/button')
register.click()

time.sleep(65)
click_resend = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/div/button')
click_resend.click()
time.sleep(2)
driver.save_screenshot('resend.jpg')


time.sleep(6)
driver.close()
