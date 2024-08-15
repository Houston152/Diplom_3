from selenium.webdriver.common.by import By


class AuthPageLocators:
    RESTORE_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')  # гиперссылка "Восстановить пароль"
    EMAIL = (By.XPATH, '//input[@name="name"]')  # поле ввода email на странице авторизации
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  # поле ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"
