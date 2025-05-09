from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/inputs")

def inputs():
    ele = driver.find_element(By.CSS_SELECTOR,"input[type='number']")
    ele.send_keys("sdfasgt")
    if ele.get_attribute("value")=="sdfasgt":
        print(False)
    else:
        print(True)
    ele.send_keys("123")
    for _ in range(5):
        ele.send_keys(Keys.ARROW_UP)

    for _ in range(10):
        ele.send_keys(Keys.ARROW_DOWN)

inputs()
