import allure
from locators.locators_auth_page import AuthPageLocators
from faker import Faker
from pages.base_page import BasePage

fake = Faker("ru_RU")


class LoginPage(BasePage):
    @allure.step('Нажать на гиперcсылку "Восстановить пароль"')
    def click_hyperlink_password_recovery(self):
        self.visibility_of_element_located(AuthPageLocators.RESTORE_PASSWORD).click()

    @allure.step('Ввести email')
    def input_email(self):
        (self.visibility_of_element_located(AuthPageLocators.EMAIL).send_keys(fake.ascii_free_email()))

    @allure.step('Ввести пароль')
    def input_password(self):
        (self.visibility_of_element_located(AuthPageLocators.EMAIL).send_keys(fake.fake.password()))

    @allure.step('Нажать на кнопку "Войти"')
    def click_button_entry(self):
        self.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON).click()

    @allure.step('Проверить наличие кнопки "Войти"')
    def check_button_entry(self):
        return self.visibility_of_element_located(AuthPageLocators.LOGIN_BUTTON)
