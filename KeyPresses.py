from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/key_presses")

def handle_keys():
    ele=driver.find_element(By.ID,"target")

    action = ActionChains(driver)
    action.click(ele).send_keys(Keys.TAB).perform()
    result = driver.find_element(By.ID, "result").text
    if "TAB" in result:
        print("Working fine.")

handle_keys()