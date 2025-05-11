from pyautogui import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/tables")

def waiting(locator):
    wait = WebDriverWait(driver,10)
    wait.until(EC.visibility_of_element_located(locator))

def table_one():
    name = "Smith"

    #Child to parent traverse
    get_name_smith = driver.find_element(By.XPATH,"//a[text()='edit']/ancestor::table[@id='table1']//tr//td[contains(.,'Smith')]").text
    print(get_name_smith)
    """
    #child to parent and Parent to child traverse combination, 
    *It is not mandatory but I have written only for practice purpose
    """
    edit_record = driver.find_element(By.XPATH,f"//table[@id='table1']//tbody//tr/td[contains(.,'{name}')]/parent::tr/td/a[1]")
    print("The visibility of the edit link : ",edit_record.is_displayed())
    edit_record.click()
    print(driver.current_url)

def table_two():
    name = "Frank"
    get_name = driver.find_element(By.XPATH,f"//table[@id='table2']//tbody/tr/td[contains(.,'{name}')]").text
    print(get_name)
    delete_record = driver.find_element(By.XPATH,f"//table[@id='table2']//tbody/tr/td[contains(.,'{name}')]/parent::tr/td/a[contains(.,'delete')]")
    print("The visibility of the edit link : ", delete_record.is_displayed())
    delete_record.click()
    print(driver.current_url)

table_one()
table_two()