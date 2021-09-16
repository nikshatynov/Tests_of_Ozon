import self
from selenium.webdriver.common.by import By

from base import BasePage


class OzonSearchLocators:
    LOCATOR_OZON_SEARCH_FIELD = (By.NAME, "text")
    LOCATOR_OZON_SEARCH_BUTTON = (By.CLASS_NAME, "f9k")
    LOCATOR_OZON_CATALOG = (By.CLASS_NAME, "kxa6")
    LOCATOR_OZON_ELECTRONIKA = (By.CLASS_NAME, "g5s7")
    LOCATOR_OZON_SHOPCART = (By.CLASS_NAME, "d1b3")
    LOCATOR_OZON_FOLLOW = (By.CLASS_NAME, "e3i2")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(OzonSearchLocators.LOCATOR_OZON_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(OzonSearchLocators.LOCATOR_OZON_SEARCH_BUTTON, time=2).click()

    def click_catalog(self):
        return self.find_element(OzonSearchLocators.LOCATOR_OZON_CATALOG, time=2).click()

    def click_elektronika(self):
        return self.find_element(OzonSearchLocators.LOCATOR_OZON_ELECTRONIKA, time=2).click()

    def highlight_and_make_screenshot(self, file_name='element.png'):
        """ Highlight element and make the screen-shot of all page. """
        return self.screenshot(file_name)

    def click_shopcart(self):
        return self.find_element(OzonSearchLocators.LOCATOR_OZON_SHOPCART, time=2).click

    def click_follow(self):
        return self.find_element(OzonSearchLocators.LOCATOR_OZON_FOLLOW, time=2).click
