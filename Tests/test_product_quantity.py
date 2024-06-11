import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class TestProductQuantity:
    def test_product_quantity(self, setup_teardown):
        driver = setup_teardown
        assert "Automation Exercise" in driver.title
        view_product = driver.find_element(By.XPATH,"//div[4]//div[1]//div[2]//ul[1]//li[1]//a[1]")
        time.sleep(3)
        view_product.click()

        product_detail_loaded = driver.find_element(By.CSS_SELECTOR, '.product-information')
        assert product_detail_loaded.is_displayed(), "Product detail is not opened"
        quantity_input = driver.find_element(By.ID,"quantity")
        quantity_input.clear()
        quantity_input.send_keys("4")

        add_to_cart_button = driver.find_element(By.XPATH, "//button[@type='button']")
        time.sleep(3)
        add_to_cart_button.click()

        view_cart_button = driver.find_element(By.XPATH, "//u[normalize-space()='View Cart']")
        time.sleep(5)
        view_cart_button.click()

        cart_page_loaded = driver.find_element(By.CSS_SELECTOR, '.cart_info')

        assert cart_page_loaded.is_displayed(), "Cart page is not loaded"

        product_quantity = driver.find_element(By.XPATH, "//button[@class='disabled']")
        assert product_quantity.text == '4', "Product quantity in cart is not correct"



