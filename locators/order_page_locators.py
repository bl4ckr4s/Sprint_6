from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    STATION_FIELD = [By.CLASS_NAME, "select-search__input"]
    STATION_SELECT = [By.CLASS_NAME, "select-search__select"]
    PHONE_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//div[@class='Order_NextButton__1_rCA']/button"]
    DATE_FIELD = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    PERIOD_FIELD = [By.XPATH, "//span[@class='Dropdown-arrow']"]
    PERIOD_OPTION = [By.XPATH, "//div[@class='Dropdown-option'][1]"]
    COLOR_BLACK = [By.ID, "black"]
    ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    CONFIRM_BUTTON = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[contains(text(),'Да')]"]
    ORDER_INFO_HEADER = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
