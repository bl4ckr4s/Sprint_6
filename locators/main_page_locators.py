from selenium.webdriver.common.by import By


class MainPageLocators:
    HOW_MUCH_QUESTION = [By.ID, 'accordion__heading-0']
    HOW_MUCH_ANSWER = [By.XPATH, "//div[@id='accordion__panel-0']/p"]
    QUANTITY_QUESTION = [By.ID, 'accordion__heading-1']
    QUANTITY_ANSWER = [By.XPATH, "//div[@id='accordion__panel-1']/p"]
    RENTAL_TIME_QUESTION = [By.ID, 'accordion__heading-2']
    RENTAL_TIME_ANSWER = [By.XPATH, "//div[@id='accordion__panel-2']/p"]
    ORDER_TODAY_QUESTION = [By.ID, 'accordion__heading-3']
    ORDER_TODAY_ANSWER = [By.XPATH, "//div[@id='accordion__panel-3']/p"]
    EXTEND_ORDER_QUESTION = [By.ID, 'accordion__heading-4']
    EXTEND_ORDER_ANSWER = [By.XPATH, "//div[@id='accordion__panel-4']/p"]
    CHARGER_QUESTION = [By.ID, 'accordion__heading-5']
    CHARGER_ANSWER = [By.XPATH, "//div[@id='accordion__panel-5']/p"]
    CANCEL_QUESTION = [By.ID, 'accordion__heading-6']
    CANCEL_ANSWER = [By.XPATH, "//div[@id='accordion__panel-6']/p"]
    DISTANCE_QUESTION = [By.ID, 'accordion__heading-7']
    DISTANCE_ANSWER = [By.XPATH, "//div[@id='accordion__panel-7']/p"]
    TOP_ORDER_BUTTON = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button"]
