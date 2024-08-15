import allure
from locators.locators_order_history_page import AccountOrderHistoryPageLocators
from pages.base_page import BasePage


class AccountOrderHistoryPage(BasePage):
    @allure.step('Получить номер заказа')
    def check_order_number(self):
        return self.visibility_of_element_located(AccountOrderHistoryPageLocators.ORDER_NUMBER).text

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_button_order_feed(self):
        return self.visibility_of_element_located(AccountOrderHistoryPageLocators.ORDER_FEED).click()
