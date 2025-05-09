from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/jqueryui/menu")
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

def click_download_option(option_text):
    enable_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Enabled']")))
    actions.move_to_element(enable_menu).perform()

    downloads = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Downloads']")))
    actions.move_to_element(downloads).perform()

    option = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[normalize-space()='{option_text}']")))
    actions.move_to_element(option).click().perform()

    driver.refresh()

click_download_option("PDF")
click_download_option("CSV")
click_download_option("Excel")
