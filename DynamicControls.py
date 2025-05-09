import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
#options.add_argument("--headless=new")
options.page_load_strategy="normal"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
def wait(locator):
    wait_ele = WebDriverWait(driver,10,2)
    wait_ele.until(EC.visibility_of_element_located(locator))

def dynamic_controls():

    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]").click()
    driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").is_selected()
    driver.find_element(By.CSS_SELECTOR,"button[onclick='swapCheckbox()']").click()
    wait((By.CSS_SELECTOR, "p[id='message']"))
    actual_text=driver.find_element(By.CSS_SELECTOR, "p[id='message']").text
    time.sleep(5)
    assert actual_text == "It's gone!"
    driver.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']").click()
    wait((By.CSS_SELECTOR, "p[id='message']"))
    actual_text1 = driver.find_element(By.CSS_SELECTOR, "p[id='message']").text
    time.sleep(5)
    assert actual_text1 == "It's back!"

dynamic_controls()