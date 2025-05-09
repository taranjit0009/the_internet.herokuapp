import time

from openpyxl.styles.builtins import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContextMenu:
    def __init__(self):
        self.drive = webdriver.Firefox()
        self.drive.get("https://the-internet.herokuapp.com/")
    def page_title_and_header(self):
        self.drive.find_element(By.LINK_TEXT,'Context Menu').click()
        title_of_page=self.drive.title
        assert title_of_page == "The Internet",f"title of the page is {title_of_page} and it is not matched with expected."
        print(f"{title_of_page} is matched with expected title.")

        assert self.drive.find_element(By.XPATH,"//div[@id='content']//div[@class='example']/h3").text=="Context Menu"

    def context_menu(self):
        element = self.drive.find_element(By.CSS_SELECTOR,"#hot-spot")
        action = ActionChains(self.drive)
        action.context_click(element).perform()
        alert_ = Alert(self.drive)
        alert_.accept()
        time.sleep(3)
        action.click(element)
        self.drive.refresh()







obj = ContextMenu()
obj.page_title_and_header()
obj.context_menu()
