import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('set name')
    def set_name(self, name):
        self.set_value(OrderPageLocators.NAME_FIELD, name)

    @allure.step('set surname')
    def set_surname(self, surname):
        self.set_value(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('set address')
    def set_address(self, address):
        self.set_value(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('set station')
    def set_station(self, station):
        self.set_value(OrderPageLocators.STATION_FIELD, station)
        self.click(OrderPageLocators.STATION_SELECT)

    @allure.step('set phone')
    def set_phone(self, phone):
        self.set_value(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('click next button')
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('set date')
    def set_date(self, date):
        self.set_value(OrderPageLocators.DATE_FIELD, date)

    @allure.step('set period')
    def set_period(self):
        self.click(OrderPageLocators.PERIOD_FIELD)
        self.click(OrderPageLocators.PERIOD_OPTION)

    @allure.step('set color')
    def set_color(self):
        self.click(OrderPageLocators.COLOR_BLACK)

    @allure.step('click order button')
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('click confirm button')
    def click_confirm_button(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('order scooter')
    def order_scooter(self, name, surname, address, station, phone, date):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone(phone)
        self.click_next_button()
        self.set_date(date)
        self.set_period()
        self.set_color()
        self.click_order_button()
        self.click_confirm_button()

    @allure.step('get order info')
    def get_order_info(self):
        return self.find_element(OrderPageLocators.ORDER_INFO_HEADER).text
