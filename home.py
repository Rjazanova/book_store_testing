
#Home: добавление комментария
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
driver.execute_script("window.scrollBy(0, 600);")
#3
read_more_btn = wait.until(
EC.element_to_be_clickable((By.CSS_SELECTOR,".post-160 h3")) )
read_more_btn.click()
#4
driver.find_element_by_css_selector(".reviews_tab a").click()
#4
driver.find_element_by_class_name("star-5").click()
#5
Review = driver.find_element_by_id("comment")
driver.execute_script("return arguments[0].scrollIntoView(true);", Review)
Review.send_keys("Nice book!")
#6
driver.find_element_by_id("author").send_keys("Elly")
#7
driver.find_element_by_id("email").send_keys("sidorova@gmail.com")
#7
driver.find_element_by_id("submit").click()
time.sleep(10)
driver.quit()