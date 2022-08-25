from selenium import webdriver
from pages.training_ground_page import TrainingGroundPage

# Setup
browser = webdriver.Chrome()
test_msg = "it worked!"

# Test
training_page = TrainingGroundPage(driver=browser)
training_page.go()

assert training_page.btn1.text == "Button1"
# training_page.btn1.click()
browser.quit()