# отображение страницы товара
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
    shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 a')
    shop.click()
    html5_forms = driver.find_element(By.CSS_SELECTOR, '[data-product_id="181"]')
    html5_forms.click()
    header = driver.find_element(By.CSS_SELECTOR, '.summary.entry-summary h1')
    text = header.text
    assert text == 'HTML5 Forms'

finally:
    time.sleep(5)
    driver.quit()

# количество товаров в категории
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
    shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 a')
    shop.click()
    html = driver.find_element(By.CSS_SELECTOR, '.cat-item.cat-item-19 a')
    html.click()
    books_on_page = driver.find_elements(By.CLASS_NAME, 'attachment-shop_catalog')
    assert len(books_on_page) == 3

finally:
    time.sleep(5)
    driver.quit()

# сортировка товаров
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 a')
    shop.click()
    sorting = driver.find_element(By.CSS_SELECTOR, '[selected="selected"]')
    assert sorting.text == 'Default sorting'
    selector_sort = driver.find_element(By.CLASS_NAME, 'orderby')
    sort_element = Select(selector_sort)
    sort_element.select_by_value('price-desc')
    sorting_second = driver.find_element(By.CSS_SELECTOR, '[selected="selected"]')
    assert sorting_second.text == 'Sort by price: high to low'


finally:
    time.sleep(5)
    driver.quit()

# отображение, скидка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
wait = WebDriverWait(driver, 10)

try:
    my_account_btn = driver.find_element(By.PARTIAL_LINK_TEXT, 'My Account')
    my_account_btn.click()
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('enumerate@none.net')
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('6Ight&Sev6n')
    login_btn = driver.find_element(By.CSS_SELECTOR, '[name="login"]')
    login_btn.click()
    shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 a')
    shop.click()
    android_book = driver.find_element(By.CSS_SELECTOR, '[data-product_id="169"]')
    android_book.click()

    book_old_price = driver.find_element(By.CSS_SELECTOR, 'del span')
    book_old_price_text = book_old_price.text
    assert book_old_price_text == '₹600.00'

    book_new_price = driver.find_element(By.CSS_SELECTOR, 'ins span')
    book_new_price_text = book_new_price.text
    assert book_new_price_text == '₹450.00'

    book_cover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Android Quick Start Guide"]')))
    book_cover.click()

    book_cover_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')))
    book_cover_close.click()

finally:
    time.sleep(5)
    driver.quit()

# проверка цены в корзине
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
wait = WebDriverWait(driver, 10)

try:
    shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 a')
    shop.click()
    html_webapp_book = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
    html_webapp_book.click()

    cart_count = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'cartcontents'), '1 Item'))
    cart_price = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.wpmenucart-contents .amount'),
                                                             '₹180.00'))

    cart = driver.find_element(By.CLASS_NAME, 'wpmenucart-contents')
    cart.click()

    subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]'), '₹180.00'))
    total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'strong span'), '₹183.60'))

finally:
    time.sleep(5)
    driver.quit()

# работа в корзине
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
wait = WebDriverWait(driver, 10)

try:
    shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 a')
    shop.click()
    html_webapp_book = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
    html_webapp_book.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 400);")
    js_data_book = driver.find_element(By.CSS_SELECTOR, '[data-product_id="180"]')
    js_data_book.click()

    cart = driver.find_element(By.CLASS_NAME, 'wpmenucart-contents')
    cart.click()
    remove_html_webapp_book = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
    remove_html_webapp_book.click()
    undo_remove = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Undo?')))
    undo_remove.click()
    js_data_book_quantity = driver.find_element(By.CSS_SELECTOR, '[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
    js_data_book_quantity.clear()
    js_data_book_quantity.send_keys('3')
    update_basket_btn = driver.find_element(By.CSS_SELECTOR, '[name="update_cart"]')
    update_basket_btn.click()
    js_quantity_value = js_data_book_quantity.get_attribute('value')
    assert js_quantity_value == '3'
    time.sleep(2)
    apply_coupon_btn = driver.find_element(By.CSS_SELECTOR, '[name="apply_coupon"]')
    apply_coupon_btn.click()
    coupon_error = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-error li'),
                                                               'Please enter a coupon code.'))

finally:
    time.sleep(5)
    driver.quit()

# покупка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
wait = WebDriverWait(driver, 10)

try:
    shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 a')
    shop.click()
    html_webapp_book = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
    html_webapp_book.click()

    cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="View your shopping cart"]')))
    cart.click()
    proceed_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button')))
    proceed_btn.click()

    first_name_field = driver.find_element(By.ID, 'billing_first_name')
    first_name_field.send_keys('John')
    last_name_field = driver.find_element(By.ID, 'billing_last_name')
    last_name_field.send_keys('Doe')
    email_field = driver.find_element(By.ID, 'billing_email')
    email_field.send_keys('enumerate@none.net')
    phone_field = driver.find_element(By.ID, 'billing_phone')
    phone_field.send_keys('88005553535')

    country_select = driver.find_element(By.ID, 's2id_billing_country')
    country_select.click()
    country_select_field = driver.find_element(By.ID, 's2id_autogen1_search')
    country_select_field.send_keys('Russia')
    country_match = driver.find_element(By.CSS_SELECTOR, '.select2-match')
    country_match.click()
    driver.execute_script("window.scrollBy(0, 500);")

    street_address_field = driver.find_element(By.ID, 'billing_address_1')
    street_address_field.send_keys('Elm')
    city_field = driver.find_element(By.ID, 'billing_city')
    city_field.send_keys('Saint-Petersburg')
    state_field = driver.find_element(By.ID, 'billing_state')
    state_field.send_keys('Main')
    postcode_field = driver.find_element(By.ID, 'billing_postcode')
    postcode_field.send_keys('5553535')
    driver.execute_script("window.scrollBy(0, 600);")

    payment_check = driver.find_element(By.ID, 'payment_method_cheque')
    payment_check.click()
    place_order_btn = driver.find_element(By.ID, 'place_order')
    place_order_btn.click()

    greeting = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'),
                                                           'Thank you. Your order has been received.'))
    payment_method = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr:nth-child(3) td'),
                                                                 'Check Payments'))

finally:
    time.sleep(5)
    driver.quit()
