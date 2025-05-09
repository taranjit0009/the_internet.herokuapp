import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/download")

def download_files():
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[href='download/API Testing using AI tool Testim.docx']")))
    driver.find_element(By.CSS_SELECTOR,"a[href='download/API Testing using AI tool Testim.docx']").click()
    time.sleep(5)
    base_path ="C:\\Users\\Taranjit Singh\\Downloads"
    for x in os.listdir(base_path):
        if "API Testing using AI tool Testim" in x and x.endswith(".docx"):
            print("file has been downloaded.")
            break
download_files()