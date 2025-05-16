import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.globalsqa.com/demoSite/practice/autocomplete/combobox.html")
first_text = "Python"

def wait_till_element_visible(locator):
    wait = WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable(locator))

def select_value_by_text(locator):
    select = Select(locator)
    select.select_by_visible_text(first_text)
def handle_auto_dropdown():
    button = (By.ID, "toggle")
    wait_till_element_visible(button)
    driver.find_element(*button).click()
    time.sleep(5)
    drop_down = driver.find_element(By.ID,"combobox")
    select_value_by_text(drop_down)
    driver.find_element(By.CSS_SELECTOR,".custom-combobox-input.ui-widget.ui-widget-content.ui-state-default.ui-corner-left.ui-autocomplete-input").send_keys("P")
    list_of_values = driver.find_elements(By.CSS_SELECTOR, "ul[id='ui-id-1'] li div")
    for x in list_of_values:
        if x.text == first_text:
            x.click()
            time.sleep(3)
handle_auto_dropdown()