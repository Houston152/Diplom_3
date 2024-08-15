import allure
from locators.locators_profile_page import AccountProfilePageLocators
from pages.base_page import BasePage


class AccountProfilePage(BasePage):
    @allure.step('Проверка кнопки "Выход"')
    def check_logout_button(self):
        return self.visibility_of_element_located(AccountProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_button_orders_history(self):
        self.visibility_of_element_located(AccountProfilePageLocators.ORDERS_HISTORY).click()

    @allure.step('Нажать на кнопку "Выход"')
    def click_logout_button(self):
        self.visibility_of_element_located(AccountProfilePageLocators.LOGOUT_BUTTON).click()

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.visibility_of_element_located(AccountProfilePageLocators.CONSTRUCTOR).click()
