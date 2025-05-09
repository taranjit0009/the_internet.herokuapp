import time
import pyautogui #it is used for mouse cursor movement.Avoid PyAutoGUI for Headless Execution
from pytest_selenium import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/exit_intent")

def action():
    actions = ActionChains(driver)
    return actions

def exit_intent():
    time.sleep(5)
    action().move_by_offset(9999, 9999)
    action().perform()
    pyautogui.moveTo(x=100,y=100)
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Close']")))
    driver.find_element(By.XPATH,"//p[normalize-space()='Close']").click()
    driver.quit()

exit_intent()