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


def test_register_user(setup_method):
    assert "Automation Exercise" in setup_method.title
    driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
    assert driver.find_element(By.XPATH, "//h2[normalize-space()='New User Signup!']").is_displayed()
    driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("User")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("tim1994@gmail.com")
    driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
    assert driver.find_element(By.XPATH, "//b[contains(text(),'Enter Account Information')]").is_displayed()
    driver.find_element(By.XPATH, "//input[@id='id_gender2']").click()
    # input_name = driver.find_element(By.ID, "name")
    # input_name.clear()
    # input_name.send_keys("User")
    # input_email = driver.find_element(By.ID, "email")
    # input_email.clear()
    # input_email.send_keys("privateuser@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//select[@id='days']").send_keys("1")
    driver.find_element(By.XPATH, "//select[@id='months']").send_keys("January")
    driver.find_element(By.XPATH, "//select[@id='years']").send_keys("1994")
    checkbox_element = driver.find_element(By.ID, "newsletter")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox_element)
    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.XPATH, "//input[@id='optin']").click()
    driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("User")
    driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Pit")
    driver.find_element(By.XPATH, "//input[@id='company']").send_keys("ABC")
    driver.find_element(By.XPATH, "//input[@id='address1']").send_keys("123 High Street")
    driver.find_element(By.XPATH, "//input[@id='address2']").send_keys("Apt 101")
    driver.find_element(By.XPATH, "//select[@id='country']").send_keys("United States")
    driver.find_element(By.XPATH, "//input[@id='state']").send_keys("New York")
    driver.find_element(By.XPATH, "//input[@id='city']").send_keys("LA")
    driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("1001")
    driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("1234567890")
    driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()
    assert driver.find_element(By.XPATH, "//b[normalize-space()='Account Created!']").is_displayed()
    driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
    assert driver.find_element(By.XPATH, "//li[10]//a[1]").is_displayed()
    driver.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()
    assert driver.find_element(By.XPATH, "//b[contains(text(),'Account Deleted!')]").is_displayed()
    driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
