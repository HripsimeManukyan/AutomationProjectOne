import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestContactUsForm:
    @pytest.fixture()
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationexercise.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        yield self.driver
        self.driver.quit()

    def test_contact_us(self, setup_teardown):
        driver = setup_teardown
        assert "Automation Exercise" in driver.title
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Contact").click()
        assert self.driver.find_element(By.XPATH, "//h2[normalize-space()='Get In Touch']").is_displayed()
        self.driver.find_element(By.NAME, "name").send_keys("Bill")
        self.driver.find_element(By.NAME, "email").send_keys("bill12@gmail.com")
        self.driver.find_element(By.NAME, "subject").send_keys("sending file")
        self.driver.find_element(By.NAME, "message").send_keys("buying some items")
        upload_element = self.driver.find_element(By.NAME, "upload_file")
        upload_element.send_keys("C:\\Users\\Hripsime\\Desktop\\Python Programming\\Selenium testing\\file (2).txt")
        self.driver.find_element(By.XPATH, "//input[@name='submit']").click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        assert self.driver.find_element(By.XPATH, "//div[@class='status alert alert-success']").is_displayed()
        home_button = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
        home_button.click()
        assert "Automation Exercise" in driver.title