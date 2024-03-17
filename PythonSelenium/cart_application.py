import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Using IMPLICIT_WAIT() to avoid using sleep at multiple lines.
# It will wait up to 5 seconds and if the page loads before 5 it will continue right away.
# If you use time.sleep(3) => It will wait 3 seconds in all condition.

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
expected_list = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_list = []


driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")

# putting time.sleep here as to give time to load vegetables
# otherwise it will return empty list sometimes, and it won't catch by wait.
time.sleep(3)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)

# check if passing "ber" results in some suggested vegetables ,
# so count should always be greater than 0.
assert count > 0

for result in results:
    actual_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expected_list == actual_list


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promobtn").click()


# Using EXPLICIT WAIT on this line of code as it may take a while to load this element.
# so we are only applying explicit wait to this line and not entire test.

explicit_wait = WebDriverWait(driver, 10)
explicit_wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
code_success = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(code_success)
assert "applied" in code_success

# SUM Validation
prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)  # converting price in integer as it was stored as string.

print(sum)
total_amount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert sum == total_amount

# discount = int(driver.find_element(By.CLASS_NAME,"discountPerc").text) /100

# print(discount)

discounted_amount = float(driver.find_element(By.CLASS_NAME,"discountAmt").text)

# if discount > 0:
assert discounted_amount < total_amount
print(discounted_amount)







