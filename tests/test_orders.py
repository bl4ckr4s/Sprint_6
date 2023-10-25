import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.mark.parametrize(
    'used_button, name, surname, address, station, phone, date',
    [
        ['top', 'Иван', 'Иванов', 'Светлая', 'Речной вокзал', '89166666666', '24.10.2023'],
        ['bottom', 'Петр', 'Петров', 'Солнечная', 'ВДНХ', '89177777777', '27.10.2023'],
    ]
)
class TestOrders:
    @allure.title('Checking the successful order creation')
    def test_order_scooter(self, driver, used_button, name, surname, address, station, phone, date):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_order_button(used_button)

        order_page = OrderPage(driver)
        order_page.order_scooter(name, surname, address, station, phone, date)
        order_info = order_page.get_order_info()
        assert 'Заказ оформлен' in order_info
