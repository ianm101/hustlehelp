from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import logging as lg

lg.basicConfig(filename="lastrun.log", encoding="utf-8", level=lg.DEBUG)

from pinterest_login import pinterest_login
from check_pinterest_messages import check_messages


grid_url = "http://localhost:4444/wd/hub"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Remote(
    command_executor=grid_url,
    options = chrome_options
)

# pinterest login function
pinterest_login(driver)

# check messages 
check_messages(driver)

print("done")