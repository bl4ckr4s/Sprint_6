from locators.base_page_locators import BasePageLocators
from pages.main_page import MainPage
from constants import Constants


class TestLogos:
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_top_order_button()
        main_page.click(BasePageLocators.SCOOTER_LOGO)
        assert main_page.get_current_url() == Constants.BASE_URL

    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click(BasePageLocators.YANDEX_LOGO)
        main_page.switch_to_next_tab()
        main_page.find_element(BasePageLocators.DZEN_LOGO, 15)
        assert main_page.get_current_url() == Constants.DZEN_URL
