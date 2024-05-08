from selenium.webdriver.common.by import By

from PageObjects.checkout_page import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckOutPage(self.driver)
        return checkout_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.check)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def submit_form(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)
