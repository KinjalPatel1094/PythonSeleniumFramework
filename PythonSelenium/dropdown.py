import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(4)

# FIND_ELEMENTS will find all countries suggested in list that comes under this CSS_SELECTOR
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

# Search in list of countries to find the perfect match
for country in countries:
    if country.text == "India":
        country.click()
        break

time.sleep(2)
# Get selected dropdown value using "Value" attribute
# print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

# USE ASSERTION to verify test pass or fail
assert (driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India")











