from selenium import webdriver
import time

URL = 'https://test.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(2)


enter_email = driver.find_element_by_xpath('//*[@id="input-16"]')
enter_email.send_keys('sachinhelange123@gmail.com')
time.sleep(1)

enter_password = driver.find_element_by_xpath('//*[@id="input-19"]')
enter_password.send_keys('Aptcoder#123')
time.sleep(1)

click_log_in = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/button/span')
click_log_in.click()
time.sleep(2)

click_orders = driver.find_elements_by_class_name('v-list-item__title')[2]
click_orders.click()
time.sleep(3)

check_payment = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/div/table/tbody/tr[1]/td[8]/button[1]')
check_payment.click()
time.sleep(3)

retry_payment = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/div/div/div/div[2]/div/table/tbody/tr[1]/td[8]/button[2]')
retry_payment.click()

time.sleep(8)
driver.close()
