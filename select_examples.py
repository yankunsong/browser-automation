from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

sel = browser.find_element(By.ID, "sel1")

my_select = Select(sel)

my_select.select_by_visible_text('Beets')

my_select.select_by_index(2)

my_select.select_by_value("second")