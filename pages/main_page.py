import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('click on order button')
    def click_on_order_button(self, used_button):
        locator = ''
        if used_button == 'top':
            locator = MainPageLocators.TOP_ORDER_BUTTON
        elif used_button == 'bottom':
            locator = MainPageLocators.BOTTOM_ORDER_BUTTON
            self.scroll_to_element(locator)
        return self.find_element(locator).click()
