from locator import *
from pages.page import BasePageStart

class MainPage(BasePageStart.BasePage):

    def click_on_elements(self):
        element = self.driver.find_element(*DynamicPropertiesLocators.ELEMENTS_PROP_CARD)
        element.click()

    def click_on_widgets(self):
        element = self.driver.find_element(*HoverElementsLocators.WIDGETS_PROP_CARD)
        element.click()

    def click_on_interactions(self):
        element = self.driver.find_element(*DragAndDropLocators.INTERACTIONS_PAGE)
        element.click()