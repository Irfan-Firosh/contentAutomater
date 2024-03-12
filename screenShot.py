from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


screenshotDir = "screenshots"
screenWidth = 400
screenHeight = 800

def takeSS(url, post_id, comment_id, option: int):
    try:
        driver, wait = setupDriver(url)
        cancelLoginPopup(driver)
        time.sleep(2)
        if option==1:
            takeTitleScreenshot(driver, wait, post_id)
        elif option==2:
            takeCommentScreenshot(driver, wait, comment_id)
        driver.close()
    except:
        driver.close()
        print('Failed for ss for post: ' + post_id + ' comment: ' + comment_id)
def setupDriver(url: str):
    try:
        options = webdriver.FirefoxOptions()
        options.headless = False
        options.mobile_options = False
        driver = webdriver.Firefox(options=options)
        wait = WebDriverWait(driver, 10)
        driver.set_window_size(width=screenWidth, height= screenHeight)
        driver.get(url)
        return driver, wait
    except:
        print("Error setting up driver")

def takeTitleScreenshot(driver, wait, id):
    try:
        handle = By.ID
        name = f"t3_{id}"
        element = wait.until(EC.presence_of_element_located((handle, name)))
        driver.execute_script("window.focus();")
        ssName = f"{screenshotDir}/{id}_post.png"
        file = open(ssName, "wb")
        file.write(element.screenshot_as_png)
        file.close()
    except:
        print("Screenshot error post: " + id)

def takeCommentScreenshot(driver, wait, id,):
    try:
        handle = By.ID
        name = f't1_{id}'
        element = wait.until(EC.presence_of_element_located((handle, name)))
    except TimeoutException:
        handle = By.CSS_SELECTOR
        name = f'[thingid="t1_{id}"]'
        element = wait.until(EC.presence_of_element_located((handle, name)))
    driver.execute_script("window.focus();")
    ssName = f'{screenshotDir}/{id}_comment.png'
    file = open(ssName, "wb")
    file.write(element.screenshot_as_png)
    file.close()

def cancelLoginPopup(driver):
    try:
        iframes = driver.find_elements(By.TAG_NAME,'iframe')
        popup = None
        
        # Gets Last Frame
        for iframe in reversed(iframes):
            src = iframe.get_attribute('src')
            if src:
                popup = iframe
                break
        driver.switch_to.frame(popup)
        driver.find_element("xpath", '//div[@role="button"]').click()
        driver.switch_to.default_content()
    except NoSuchElementException:
        print("No Login Found")
    except:
        print("Error with cancel login")
