import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

def login():
    username = "tomsmith"
    password = "SuperSecretPassword!"

    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,".fa.fa-2x.fa-sign-in").click()
    title_after_login = driver.title
    if title_after_login=="The Internet":
        print(True,"loggedin")
    success_message = driver.find_element(By.ID,"flash").text
    if re.search("You logged into a secure area!",success_message):
        print(True,f"{success_message}")
    driver.find_element(By.XPATH,"//a[@class='button secondary radius']").click()

login()