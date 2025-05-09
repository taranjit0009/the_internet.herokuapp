import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait



class DragAndDrop:
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/")
    def wait_element(self):
        pass
    def drog_n_drop(self):
        self.driver.find_element(By.LINK_TEXT,"Drag and Drop").click()

        actions= ActionChains(self.driver)
        source= self.driver.find_element(By.ID,"column-a")
        target=self.driver.find_element(By.ID,"column-b")
        actions.drag_and_drop(source,target).perform()
        time.sleep(5)
        self.driver.close()

obj = DragAndDrop()
obj.drog_n_drop()