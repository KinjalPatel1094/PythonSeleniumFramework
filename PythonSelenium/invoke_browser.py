import time

from selenium import webdriver

# Invoke Chrome browser using chrome driver
# Different browser invoke
# firefox = geckodriver
# Edge = Edge driver
# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver = webdriver.Chrome()
driver.get("https://github.com/KinjalPatel1094")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(3)
