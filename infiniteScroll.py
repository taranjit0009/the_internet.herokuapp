from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/infinite_scroll")

def infinite_scroll():
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

infinite_scroll()