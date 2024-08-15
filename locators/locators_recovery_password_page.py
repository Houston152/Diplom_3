from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    PASSWORD_RECOVERY_TEXT = (By.XPATH, '//h2[text()="Восстановление пароля"]')  # текст "Восстановление пароля"
    INPUT_EMAIL = (By.XPATH, '//input[contains(@class, "text")]')  # поле ввода "Email"
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка "Восстановить"
    INPUT_NEW_PASSWORD = (By.CSS_SELECTOR, '[name="Введите новый пароль"]')  # поле ввода "Пароль"
    INPUT_ICON = (By.XPATH, '//div[contains(@class, "input__icon")]')  # кнопка показать/скрыть пароль
    ACTIVE_INPUT_NEW_PASSWORD = (By.XPATH, '//div[contains(@class, "input_status_active")]')  # активный инпут "Пароль"
