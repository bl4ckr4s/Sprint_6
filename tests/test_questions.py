import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@pytest.mark.parametrize(
    'question_locator, answer_locator, current_answer',
    [
        [MainPageLocators.HOW_MUCH_QUESTION, MainPageLocators.HOW_MUCH_ANSWER, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [MainPageLocators.QUANTITY_QUESTION, MainPageLocators.QUANTITY_ANSWER, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [MainPageLocators.RENTAL_TIME_QUESTION, MainPageLocators.RENTAL_TIME_ANSWER, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [MainPageLocators.ORDER_TODAY_QUESTION, MainPageLocators.ORDER_TODAY_ANSWER, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [MainPageLocators.EXTEND_ORDER_QUESTION, MainPageLocators.EXTEND_ORDER_ANSWER, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [MainPageLocators.CHARGER_QUESTION, MainPageLocators.CHARGER_ANSWER, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [MainPageLocators.CANCEL_QUESTION, MainPageLocators.CANCEL_ANSWER, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [MainPageLocators.DISTANCE_QUESTION, MainPageLocators.DISTANCE_ANSWER, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'],
    ]
)
class TestQuestions:
    @allure.title('Checking the compliance of the answer')
    def test_question(self, driver, question_locator, answer_locator, current_answer):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question(question_locator)
        answer_text = main_page.find_element(answer_locator).text
        assert answer_text == current_answer
