from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

PINTEREST_EMAIL = config.get('pinterest', 'PINTEREST_EMAIL')
PINTEREST_PASSWORD = config.get('pinterest', 'PINTEREST_PASSWORD')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Pinterest login page
driver.get("https://www.pinterest.com/login/")

# Wait for the login form to load
time.sleep(5)

email_input_elem = driver.find_element(By.ID, "email")
email_input_elem.send_keys(PINTEREST_EMAIL)

# Tab to password
password_input_element = driver.find_element(By.ID, "password")
password_input_element.send_keys(PINTEREST_PASSWORD)
time.sleep(0.5)

login_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[3]/div/div/div[3]/form/div[7]/button")

login_element.click()

# Wait for the dashboard to load
time.sleep(10)

# Verify that login was successful
if "Pinterest" in driver.title:
    print("Login successful")
else:
    print("Login failed")

# Close the browser window
driver.close()

