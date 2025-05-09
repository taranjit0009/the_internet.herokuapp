from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.page_load_strategy='normal'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.maximize_window()

def wait(locator):
    wait_ele = WebDriverWait(driver,10,2)
    wait_ele.until(EC.visibility_of_element_located(locator))

def entry_ad():
    driver.get("https://the-internet.herokuapp.com/entry_ad")
    wait((By.CSS_SELECTOR,"div[class ='modal-footer'] p"))
    driver.find_element(By.CSS_SELECTOR,"div[class ='modal-footer'] p").click()
    driver.find_element(By.ID,"restart-ad").click()
    wait((By.CSS_SELECTOR, "div[class ='modal-footer'] p"))
    driver.find_element(By.CSS_SELECTOR, "div[class ='modal-footer'] p").click()

entry_ad()