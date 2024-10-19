from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Edge()


def xpath(xpath, timeout=5):
    global driver
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(
            (By.XPATH, xpath)
        ), message=f'Timeout: Element with xpath "{xpath}" took too long to appear or was not found!'
    )
    time.sleep(0.3)
    return element


def if_element_is_displayed(xpath, timeout=5):
    global driver
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, xpath)
            )
        )
        return True
    except:
        return False







