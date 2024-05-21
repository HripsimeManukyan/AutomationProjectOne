import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup_method():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login_with_incorrect_credentials(setup_method):
    assert "Automation Exercise" in setup_method.title
    driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
    assert driver.find_element(By.XPATH, "//h2[normalize-space()='Login to your account']").is_displayed()
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("jane19@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("12345600")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    assert driver.find_element(By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']").is_displayed()
