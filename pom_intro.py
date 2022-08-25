from selenium.webdriver.common.by import By


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground/'

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        inpt = self.driver.find_element(By.ID, 'ipt1')
        inpt.clear()
        inpt.send_keys(text)

    def get_input_text(self):
        inpt = self.driver.find_element(By.ID, 'ipt1')
        elem_text = inpt.get_attribute('value')
        return elem_text

    def click_btn_1(self):
        btn = self.driver.find_element(By.ID, 'b1')
        btn.click()


# Our test
from selenium import webdriver

# Setup
browser = webdriver.Chrome()
test_msg = "it worked!"

# Test
training_page = TrainingGroundPage(browser)
training_page.go()
training_page.type_into_input(test_msg)


assert training_page.get_input_text() == test_msg

training_page.click_btn_1()