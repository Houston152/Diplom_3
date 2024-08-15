from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # кнопка "Личный кабинет"
    BUILD_A_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')  # текст "Соберите бургер" на главной странице
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')  # кнопка "Лента заказов"
    INGREDIENT = (By.CSS_SELECTOR, 'img[alt="Флюоресцентная булка R2-D3"]')  # ингредиент
    DETAILS_INGREDIENT = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]')  # окно "Детали ингредиента"
    CLOSE_DETAILS_INGREDIENT = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//button[contains(@class,"Modal_modal__close_modified")]')  # закрыть окно "Детали ингредиента"
    DRAG_HERE = (By.XPATH, '//ul[contains(@class, "BurgerConstructor")]')  # перетащить ингредиент в заказ
    COUNTER_INGREDIENTS = (By.XPATH, '//p[contains(@class, "counter_counter__num")]')  # счетчик ингредиентов
    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    ORDER_IS_PROCESSED = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')  # текст "Ваш заказ начали готовить"
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')  # номер заказа
