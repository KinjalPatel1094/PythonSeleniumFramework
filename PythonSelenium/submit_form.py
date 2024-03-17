import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# Find element by ID, NAME
driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test")
driver.find_element(By.ID, "exampleCheck1").click()

# Find element using x-path
# syntax for x-path : //tag_name[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Find element using CSSSelector
# same syntax as X-path except for @ and //.
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("kinjal patel")

# Turning ID by adding "#" to CSS SELECTOR , also for  class name -> use "."
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("Hello Again")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()

# Find element by CLASS_NAME
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

# Set the assertion to check for string present in the message after submitting the form.
assert "success" in message

# Find element for STATIC DROPDOWN
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value()








time.sleep(5)
