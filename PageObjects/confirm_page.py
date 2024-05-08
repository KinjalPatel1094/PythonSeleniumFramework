from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country_name = (By.ID, "country")
    select_country = (By.LINK_TEXT,"India")
    check_box = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submit_button = (By.CSS_SELECTOR,"[type='submit']")
    alert_message = (By.CSS_SELECTOR,"[class*='alert-success']")


    #self.driver.find_element_by_id("country")
    # self.driver.find_element_by_link_text("India").click()
    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element_by_css_selector("[type='submit']")
    #self.driver.find_element_by_css_selector("[class*='alert-success']")
    def verify_country(self):
        return self.driver.find_element(*ConfirmPage.country_name)

    def select_county_from_list(self):
        return self.driver.find_element(*ConfirmPage.select_country)

    def select_check_box(self):
        return self.driver.find_element(*ConfirmPage.check_box)

    def submit_items(self):
        return self.driver.find_element(*ConfirmPage.submit_button)

    def verify_success_message(self):
        return self.driver.find_element(*ConfirmPage.alert_message)


