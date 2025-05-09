import time
import re

from pytest_selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class ChallengingDom:
    def __init__(self):
        self.driver= webdriver.Firefox()
    def get_url(self):
        self.driver.get('https://the-internet.herokuapp.com/')
    def clicking_on_buttons(self):
        self.driver.find_element(By.LINK_TEXT,"Challenging DOM").click()
        button1=(By.XPATH,"//div[@class='large-2 columns']/a[@class='button']")
        button2=(By.XPATH,"//div[@class='large-2 columns']/a[@class='button alert']")
        button3=(By.XPATH,"//div[@class='large-2 columns']/a[@class='button success']")

        self.driver.find_element(*button1).click()
        self.driver.find_element(*button2).click()
        self.driver.find_element(*button3).click()
    def edit_2nd_row_of_table(self):
        self.driver.find_element(By.XPATH,"//div[@class='large-10 columns']/table/tbody/tr[2]/td[7]/a[1]").click()
    def delete_6th_row_of_table(self):
        self.driver.find_element(By.XPATH,"//div[@class='large-10 columns']/table/tbody/tr[6]/td[7]/a[2]").click()

    def play_with_canvas(self):
        script_block=self.driver.find_element(By.XPATH,"//div[@id='content']/script").get_attribute('innerHTML')
        old_answer = re.search(r"Answer:\s(\d+)", script_block).group(1)
        self.driver.refresh()
        print(old_answer)
        # grab the canvas generation script block, which contains the Answer buried in javascript
        script_block = self.driver.find_element(By.XPATH,'//div[@id="content"]/script').get_attribute('innerHTML')
        # pick out the number after 'Answer' using regex
        new_answer = re.search(r"Answer:\s(\d+)", script_block).group(1)
        print(new_answer)

    def actual_play_with_canva(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/challenging_dom")
        # if "--headless" not in options:
        driver.maximize_window()
        while True:
            txt = driver.find_element(By.XPATH, "//script[contains(text(), 'strokeText')]").get_attribute("textContent")
            value = re.search(r"Answer:\s(\d+)", txt).group(1)
            print(value)
            driver.refresh()
            txt2 = driver.find_element(By.XPATH, "//script[contains(text(), 'strokeText')]").get_attribute(
                "textContent")
            value2 = re.search(r"Answer:\s(\d+)", txt2).group(1)
            if value != value2:
                assert True
                print(f"Answer value is changed by system from {value} to {value2}.")
                break
    def close(self):
        self.driver.close()
obj = ChallengingDom()
obj.get_url()
obj.clicking_on_buttons()
obj.play_with_canvas()
obj.close()