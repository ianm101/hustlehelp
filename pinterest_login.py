from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

# Click on the "Continue with Google" button
# google_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]")
google_button = driver.find_element(By.XPATH, "/html/body/div/div")
google_button.click()

# Switch to the Google login window
driver.switch_to.window(driver.window_handles[-1])

# Find the email field and enter your Google email
email_field = driver.find_element(By.NAME, "identifier")
email_field.send_keys(PINTEREST_EMAIL)
email_field.send_keys(Keys.RETURN)

# Wait for the password field to load
time.sleep(5)

# Find the password field and enter your Google password
password_field = driver.find_element(By.NAME, "Passwd")
password_field.send_keys(PINTEREST_PASSWORD)
password_field.send_keys(Keys.RETURN)

# Switch back to the Pinterest window
driver.switch_to.window(driver.window_handles[0])

# Wait for the dashboard to load
time.sleep(10)

# Verify that login was successful
if "Pinterest" in driver.title:
    print("Login successful")
else:
    print("Login failed")

# Close the browser window
driver.close()

