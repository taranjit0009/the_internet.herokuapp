import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/horizontal_slider")

def horizontal_slider():
    slider=driver.find_element(By.CSS_SELECTOR,"input[value='0']")
    #first way
    action = ActionChains(driver,10)
    action.drag_and_drop_by_offset(slider,0,3).perform()
    time.sleep(5)
    #2nd way
    for _ in range(1):
        slider.send_keys(Keys.ARROW_RIGHT)
    time.sleep(5)
    value_vol = driver.find_element(By.XPATH,"//span[@id='range']").text
    print(value_vol)
horizontal_slider()