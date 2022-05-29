#Registration_login: регистрация аккаунта
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver,20)
# #1
# driver.get("http://practice.automationtesting.in/")
# #2
# driver.find_element_by_link_text("My Account").click()
# #3
# driver.find_element_by_id("reg_email").send_keys("sidorova@gmail.com")
# #4
# driver.find_element_by_id("reg_password").send_keys("Sidorova2022")
# #5
# driver.find_element_by_class_name("register").click()
# driver.quit()

##   Registration_login: логин в систему

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,20)
#1
driver.get("http://practice.automationtesting.in/")
#2
driver.find_element_by_link_text("My Account").click()
#3
driver.find_element_by_id("username").send_keys("sidorova@gmail.com")
#4
driver.find_element_by_id("password").send_keys("Sidorova2022")
#5
driver.find_element_by_css_selector("[name='login']").click()
#6
element = driver.find_element_by_link_text("Logout")
element_get_text = element.text
assert element_get_text == "Logout"

driver.quit()