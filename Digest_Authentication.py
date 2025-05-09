from selenium import webdriver
from selenium.webdriver.common.by import By

class DigestAuthentication:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/")

    def digest_auth(self):
        self.driver.find_element(By.LINK_TEXT,"Digest Authentication").click()
        self.driver.get('https://admin:admin@the-internet.herokuapp.com/digest_auth')
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == "Digest Auth"
        assert "Congratulations" in self.driver.find_element(By.XPATH,"//div[@class='example']/p").text

obj = DigestAuthentication()
obj.digest_auth()