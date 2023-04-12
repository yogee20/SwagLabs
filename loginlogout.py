import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.maximize_window()

print(driver.title)

username = driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")

time.sleep(2)

password = driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")

time.sleep(4)

login = driver.find_element(By.XPATH, "//*[@id='login-button']").click()

time.sleep(2)

select_item1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()

time.sleep(2)

add_to_cart = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()

time.sleep(2)

cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

time.sleep(2)

remove = driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-backpack']").click()

time.sleep(2)

continue_shopping = driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()

time.sleep(2)

select_item2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").click()

time.sleep(2)

add_to_cart = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()

time.sleep(2)

cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

time.sleep(2)

checkout = driver.find_element(By.XPATH, "//*[@id='checkout']").click()

time.sleep(2)

logout= driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()

time.sleep(2)

logout = driver.find_element(By. XPATH, "//*[@id='logout_sidebar_link']").click()
