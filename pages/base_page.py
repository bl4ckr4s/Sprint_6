import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from constants import Constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Constants.BASE_URL

    @allure.step('go to site')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step('find element')
    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator),
                                                      message=f'Not find {locator}')

    @allure.step('click')
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step('scroll to element')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('set value')
    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step('get current url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('switch to next tab')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('click on question')
    def click_on_question(self, locator):
        self.scroll_to_element(locator)
        return self.find_element(locator).click()
