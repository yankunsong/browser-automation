from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

# this will only have the last one in the end
browser.get("https://techstepacademy.com/trial-of-the-stones")
browser.get("https://google.com")

browser.execute_script("window.open('https://amazon.com', '_blank');")
browser.execute_script("window.open('https://ebay.com', '_blank');")
browser.execute_script("window.open('https://yahoo.com', '_blank');")
print(browser.window_handles)

handles = browser.window_handles
# the tabs are not necessarily in the order of code
# it's better to only do 2 tabs
browser.switch_to.window(handles[2])
