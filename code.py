from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

# CSS selector $$("input[id='ipt1']")
input1Path = "input[id='ipt1']"
from selenium.webdriver.common.by import By

input1Element = browser.find_element(By.CSS_SELECTOR, input1Path)
input1Element.send_keys("haha")

# XPath
"""
Used when hard to get the unique element via CSS selector
find its unique, repeatable children, and then go up
$x("//button[@name='butn1']")
$x("//b[contains(text(), 'Product 1')]")
$x("//b[contains(text(), 'Product 1')]/../..")
$x("//b[contains(text(), 'Product 1')]/../b")
"""

