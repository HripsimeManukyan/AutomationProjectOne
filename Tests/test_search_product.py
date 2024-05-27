import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProducts:
    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("http://automationexercise.com")
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()

    def test_search_and_verify_products_detail(self, driver):
        assert "Automation Exercise" in driver.title, "Home page not loaded correctly"

        driver.find_element(By.XPATH, "//a[@href='/products']").click()
        assert driver.find_element(By.XPATH,
                                   "//h2[text()='All Products']").is_displayed(), "Products page not displayed"

        search_input = driver.find_element(By.ID, "search_product")
        search_input.send_keys("jeans")
        search_button = driver.find_element(By.ID, "submit_search")
        search_button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Searched Products']"))
        )
        assert driver.find_element(By.XPATH,
                                   "//h2[text()='Searched Products']").is_displayed(), "Searched Products section not displayed"

        products = driver.find_elements(By.CSS_SELECTOR, ".features_items .col-sm-4")
        assert len(products) > 0, "No products found related to the search query"



