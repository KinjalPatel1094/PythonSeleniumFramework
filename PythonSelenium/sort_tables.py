#  Sorting TABLE in selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

browser_sorted_veggies = []

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Click on Colum header first
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()

# Collect all veggie names
veggie_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggie_elements:
    browser_sorted_veggies.append(element.text)

# keep a copy of originally browser sorted veggies
original_browser_sorted_veggies = browser_sorted_veggies.copy()

# Here it will get sort by sort() method
browser_sorted_veggies.sort()

# If assertion FAIL, meaning there is a bug in sorting items in web table.
assert browser_sorted_veggies == original_browser_sorted_veggies





