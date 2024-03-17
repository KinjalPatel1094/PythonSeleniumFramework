import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/client")
driver.maximize_window()

# finding element using LINK_TEXT
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# finding XPATH using tag name ,finding CSS_SELECTOR using tag name
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("12345")

# using ID as CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("12345")

# finding XPATH using button TEXT
driver.find_element(By.XPATH, "//button[text() = 'Save New Password']").click()


time.sleep(5)

