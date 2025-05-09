from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/notification_message_rendered")

st_msg_1 = "Action unsuccesful, please try again"
st_msg_2 ="Action successful"
def action_unsuccessful_notification_render():
    wait  = WebDriverWait(driver,10)
    while True:
        try:
            ele = driver.find_element(By.XPATH,"//a[normalize-space()='Click here']")
            ele.click()
            msg = (By.ID, "flash")
            if wait.until(EC.text_to_be_present_in_element(msg,st_msg_1)):
                print(st_msg_1)
                break
            """
            #StaleElementReferenceException or TimeoutException,
            I have used this because I have run the script in while loop for getting message.
            """
        except Exception as e:
            print(f"Exception occurred: {e}")
action_unsuccessful_notification_render()
def action_successful_notification_render():
    wait  = WebDriverWait(driver,10)
    ele = driver.find_element(By.XPATH, "//a[normalize-space()='Click here']")
    while True:
        try:
            ele.click()
            msg = (By.ID, "flash")
            if wait.until(EC.text_to_be_present_in_element(msg,st_msg_2)):
                print(st_msg_2)
                break
            """
            #StaleElementReferenceException or TimeoutException,
            I have used this because I have run the script in while loop for getting message.
            """
        except Exception as e:
            print(f"Exception occurred: {e}")


action_successful_notification_render()


