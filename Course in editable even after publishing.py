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

select_courses = driver.find_elements_by_class_name('v-list-item__title')[3]
select_courses.click()
time.sleep(2)

click_course = driver.find_element_by_xpath('/html/body/div/div/div/main/div/div/div/div[2]/button/div[2]/i')
click_course.click()
time.sleep(1)

click_edit_course = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div/div/div/div[2]/div/div/div/div/div[3]/div/button/span/i')
click_edit_course.click()
time.sleep(1)

# edit = driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/form/div/div/div[1]/div[1]/div/div/div[1]/div/label')
# edit.click()
# time.sleep(4)
# edit.send_keys('with upsc')
# time.sleep(1)


price_edit = driver.find_element_by_xpath('/html/body/div/div[4]/div/div/div/form/div/div/div[3]/div[2]/div/div/div[1]/div/label')
price_edit.click()
time.sleep(1)
price_edit.send_keys('0')
time.sleep(1)

save_button = driver.find_element_by_xpath('/html/body/div/div[4]/div/div/div/form/div/div/div[4]/button[2]')
save_button.click()


time.sleep(4)
driver.close()