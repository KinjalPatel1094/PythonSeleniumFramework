import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from PageObjects.checkout_page import CheckOutPage
from PageObjects.home_page import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.get_logger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()
        log.info("Getting all the card titles")
        cards = checkout_page.get_card_title()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkout_page.get_card_footer()[i].click()

        checkout_page.verify_cart().click()

        confirm_page = checkout_page.check_out_items()
        confirm_page.verify_country().send_keys("ind")

        log.info("Entering country name as ind")

        self.verify_link_presence("India")

        confirm_page.select_county_from_list().click()
        confirm_page.select_check_box().click()
        confirm_page.submit_items().click()
        textMatch = confirm_page.verify_success_message().text
        log.info("Text received from application is" + textMatch)

        assert ("Success! Passed ! Thank you!" in textMatch)
