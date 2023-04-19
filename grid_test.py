from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



capabilities = DesiredCapabilities.CHROME.copy()
capabilities["platform"] = "LINUX"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Remote(
    command_executor=grid_url,
    options = chrome_options
)

print("before get")
driver.get("https://www.google.com")
print(driver.title)

driver.quit()