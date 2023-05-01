from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging as lg

# Currently set to 2 minutes
MAX_TIMEOUT = 120

def check_messages(driver):
    # -- from home page enter messages sidewindow --
    lg.info("Entering check messages function")
    messages_button = driver.find_element(
        By.XPATH, 
        "/html/body/div[2]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[6]/div[3]/div/div/div/div"
        )
    messages_button.click()

    # -- find messages container --
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


    # -- get messages container --
    lg.info("[check messages] Searching for individual messages container")
    individual_message_container = WebDriverWait(driver, timeout=MAX_TIMEOUT).until(
        lambda driver: driver.find_element(
        By.XPATH, 
        "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div"
        ))
    lg.info("[check messages] Found individual messages container")

    # -- Get name of person we are chatting with --
    chat_recipient = WebDriverWait(driver, timeout=MAX_TIMEOUT).until(
        lambda driver: driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/a")
    )
    print(f'Chat recipient: {chat_recipient.text}\n')


    lg.info("[check messages] Searching for individual message items")
    individual_message_messages = WebDriverWait(individual_message_container, timeout=MAX_TIMEOUT).until(
        lambda driver: driver.find_elements(
        By.XPATH, "./child::div"
        ))
    
    all_messages = []
    for msg in individual_message_messages:
        all_messages.append(msg.text)

    print("\n\n")
    for i, msg in enumerate(all_messages):
        print(f"Message {i}: {msg}")
    
    lg.info("[check messages] Found individual messages")
    
    lg.info("Exiting check messages function")