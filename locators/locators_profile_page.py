from selenium.webdriver.common.by import By


class AccountProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # кнопка выхода из Личного кабинета
    ORDERS_HISTORY = (By.XPATH, '//a[@href="/account/order-history"]')  # кнопка История заказов
    CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка Конструктор
    