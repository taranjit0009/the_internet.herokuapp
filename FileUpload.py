import time
from math import trunc

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/upload")

def upload_file():
    base_path = os.path.dirname(__file__)
    file_path = "./file/"
    file_name = "TestNG Interview Questions.pdf"
    actual_file = os.path.join(base_path,file_path+file_name)
    print(actual_file)

    # driver.find_element(By.ID,"file-upload").send_keys(actual_file)
    # driver.find_element(By.ID,"file-submit").click()
    # time.sleep(10)
    # driver.back()
    time.sleep(5)
    action = ActionChains(driver,10)
    ele = driver.find_element(By.ID,"drag-drop-upload")
    action.move_to_element(ele).click(ele).send_keys(actual_file).perform()
    time.sleep(5)
    #driver.find_element(By.ID,"drag-drop-upload").send_keys(actual_file)

#upload_file()


def even_generator():
    n=0
    while True:
        n+=1
        if n % 2 == 0:
            yield n

even_num  = even_generator()

for _ in range(10):
    
    print(next(even_num),end=" ")
