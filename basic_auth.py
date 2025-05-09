import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasicAuth:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_url(self):
        self.driver.get("https://the-internet.herokuapp.com/")
    def basic_auth(self):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Basic Auth')]").click()
        # add credentials username = admin, password = admin
        #Syntax to embed creds in the URL > "https://" + USERNAME + ":" + PASSWORD + "@the-internet.herokuapp.com/"

        self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        value = self.driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations!')]").text
        assert "Congratulations!" in value,f"There is no success message getting."
        print(value)


obj = BasicAuth()

obj.get_url()
obj.basic_auth()