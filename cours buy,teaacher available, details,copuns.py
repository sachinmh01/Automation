from selenium import webdriver
import time

URL = 'https://test.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(3)


enter_email = driver.find_element_by_xpath('//*[@id="input-16"]')
enter_email.send_keys('sachinhelange123@gmail.com')
time.sleep(1)

enter_password = driver.find_element_by_xpath('//*[@id="input-19"]')
enter_password.send_keys('Aptcoder#123')
time.sleep(1)


click_log_in = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/button/span')
click_log_in.click()
time.sleep(2)

driver.execute_script("window.scrollTo(0,400)")

time.sleep(3)
buy_course = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div/div/div/div[1]/div[4]/div/div[4]/div/button')
buy_course.click()

time.sleep(3)
click = driver.find_element_by_id('input-246')
click.click()
time.sleep(3)

search_teacher_name = driver.find_element_by_id('input-260')
search_teacher_name.click()
time.sleep(2)
search_teacher_name.send_keys('Juhi')
time.sleep(1)
teacher_click = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div[2]')
teacher_click.click()
time.sleep(2)

driver.execute_script("window.scrollTo(0,400)")
time.sleep(3)
select_slot = driver.find_element_by_xpath('//*[@class="v-calendar-daily__day v-present"]/div[5]')
time.sleep(3)
select_slot.click()
time.sleep(4)

# driver.save_screenshot('slot.jpg')
# time.sleep(3)
driver.close()
