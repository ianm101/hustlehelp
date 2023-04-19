from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def check_messages(driver):
    messages_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[6]/div[3]/div/div/div/div")
    messages_button.click()

    time.sleep(3)

    msgs_container = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/ul")
    msgs_elements = msgs_container.find_elements(By.XPATH, "./child::*")

    # Click first message (testing)
    msgs_elements[0].click()
    
    # Should be able to identify all messages (html elements) via this class
    individual_message_messages = driver.find_elements(By.CLASS_NAME, "Jea zI7 iyn Hsu")
    print(f'Individual Messages: {len(individual_message_messages)}')
    
    print("done")