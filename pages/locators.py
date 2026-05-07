from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-default[href*='/basket/']:not(.visible-xs-inline-block)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form1")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form1")
    REGISTER_FORM_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3)")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRODUCT_COST_IN_BASKET_COST_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p:nth-child(1) > strong")

class BasketPageLocators():
    PRODUCTS_IN_BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title.hidden-xs")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")