import pytest

from PageObjects.home_page import HomePage
from TestData.home_page_data import HomePageData
from Utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestHomePage(BaseClass):

    def test_form_submission(self,get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        log.info("first name is:" + get_data["firstname"])
        home_page.get_name().send_keys(get_data["firstname"])
        home_page.get_email().send_keys(get_data["email"])
        home_page.get_checkbox().click()
        self.select_option(home_page.get_gender(), get_data["gender"])
        home_page.submit_form().click()

        alert_text = home_page.get_success_message().text

        assert ("Success" in alert_text)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("testcase2"))
    def get_data(self, request):
        return request.param
