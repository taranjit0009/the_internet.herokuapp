import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By



class BrokenImage:
    def __init__(self):
        self.driver= webdriver.Firefox()

    def get_url(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def find_broken_images(self):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Broken Images')]").click()
        images =self.driver.find_elements(By.TAG_NAME,'img')
        broken_images = []
        for img in images:
            src = img.get_attribute('src')
            if requests.get(src).status_code==404:
                broken_images.append(src)
        print("-----------------------------------------------------------------------------------")
        for broken_image in broken_images:
            print(broken_image)
        print("-----------------------------------------------------------------------------------")
        assert not broken_images,f"There are {len(broken_images)} broken images:{broken_images}"

    def quit(self):
        self.driver.close()

obj = BrokenImage()
obj.get_url()
obj.find_broken_images()
obj.quit()