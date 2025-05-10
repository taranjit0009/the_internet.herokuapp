from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/shadowdom")


def get_shadow_dom(element):
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", element)
    return shadow_root

def shadow_dom():
    try:
        grand_ele = driver.find_element(By.TAG_NAME,"my-paragraph")
        ele_1 = get_shadow_dom(grand_ele)
        hidden_txt = ele_1.find_element(By.CSS_SELECTOR,"slot[name='my-text']").text
        print(hidden_txt)
    except Exception as e:
        print(e)
shadow_dom()