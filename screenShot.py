from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.reddit.com/r/learnpython/comments/115olu9/pandas_how_do_i_combine_values_from_rows_with_the/"

screenshotDir = "screenshotss"
screenWidth = 400
screenHeight = 800

def setupDriver(url: str):
    options = webdriver.FirefoxOptions()
    options.headless = False
    options.mobile_options = False
    print(options)
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 10)
    driver.set_window_size(width=screenWidth, height= screenHeight)
    driver.get(url)
    return driver, wait

def takeTitleScreenshot(driver, wait):
    driver.get(url)
    handle = By.CLASS_NAME
    name = "Post"
    element = wait.until(EC.presence_of_element_located(handle, name))
    ssName = f"{screenshotDir}/{handle}.png"
    file = open(screen)

setupDriver(url)