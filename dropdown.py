import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DropDown:
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://the-internet.herokuapp.com")
    def drop_down(self):
        self.driver.find_element(By.LINK_TEXT,"Dropdown").click()
        element = self.driver.find_element(By.ID,"dropdown")
        select = Select(element)
        select.select_by_visible_text('Option 2')
        self.driver.close()


obj = DropDown()
obj.drop_down()