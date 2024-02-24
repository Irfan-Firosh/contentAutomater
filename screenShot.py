from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.reddit.com/r/AskReddit/comments/1az32dq/what_did_everyone_have_25_years_ago_1999_that/"

screenshotDir = "screenshots"
screenWidth = 400
screenHeight = 800

def setupDriver(url: str):
    options = webdriver.FirefoxOptions()
    options.headless = False
    options.mobile_options = False
    print(options)
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 100)
    driver.set_window_size(width=screenWidth, height= screenHeight)
    driver.get(url)
    return driver, wait

def takeTitleScreenshot(filePrefix, driver, wait, id):
    driver.get(url)
    handle = By.ID
    name = f"t3_{id}"
    element = wait.until(EC.presence_of_element_located((handle, name)))
    driver.execute_script("window.focus();")
    ssName = f"{screenshotDir}/{handle}_{filePrefix}.png"
    file = open(ssName, "wb")
    file.write(element.screenshot_as_png)
    file.close()
    driver.quit()

driver, wait = setupDriver(url)
takeTitleScreenshot("test", driver, wait, "1az32dq")