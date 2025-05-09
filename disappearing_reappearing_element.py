from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class ElementsDisappearingReappearing:

    def __init__(self):
        self.driver= webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/")

    def elements_disappearing_reappearing(self):
        self.driver.find_element(By.LINK_TEXT, "Disappearing Elements").click()
        element=None
        while not element:
            try:
                element = self.driver.find_element(By.XPATH,"//a[contains(text(),'Gallery')]").click()
                break
            except NoSuchElementException:
                self.driver.refresh()
        self.driver.close()

obj = ElementsDisappearingReappearing()
obj.elements_disappearing_reappearing()
