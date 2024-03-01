from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("localhost:8080/s/pacs")
    yield driver
    driver.quit()

def test_login(driver):
    username_field = driver.find_element_by_name("Autorisation")
    username_field.send_keys("admin")

    password_field = driver.find_element_by_name("password")
    password_field.send_keys("12345")

    login_button = driver.find_element_by_name("login")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.title_is("Logged in"))