from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/iframe-training")

# can't find it cuz it's an iframe， will raise exception
# msg = browser.find_element(By.CSS_SELECTOR, "div#block-ec928cee802cf918d26c div p")

# just need to switch to iframe first
iframe = browser.find_element(By.CSS_SELECTOR, "iframe")
browser.switch_to.frame(iframe)
msg = browser.find_element(By.CSS_SELECTOR, "div#block-ec928cee802cf918d26c div p")
print(msg.text)

# this won't work cuz that is outside the iframe
# content = browser.find_element(By.CSS_SELECTOR, "div#block-5d3de848045889000188d389")

browser.switch_to.default_content()
content = browser.find_element(By.CSS_SELECTOR, "div#block-5d3de848045889000188d389")
print(content.text)
