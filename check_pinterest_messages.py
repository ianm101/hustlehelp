from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging as lg

# Currently set to 2 minutes
MAX_TIMEOUT = 120

def check_messages(driver):
    lg.info("Entering check messages function")
    messages_button = driver.find_element(
        By.XPATH, 
        "/html/body/div[2]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[6]/div[3]/div/div/div/div"
        )
    messages_button.click()
    lg.info("[check_messages] Searching for messages container")
    msgs_container = WebDriverWait(driver, timeout=MAX_TIMEOUT).until(
        lambda driver: driver.find_element(
        By.XPATH, 
        "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/ul"
        ))
    lg.info("[check messages] Found messages container")
    msgs_elements = msgs_container.find_elements(By.XPATH, "./child::*")

    # Click first message (testing)
    msgs_elements[0].click()


    # get messages container
    lg.info("[check messages] Searching for individual messages container")
    individual_message_container = WebDriverWait(driver, timeout=MAX_TIMEOUT).until(
        lambda driver: driver.find_element(
        By.XPATH, 
        "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div"
        ))
    lg.info("[check messages] Found individual messages container")

    # Should be able to identify all messages (html elements) via this class
    lg.info("[check messages] Searching for individual message items")
    individual_message_messages = WebDriverWait(individual_message_container, timeout=MAX_TIMEOUT).until(
        lambda driver: driver.find_elements(
        By.TAG_NAME,"span"
        ))
    lg.info("[check messages] Found individual messages")

    for individ_msg in individual_message_messages:
        print(f'Individual Message Text: {individ_msg.text}')
    
    lg.info("Exiting check messages function")