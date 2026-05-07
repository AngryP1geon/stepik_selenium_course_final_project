from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not present."

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        assert BasePage.solve_quiz_and_get_code(self), \
            "Quiz is not solved and code is not gotten."

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not present."

    def is_product_name_match_product_name_in_success_message(self):
        time.sleep(2)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_success_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert product_name == product_name_in_success_message, \
            f"Product name ({product_name}) and product name in success message ({product_name_in_success_message}) do not match."

    def should_be_basket_cost_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_MESSAGE), \
            "Basket cost message is not present."

    def is_product_cost_match_product_cost_in_basket_cost_message(self):
        time.sleep(2)
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        product_cost_in_basket_cost_message = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_IN_BASKET_COST_MESSAGE).text
        assert product_cost == product_cost_in_basket_cost_message, \
            f"Product cost ({product_cost}) and product cost in basket cost message ({product_cost_in_basket_cost_message}) do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is present, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it present"