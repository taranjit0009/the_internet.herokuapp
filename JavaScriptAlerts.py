from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

def js_alerts():
    driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
    alt_text=driver.switch_to.alert.text
    print(alt_text)
    driver.switch_to.alert.accept()

    driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
    conf_txt = driver.switch_to.alert.text
    print(conf_txt)
    driver.switch_to.alert.dismiss()

    driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
    driver.switch_to.alert.send_keys("Hello Pappu!")
    driver.switch_to.alert.accept()
js_alerts()