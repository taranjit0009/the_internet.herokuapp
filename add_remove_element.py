import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class AddDeleteElement:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def launch_url(self):
       self.driver.get('https://the-internet.herokuapp.com/')

    def wait(self,locator,timeout):
        WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))



    def add_remove_element(self,add_count,delete_count):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Add/Remove Elements')]").click()
        title = self.driver.find_element(By.XPATH,"//h3[contains(text(),'Add/Remove Elements')]").text
        assert title == "Add/Remove Elements",f"Title is not matched."
        print(f"title = {title} is matched")
        add_button=self.driver.find_element(By.XPATH,"//button[contains(text(),'Add Element')]")

        for _ in range(add_count):
            add_button.click()
        delete_button=(By.XPATH,"//div[@id='elements']/button")
        self.wait(delete_button, 15)
        buttons = self.driver.find_elements(*delete_button)
        if delete_count < len(buttons):
            buttons[delete_count].click()
        else:
            print(f"Cannot delete button at index {delete_count} as there are only {len(buttons)} buttons")

    def delete_all_buttons(self):
        delete_button = (By.XPATH, "//div[@id='elements']/button")
        self.wait(delete_button, 15)
        buttons = self.driver.find_elements(*delete_button)
        for x in buttons:
            x.click()
objAddDeleteElement = AddDeleteElement()

objAddDeleteElement.launch_url()
objAddDeleteElement.add_remove_element(4,1)

objAddDeleteElement.delete_all_buttons()