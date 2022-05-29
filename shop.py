#Shop: отображение страницы товара
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
# driver.find_element_by_id("username").send_keys("sidorova@gmail.com")
# driver.find_element_by_id("password").send_keys("Sidorova2022")
# driver.find_element_by_css_selector("[name='login']").click()
# #3
# driver.find_element_by_id("menu-item-40").click()
# #4
# driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()
# #5
# element = driver.find_element_by_css_selector("[class='summary entry-summary']")
# element_get_text = element.text
# assert "HTML5 Forms" in element_get_text
# driver.quit()
#Shop: количество товаров в категории
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
# driver.find_element_by_id("username").send_keys("sidorova@gmail.com")
# driver.find_element_by_id("password").send_keys("Sidorova2022")
# driver.find_element_by_css_selector("[name='login']").click()
# #3
# driver.find_element_by_id("menu-item-40").click()
# #4
# driver.find_element_by_link_text("HTML").click()
# time.sleep(10)
# #5
# items_count=driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(items_count)==3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка. Количество товаров на странице: " + str(len(items_count)))
# driver.quit()

#Shop: сортировка товаров
#
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
# driver.find_element_by_id("username").send_keys("sidorova@gmail.com")
# driver.find_element_by_id("password").send_keys("Sidorova2022")
# driver.find_element_by_css_selector("[name='login']").click()
# #3
# driver.find_element_by_id("menu-item-40").click()
# #4
# from selenium.webdriver.support.select import Select
# selector = driver.find_element_by_class_name("orderby")
# Default_sorting_selected = selector.get_attribute("value")
# if Default_sorting_selected == "menu_order":
#     print("Выбран вариант сортировки по умолчанию")
# else:
#     print("Выбран иной вариант сортировки")
# #5
# driver.execute_script("window.scrollBy(0, 400);")
# select = Select(selector)
# select.select_by_value("price-desc")
# #6
# selector_new = driver.find_element_by_class_name("orderby")
# Sort_by_price = selector_new.get_attribute("value")
# if Sort_by_price == "price-desc":
#     print("в селекторе выбран вариант сортировки по цене от большей к меньшей")
# else:
#     print("Выбран иной вариант сортировки")
# driver.quit()

#  Shop: отображение, скидка товара
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
# driver.find_element_by_id("username").send_keys("sidorova@gmail.com")
# driver.find_element_by_id("password").send_keys("Sidorova2022")
# driver.find_element_by_css_selector("[name='login']").click()
# #3
# driver.find_element_by_id("menu-item-40").click()
# #4
# driver.find_element_by_class_name("post-169").click()
# #5
# old_price = driver.find_element_by_css_selector(".price>del>span")
# old_price_get_text = old_price.text
# assert old_price_get_text == "₹600.00"
# #6
# new_price = driver.find_element_by_css_selector(".price>ins>span")
# new_price_get_text = new_price.text
# assert new_price_get_text == "₹450.00"
# #7
# book_cover_element = wait.until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover_element.click()
# #8
# book_cover_close = wait.until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
# driver.quit()

# Shop: проверка цены в корзине

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver,20)
# #1
# driver.get("http://practice.automationtesting.in/")
# #2
# driver.find_element_by_id("menu-item-40").click()
# #3
# add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='182']")
# add_to_basket_btn.click()
# #4
# View_Basket = wait.until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[title='View Basket']"), "View Basket"))
# basket_quantity = driver.find_element_by_class_name("cartcontents")
# basket_quantity_text = basket_quantity.text
# assert basket_quantity_text == "1 Item"
# basket_price = driver.find_element_by_class_name("amount")
# basket_price_text = basket_price.text
# assert basket_price_text == "₹180.00"
# #5
# driver.find_element_by_id("wpmenucartli").click()
# #6
# subtotal = wait.until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "₹180.00"))
# #7
# total = wait.until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "order-total"), "₹189.00"))
# #7
# driver.quit()
#Shop: работа в корзине
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver,20)
# #1
# driver.get("http://practice.automationtesting.in/")
# #2
# driver.find_element_by_id("menu-item-40").click()
# #3
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(5)
# driver.find_element_by_css_selector("[data-product_id='180']").click()
# #4
# driver.find_element_by_id("wpmenucartli").click()
# #5
# time.sleep(5)
# driver.find_element_by_css_selector("[data-product_id='182']").click()
# #6
# undo_btn = wait.until(
# EC.element_to_be_clickable((By.LINK_TEXT, "Undo?")) )
# undo_btn.click()
# #7
# quantity = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# quantity.clear()
# quantity.send_keys("3")
# quantity.click()
# #8
# driver.find_element_by_css_selector("[name='update_cart']").click()
# #9
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == "3"
# #10
# time.sleep(5)
# driver.find_element_by_css_selector("[name='apply_coupon']").click()
# #11
# message_text= wait.until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))
# driver.quit()
#Shop: покупка товара

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver,20)
#1
driver.get("http://practice.automationtesting.in/")
#2
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
#3
driver.find_element_by_css_selector("[data-product_id='182']").click()
View_Basket = wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[title='View Basket']"), "View Basket"))
#4
driver.find_element_by_id("wpmenucartli").click()
#5
checkout_btn = wait.until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")) )
checkout_btn.click()
#6
first_name=wait.until(
EC.element_to_be_clickable((By.ID, "billing_first_name")) )
first_name.send_keys("Elly")
last_name=driver.find_element_by_id("billing_last_name")
last_name.send_keys("Sidorova")
driver.find_element_by_id("billing_email").send_keys("sidorova@gmail.com")
driver.find_element_by_id("billing_phone").send_keys("89121451289")
country=driver.find_element_by_id("s2id_billing_country")
country.click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
driver.find_element_by_id("select2-results-1").click()
driver.find_element_by_id("billing_address_1").send_keys("Lenina")
driver.find_element_by_id("billing_city").send_keys("Samara")
driver.find_element_by_id("billing_state").send_keys("Samarskaya oblast")
driver.find_element_by_id("billing_postcode").send_keys("443028")
#7
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
driver.find_element_by_css_selector("[value='cheque']").click()
#8
driver.find_element_by_id("place_order").click()
#9
page_content = wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce>p"), "Thank you. Your order has been received."))
#10
check_payments_message = wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)>td"), "Check Payments"))
driver.quit()