import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSubscription:
    @pytest.fixture()
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationexercise.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        yield self.driver
        self.driver.quit()

    def test_home_page_subscription(self, setup_teardown):
        driver = setup_teardown
        assert "Automation Exercise" in driver.title
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert driver.find_element(By.XPATH, "//h2[normalize-space()='Subscription']").is_displayed()
        driver.find_element(By.XPATH, "//input[@id='susbscribe_email']").send_keys("jane1994@gmail.com")
        driver.find_element(By.XPATH, "//i[@class='fa fa-arrow-circle-o-right']").click()
        assert driver.find_element(By.XPATH, "//div[@class='alert-success alert']").is_displayed()