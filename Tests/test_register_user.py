import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    name_field = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    email_field = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")

    name_field.send_keys("Test Name")
    email_field.send_keys("work@gmail.com")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Signup']")
    submit_button.click()

    account_name_field = driver.find_element(By.NAME, 'name')
    account_email_field = driver.find_element(By.ID, "email")

    driver.execute_script("arguments[0].removeAttribute('readonly')", account_name_field)
    driver.execute_script("arguments[0].removeAttribute('readonly')", account_email_field)
    driver.execute_script("arguments[0].value = ''", account_name_field)
    driver.execute_script("arguments[0].value = ''", account_email_field)
    driver.execute_script("arguments[0].value = 'Jane'", account_name_field)
    driver.execute_script("arguments[0].value = 'workmail@example.com'", account_email_field)

    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//select[@id='days']").send_keys("1")
    driver.find_element(By.XPATH, "//select[@id='months']").send_keys("January")
    driver.find_element(By.XPATH, "//select[@id='years']").send_keys("1994")
    checkbox_element = driver.find_element(By.ID, "newsletter")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox_element)
    newsletter_checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "newsletter")))
    newsletter_checkbox.click()
    driver.find_element(By.XPATH, "//input[@id='optin']").click()
    driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Jane")
    driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Brown")
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


