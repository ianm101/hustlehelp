from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import configparser
import time
import logging as lg

# Currently set to 2 minutes
MAX_TIMEOUT = 120

config = configparser.ConfigParser()
config.read('config.ini')

PINTEREST_EMAIL = config.get('pinterest', 'PINTEREST_EMAIL')
PINTEREST_PASSWORD = config.get('pinterest', 'PINTEREST_PASSWORD')


def pinterest_login(driver):
    lg.info("Entering pinterest_login function")
    # Navigate to the Pinterest login page
    driver.get("https://www.pinterest.com/login/")

    # Wait for the login form to load
    email_input_elem = WebDriverWait(driver, timeout=MAX_TIMEOUT).until(
        lambda driver: driver.find_element(
            By.ID, "email"
        ))
    email_input_elem.send_keys(PINTEREST_EMAIL)

    # Tab to password
    password_input_element = WebDriverWait(driver, timeout=MAX_TIMEOUT).until(
        lambda driver : driver.find_element(
            By.ID, "password"
        ))
    password_input_element.send_keys(PINTEREST_PASSWORD)

    login_element = WebDriverWait(driver, timeout=MAX_TIMEOUT).until(
        lambda driver: driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[3]/div/div/div[3]/form/div[7]/button"
        ))

    login_element.click()

    # Wait for the dashboard to load
    time.sleep(10)

    # Verify that login was successful
    if "Pinterest" in driver.title:
        print("Login successful")
        lg.info("Login successful")
    else:
        lg.error("Login failed")
        print("Login failed")

    lg.info("Exiting pinterest_login function")
    print("exiting pinterest login function")
