from selenium.webdriver.common.by import By


class AccountOrderHistoryPageLocators:
    ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "text text_type_digits")]')   # номер заказа
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')  # кнопка "Лента заказов"
    