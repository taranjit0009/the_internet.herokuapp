import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument("--headless=new")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/jqueryui/menu")
"""
Since the DOM has changed e.g. through the update action, you are receiving a StaleElementReference Error

WebElement button = driver.findElement(By.xpath("xpath"));
button.click();

//here you do something like update or save 

//then you define the button element again before you use it
WebElement button1 = driver.findElement(By.xpath("xpath"));
//that new element will point to the same element in the new DOM
button1.click();
"""
def jquary_menus():
    action = ActionChains(driver,10)
    ele = driver.find_element(By.XPATH,"//a[normalize-space()='Disabled']")
    enable_menu_ = driver.find_element(By.XPATH, "//a[normalize-space()='Enabled']")
    back_to_jquary = driver.find_element(By.CSS_SELECTOR,"a[href='/jqueryui']")

    if enable_menu_.is_enabled():
        print("Element is enabled.")
    else:
        print("Element is disabled.")

    # click on pdf
    enable_menu = driver.find_element(By.XPATH, "//a[normalize-space()='Enabled']")
    downloads = driver.find_element(By.XPATH,"//a[normalize-space()='Downloads']")
    download_pdf = driver.find_element(By.XPATH, "//a[normalize-space()='PDF']")
    action.move_to_element(enable_menu).pause(3).move_to_element(downloads).pause(2).click(download_pdf).perform()
    driver.refresh()
    # click on CSV
    enable_menu1 = driver.find_element(By.XPATH, "//a[normalize-space()='Enabled']")
    downloads1 = driver.find_element(By.XPATH, "//a[normalize-space()='Downloads']")
    download_csv = driver.find_element(By.XPATH, "//a[normalize-space()='CSV']")
    action.move_to_element(enable_menu1).pause(3).move_to_element(downloads1).pause(2).click(download_csv).perform()
    driver.refresh()

    #click on Excel
    enable_menu2 = driver.find_element(By.XPATH, "//a[normalize-space()='Enabled']")
    downloads2 = driver.find_element(By.XPATH, "//a[normalize-space()='Downloads']")
    download_excel = driver.find_element(By.XPATH, "//a[normalize-space()='Excel']")
    action.pause(3).move_to_element(enable_menu2).pause(1).move_to_element(downloads2).pause(3).click(download_excel).perform()

jquary_menus()