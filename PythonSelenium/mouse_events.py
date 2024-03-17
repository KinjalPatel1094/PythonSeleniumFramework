import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# creating an object"action" of class "ACTIONCHAINS" to use mouse event methods.
action = ActionChains(driver)

# Different mouse events
# action.double_click()
# action.drag_and_drop()

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# You can perform click/send_keys action also.
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

# For Right click event
# action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).perform()

