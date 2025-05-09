from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

def handle_windows():
    original_window=driver.current_window_handle
    driver.find_element(By.CSS_SELECTOR,"a[href='/windows/new']").click()
    driver.switch_to.window(driver.window_handles[1])
    text_next_window = driver.find_element(By.CSS_SELECTOR,"div[class='example'] h3").text
    print(text_next_window)
    driver.switch_to.window(original_window)
    current_window_text = driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text
    print(current_window_text)
handle_windows()