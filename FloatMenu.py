import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/floating_menu")

def floating_menu():
    driver.implicitly_wait(5)
    ele=driver.find_element(By.ID,"menu")
    driver.execute_script("window.scroll(0,500)")
    if ele.value_of_css_property("position").__eq__("fixed"):
        print("Nav bar is floating.")
    else:
        print("Nav bar is not floating.")
floating_menu()