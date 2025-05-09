from  selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/hovers")

def hover_mouse():
    ele = driver.find_element(By.XPATH,"//div[@class='example']//div[1]//img[1]")
    action = ActionChains(driver,10)
    action.move_to_element(ele).perform()
    user_name = driver.find_element(By.XPATH,"//div[@class='example']//div[1]//div[1]//h5").text
    print(user_name)

hover_mouse()