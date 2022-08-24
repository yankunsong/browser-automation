from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

input1Path = "input[id='ipt1']"
from selenium.webdriver.common.by import By

input1Element = browser.find_element(By.CSS_SELECTOR, input1Path)
input1Element.send_keys("haha")