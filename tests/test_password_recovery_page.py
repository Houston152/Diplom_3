import allure
import pytest
from locators.locators_main_page import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @pytest.mark.parametrize('locator_button',
                             [MainPageLocators.LOGIN_BUTTON, MainPageLocators.PERSONAL_ACCOUNT_BUTTON])
    def test_go_to_page_password_recovery(self, driver, locator_button):
        main_page = MainPage(driver)
        main_page.click_to_login_button_with_locator(locator_button)
        login_page = LoginPage(driver)
        login_page.click_hyperlink_password_recovery()
        password_recovery_page = PasswordRecoveryPage(driver)
        assert password_recovery_page.check_password_recovery_text(), \
            'Не удалось перейти на страницу восстановления пароля'

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_click_to_button_restore(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_login_button()
        login_page = LoginPage(driver)
        login_page.click_hyperlink_password_recovery()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.input_email()
        password_recovery_page.click_recovery_button()
        assert password_recovery_page.check_input_new_password(), 'Не удалось перейти на страницу восстановление пароля'

    @allure.title('При клике по инпуту ввода пароля оно становится активным')
    def test_click_to_input(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_login_button()
        login_page = LoginPage(driver)
        login_page.click_hyperlink_password_recovery()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.input_email()
        password_recovery_page.click_recovery_button()
        password_recovery_page.click_icon_in_input_new_password()
        assert password_recovery_page.check_input_new_password_active(), \
            'Инпут ввода пароля не активен'
