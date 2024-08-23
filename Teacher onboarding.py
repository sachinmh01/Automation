from selenium import webdriver
import time

# 8830627135

URL = 'https://test.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(2)


login_with_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/div[1]/div/div[1]/div/div')
login_with_otp.click()
time.sleep(1)

enter_button = driver.find_element_by_xpath('//*[@id="input-16"]')
enter_button.send_keys('8830627135')
time.sleep(2)


click_log_in = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/button/span')
click_log_in.click()
time.sleep(2)

enter_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/form/div/div[1]')
enter_otp.click()

time.sleep(11)
verify_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/form/button/span')
verify_otp.click()
time.sleep(3)

# date_of_birth = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/div[1]/div[2]/div[1]/div/label')
# date_of_birth.click()
# time.sleep(1)

select_date = driver.find_elements_by_class_name('v-btn__content')[10]
select_date.click()


time.sleep(2)
driver.close()