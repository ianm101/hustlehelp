from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

grid_url = "http://localhost:4444/wd/hub"

capabilities = DesiredCapabilities.CHROME.copy()
capabilities["platform"] = "MAC"

driver = webdriver.Remote(
    command_executor=grid_url,
    options = webdriver.ChromeOptions()
)

print("before get")
driver.get("https://www.google.com")
print(driver.title)

driver.quit()