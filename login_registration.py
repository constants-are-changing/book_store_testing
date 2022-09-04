# регистрация аккаунта
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import pyautogui

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)


try:
    my_account_btn = driver.find_element(By.PARTIAL_LINK_TEXT, 'My Account')
    my_account_btn.click()
    email_field = driver.find_element(By.ID, 'reg_email')
    email_field.send_keys('enumerate@none.net')
    reg_password_field = driver.find_element(By.ID, 'reg_password')
    reg_password_field.send_keys('6Ight&Sev6n')
    body = driver.find_element(By.ID, 'body')
    body.click()
    reg_btn = driver.find_element(By.CSS_SELECTOR, '[value="Register"]')
    reg_btn.click()

finally:
    time.sleep(5)
    driver.quit()

# логин в систему
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)


try:
    my_account_btn = driver.find_element(By.PARTIAL_LINK_TEXT, 'My Account')
    my_account_btn.click()
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('enumerate@none.net')
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('6Ight&Sev6n')
    login_btn = driver.find_element(By.CSS_SELECTOR, '[name="login"]')
    login_btn.click()



finally:
    time.sleep(5)
    driver.quit()