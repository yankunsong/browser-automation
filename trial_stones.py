from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")

# 1 Riddle of Stones

stone_input = browser.find_element(By.CSS_SELECTOR, "input#r1Input")
stone_ans_btn = browser.find_element(By.ID, "r1Btn")
stone_res = browser.find_element(By.CSS_SELECTOR, "div#passwordBanner > h4")


# 2 Riddle of Secrets
secrets_input = browser.find_element(By.CSS_SELECTOR, "input#r2Input")
secrets_ans_btn = browser.find_element(By.CSS_SELECTOR, "button#r2Butn")


# 3 Two Merchants
# simple approach
richest_name = browser.find_element(By.XPATH, "//p[text()='3000']/../span/b")
merchant_input = browser.find_element(By.ID, "r3Input")
merchant_ans_btn = browser.find_element(By.CSS_SELECTOR, "button#r3Butn")

check_btn = browser.find_element(By.CSS_SELECTOR, "button[name='checkButn']")

complete_msg = browser.find_element(By.CSS_SELECTOR, "div#trialCompleteBanner h4")




# Mock

stone_input.send_keys("rock")
stone_ans_btn.click()
# if the text is between tags, use .text, if is in an input field, use .value
password = stone_res.text

secrets_input.send_keys(password)
secrets_ans_btn.click()

merchant_input.send_keys(richest_name.text)
merchant_ans_btn.click()

check_btn.click()
assert complete_msg.text == "Trial Complete"
