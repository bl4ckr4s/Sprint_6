from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from constants import Constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Constants.BASE_URL

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator),
                                                      message=f'Not find {locator}')

    def click(self, locator):
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
