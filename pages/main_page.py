from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_on_question(self, locator):
        self.scroll_to_element(locator)
        return self.find_element(locator).click()

    def click_on_top_order_button(self):
        return self.find_element(MainPageLocators.TOP_ORDER_BUTTON).click()

    def click_on_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        return self.find_element(MainPageLocators.BOTTOM_ORDER_BUTTON).click()
