from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *
from pages.page import BasePageStart
import data


class DynamicPropertiesPage(BasePageStart.BasePage):

    def get_random_text(self):

        return self.driver.find_element(*DynamicPropertiesLocators.RANDOM_TEXT_ID).text

    def visible_after_exception(self):

        try:

            element = self.driver.find_element(*DynamicPropertiesLocators.VISIBLE_AFTER)

        except NoSuchElementException:
            pass

    def get_enable_button_false(self):

        return self.driver.find_element(*DynamicPropertiesLocators.ENABLE_BUTTON).is_enabled()

    def get_enable_button_true(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(DynamicPropertiesLocators.ENABLE_BUTTON))
        return self.driver.find_element(*DynamicPropertiesLocators.ENABLE_BUTTON).is_enabled()

    def get_color_assert(self):

        return self.driver.find_element(*DynamicPropertiesLocators.COLOR_CHANGE).value_of_css_property('color')

    def visible_after(self):

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(DynamicPropertiesLocators.VISIBLE_AFTER))
        return self.driver.find_element(*DynamicPropertiesLocators.VISIBLE_AFTER).is_displayed()
