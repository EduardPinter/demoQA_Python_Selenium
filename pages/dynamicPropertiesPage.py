from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *
from pages.page import BasePageStart
import data


class DynamicPropertiesPage(BasePageStart.BasePage):

    def assert_random_text(self):

        randomText = self.driver.find_element(*DynamicPropertiesLocators.RANDOM_TEXT_ID)
        assert randomText.text == data.DynamicPropertiesData.randomTextId

    def visible_after_exception(self):

        try:

            element = self.driver.find_element(*DynamicPropertiesLocators.VISIBLE_AFTER)

        except NoSuchElementException:
            pass

    def enable_button_false(self):

        element = self.driver.find_element(*DynamicPropertiesLocators.ENABLE_BUTTON)
        elementIsEnabled = element.is_enabled()
        assert elementIsEnabled == False, f'Expected False, got {elementIsEnabled=}'

    def enable_button_true(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(DynamicPropertiesLocators.ENABLE_BUTTON))
        element = self.driver.find_element(*DynamicPropertiesLocators.ENABLE_BUTTON)
        elementIsEnabled = element.is_enabled()
        assert elementIsEnabled == True, f'Expected True, got {elementIsEnabled=}'

    def color_assert(self):

        color = self.driver.find_element(*DynamicPropertiesLocators.COLOR_CHANGE)
        colorValue = color.value_of_css_property('color')
        supposedColor = data.DynamicPropertiesData.colorAsserting
        assert colorValue == supposedColor, f'Expected {supposedColor=}, Actual {colorValue=}'

    def visible_after(self):

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(DynamicPropertiesLocators.VISIBLE_AFTER))
        visibleAfter = self.driver.find_element(*DynamicPropertiesLocators.VISIBLE_AFTER)
        visibleAfterDisplayed = visibleAfter.is_displayed()
        assert visibleAfterDisplayed == True, f'Expected True(element to be visible, actual result {visibleAfterDisplayed=}'