from selenium import webdriver
import time

URL = 'https://test.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(2)


enter_email = driver.find_element_by_xpath('//*[@id="input-16"]')
enter_email.send_keys('nikhil.admin@aptcoder.com')
time.sleep(2)

enter_password = driver.find_element_by_xpath('//*[@id="input-19"]')
enter_password.send_keys('Aptcoder#123')
time.sleep(2)


click_log_in = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/button/span')
click_log_in.click()
time.sleep(2)

click_user = driver.find_elements_by_class_name('v-list-item__title')[1]
click_user.click()
time.sleep(2)

choose_user = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div/div/header/div/div[5]/div/div/div[1]/div[1]/div[2]/div/i')
choose_user.click()
time.sleep(2)

select_teacher = driver.find_elements_by_class_name('v-list-item__title')[9]
select_teacher.click()
time.sleep(2)

click_filter = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/main/div/div/header/div/button[1]/span/button')
click_filter.click()
time.sleep(2)

enter_first_name = driver.find_element_by_xpath('//*[@id="input-362"]')
enter_first_name.click()
time.sleep(1)
enter_first_name.send_keys('Juhi')
time.sleep(2)

apply = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/button[1]')
apply.click()
time.sleep(2)

# click_view_calendar = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div/div/div/div[3]/div/div[1]/table/tbody/tr/td[8]/button[4]')
# click_view_calendar.click()
# time.sleep(3)
# driver.back()

click_view_class = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div/div/div/div[3]/div/div[1]/table/tbody/tr/td[8]/button[5]')
click_view_class.click()


time.sleep(4)
driver.close()
