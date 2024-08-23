from selenium import webdriver
import time

URL = 'https://test.aptcoder.com/#/login'
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get(URL)
driver.maximize_window()
time.sleep(2)


login_with_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/div[1]/div/div[1]/div/div')
login_with_otp.click()
time.sleep(2)

enter_button = driver.find_element_by_xpath('//*[@id="input-16"]')
enter_button.send_keys('8989123202')
time.sleep(2)


click_log_in = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/form/button/span')
click_log_in.click()
time.sleep(2)

enter_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/form/div/div[1]')
enter_otp.click()

time.sleep(11)
verify_otp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[5]/form/button/span')
verify_otp.click()
time.sleep(2)

enter_first_name = driver.find_element_by_xpath('//*[@id="input-81"]')
enter_first_name.click()
time.sleep(1)
enter_first_name.send_keys('yogita')
time.sleep(1)

enter_last_name = driver.find_element_by_xpath('//*[@id="input-84"]')
enter_last_name.click()
time.sleep(1)
enter_last_name.send_keys('ahire')


parent_name = driver.find_element_by_xpath('//*[@id="input-87"]')
parent_name.click()

parent_name.send_keys('mohan')

school_name = driver.find_element_by_xpath('//*[@id="input-90"]')
school_name.click()
school_name.send_keys('kynj')

grade = driver.find_element_by_id('input-93')
grade.click()
time.sleep(1)

select_grade = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div')
select_grade.click()
time.sleep(1)

enter_age = driver.find_element_by_xpath('//*[@id="input-98"]')
enter_age.click()
enter_age.send_keys('30')
time.sleep(1)

select_gender = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div/div/div[2]/form/div[3]/div[1]/div/div/div/div/div[1]/div/div[1]/label')
select_gender.click()

primary_address = driver.find_element_by_xpath('//*[@id="input-108"]')
primary_address.click()
primary_address.send_keys('delhi')

secondary_address = driver.find_element_by_xpath('//*[@id="input-111"]')
secondary_address.click()
secondary_address.send_keys('delhi')
time.sleep(1)

enter_pin = driver.find_element_by_xpath('//*[@id="input-114"]')
enter_pin.click()
enter_pin.send_keys('411057')
time.sleep(3)

driver.execute_script("window.scrollBy(0,300)")

register = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div/div/div[2]/div[2]/div[2]/button')
register.click()

time.sleep(5)
driver.close()
