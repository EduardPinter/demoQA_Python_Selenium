from selenium.webdriver import ActionChains
from locator import *
from pages.page import BasePageStart


class DroppablePage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.DRAGGABLE = (By.CSS_SELECTOR, "div#draggable")
        self.DROPPABLE = (By.CSS_SELECTOR, "#simpleDropContainer #droppable")
        self.action = ActionChains(self.driver)

    def click_and_drag(self, x_from, y_from, x_to, y_to):
        element = self.driver.find_element(*self.DRAGGABLE)
        self.action.move_to_element(element)
        self.action.move_by_offset(x_from, y_from)
        self.action.click_and_hold(on_element=None)
        self.action.move_by_offset(x_to, y_to)
        self.action.release(on_element=None)
        self.action.perform()

    def get_color_assert(self):

        return self.driver.find_element(*self.DROPPABLE).value_of_css_property('background-color')
