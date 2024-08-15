from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')  # текст "Лента заказов"
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')  # номер заказа
    ORDER = (By.XPATH, '//li[contains(@class, "OrderHistory")]')  # заказ
    DETAILS_ORDER = (By.XPATH, '//div[contains(@class, "Modal_orderBox")]')  # модальное окно с деталями заказа
    ORDERS_OF_ALL_TIME = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')  # Выполнено заказов за все время
    ORDERS_FOR_TODAY = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')  # Выполнено заказов за сегодня
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # кнопка "Личный кабинет"
    CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка Конструктор
    ORDER_IN_WORK = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]'
                               '/li[contains(@class, "text text_type_digits")]')  # заказ в работе
