from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

try:
    driver.execute_script("window.scrollBy(0, 600);")
    selenium_ruby_book = driver.find_element(By.CSS_SELECTOR, '[title="Selenium Ruby"]')
    selenium_ruby_book.click()
    review = driver.find_element(By.CSS_SELECTOR, '[href="#tab-reviews"]')
    review.click()
    driver.execute_script("window.scrollBy(0, 600);")
    star_five = driver.find_element(By.CLASS_NAME, 'star-5')
    star_five.click()
    review_field = driver.find_element(By.ID, 'comment')
    review_field.send_keys('Nice book!')
    driver.execute_script("window.scrollBy(0, 400);")
    name_field = driver.find_element(By.CSS_SELECTOR, '[name="author"]')
    name_field.send_keys('Ivan')
    email_field = driver.find_element(By.ID, 'email')
    email_field.send_keys('enumerate@none.net')
    submit_btn = driver.find_element(By.ID, 'submit')
    submit_btn.click()

finally:
    time.sleep(5)
    driver.quit()