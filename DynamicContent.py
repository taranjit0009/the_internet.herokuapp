import time

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class DynamicContent:    
    def __init__(self):
        self.driver= webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/")

    def dynamic_content(self):
        self.driver.find_element(By.LINK_TEXT,'Dynamic Content').click()
        click_button=self.driver.find_element(By.XPATH,'//a[contains(text(),"click here")]')
        img = self.driver.find_element(By.XPATH,"//div[@id='content']//div[3]/div[1]/img")
        first_text = self.driver.find_element(By.XPATH,"//div[@id='content']//div[3]/div[2]").text
        src_img=img.get_attribute('src')
        print(src_img)
        click_button.click()
        time.sleep(10)
        # Retry mechanism to handle stale element
        max_retries = 5
        retries = 0
        while retries < max_retries:
            try:
                img = self.driver.find_element(By.XPATH, "//div[@id='content']//div[3]/div[1]/img")
                src_img2 = img.get_attribute('src')
                print(src_img2)
                break
            except StaleElementReferenceException:
                retries += 1
                time.sleep(1)
        # Wait before retrying if retries == max_retries: print("Failed to retrieve new image src after multiple attempts.")

        # while src_img!=src_img2:
        #     try:
        #         click_button.click()
        #     except NoSuchElementException:
        #         print('again try')

        #print('Images are changing dynamically.')
        second_text = self.driver.find_element(By.XPATH,"//div[@id='content']//div[3]/div[2]").text
        time.sleep(5)
        assert second_text != first_text,f'second text is same as first text.'
        print('Text are different.')
obj = DynamicContent()
obj.dynamic_content()