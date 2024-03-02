from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


screenshotDir = "screenshots"
screenWidth = 400
screenHeight = 800

def takeSS(url, post_id, comment_id, option: int):
    try:
        driver, wait = setupDriver(url)
        if option==1:
            takeTitleScreenshot(driver, wait, post_id)
        elif option==2:
            takeCommentScreenshot(driver, wait, comment_id)
        driver.close()
    except:
        print('Failed for ss for post: ' + post_id + ' comment: ' + comment_id)
def setupDriver(url: str):
    options = webdriver.FirefoxOptions()
    options.headless = False
    options.mobile_options = False
    options.set_preference("dom.popup_maximum", 0)
    print(options)
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 15)
    driver.set_window_size(width=screenWidth, height= screenHeight)
    driver.get(url)
    return driver, wait

def takeTitleScreenshot(driver, wait, id):
    handle = By.ID
    name = f"t3_{id}"
    element = wait.until(EC.presence_of_element_located((handle, name)))
    driver.execute_script("window.focus();")
    ssName = f"{screenshotDir}/{id}_post.png"
    file = open(ssName, "wb")
    file.write(element.screenshot_as_png)
    file.close()

def takeCommentScreenshot(driver, wait, id):
    handle = By.CSS_SELECTOR
    name = f'[thingid="t1_{id}"]'
    element = wait.until(EC.presence_of_element_located((handle, name)))
    driver.execute_script("window.focus();")
    ssName = f'{screenshotDir}/{id}_comment.png'
    file = open(ssName, "wb")
    file.write(element.screenshot_as_png)
    file.close()

def cancelLoginPopup(driver, wait):
    try:
        popup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[id="animated-container"]')))
        #WebDriverWait(popup, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='No thanks']"))).click()
        print(popup)
        
        #button = popup.find_element(By.TAG_NAME, "button")

        #button.click()
    except:
        print("Login Popup does not exist")
