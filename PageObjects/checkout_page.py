from selenium.webdriver.common.by import By

from PageObjects.confirm_page import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_elements_by_css_selector(".card-title a")
    # self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    added_items = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    check_out = (By.XPATH,"//button[@class='btn btn-success']")

    def get_card_title(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckOutPage.card_footer)

    def verify_cart(self):
        return self.driver.find_element(*CheckOutPage.added_items)

    def check_out_items(self):
        self.driver.find_element(*CheckOutPage.check_out).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page


