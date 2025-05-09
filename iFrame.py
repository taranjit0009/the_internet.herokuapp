import time

from selenium.webdriver.chrome.service import Service
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/frames")

def nested_iframe():
    driver.find_element(By.PARTIAL_LINK_TEXT,"Nested Frames").click()
    time.sleep(5)
    WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"frame[name='frame-top']")))
    frame_1 = driver.find_element(By.CSS_SELECTOR,"frame[name='frame-left']")
    driver.switch_to.frame(frame_1)
    time.sleep(5)
    lf_text= driver.find_element(By.TAG_NAME,"body").text
    print(lf_text)
    driver.switch_to.parent_frame()
    right_frame = driver.find_element(By.CSS_SELECTOR,"frame[name='frame-right")
    driver.switch_to.frame(right_frame)
    rt_text= driver.find_element(By.TAG_NAME,"body").text
    print(rt_text)
    driver.switch_to.default_content()
nested_iframe()

"""
frames = driver.find_elements(By.TAG_NAME, "frame")
    driver.switch_to.frame(frames[0])  # frame-top
    # ... actions ...
    frame_left =driver.find_element(By.NAME,"frame-left")
    driver.switch_to.frame(frame_left)
    lf=driver.find_element(By.TAG_NAME,"body").text
    print(lf)
    driver.switch_to.parent_frame()
    right_f=driver.find_element(By.CSS_SELECTOR,"frame[name='frame-right']")
    driver.switch_to.frame(right_f)
    r_text = driver.find_element(By.TAG_NAME,"body").text
    print(r_text)
    driver.switch_to.parent_frame()
"""

def nested_iframe():
    pass