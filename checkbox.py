from selenium import webdriver
from selenium.webdriver.common.by import By
class CheckBox:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_url(self):
        self.driver.get("https://the-internet.herokuapp.com/")
    def check_the_buttons(self):
        self.driver.find_element(By.LINK_TEXT,"Checkboxes").click()
        check_button = (By.XPATH,"//form[@id='checkboxes']/input[1]")
        assert self.driver.find_element(*check_button).is_displayed(),f'check button is not displayed.'
        print('check button is displayed.')
        self.driver.find_element(*check_button).click()
        assert self.driver.find_element(*check_button).is_selected(),f'check button is not selected.'

    def uncheck_the_button(self):
        uncheck_button = self.driver.find_element(By.XPATH,"//form[@id='checkboxes']/input[2]")
        uncheck_button.click()
        assert not uncheck_button.is_selected(),f'uncheck button is enabled.'
        print('check button is unchecked.')

    def close(self):
        self.driver.close()



obj = CheckBox()
obj.get_url()
obj.check_the_buttons()
obj.uncheck_the_button()
obj.close()
