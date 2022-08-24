from selenium import webdriver
from selenium.webdriver.common.alert import  Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

from selenium.webdriver.support.select import  Select

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

# Explict wait
print("I've arrived!")
WebDriverWait(browser, 5).until(alert_is_present())
print("I see an alert!")

