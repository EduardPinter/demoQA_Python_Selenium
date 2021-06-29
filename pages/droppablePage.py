from selenium.webdriver import ActionChains
from locator import *
from pages.page import BasePageStart

class DroppablePage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.DRAGGABLE = (By.CSS_SELECTOR, "div#draggable")
        self.DROPPABLE = (By.CSS_SELECTOR, "#simpleDropContainer #droppable")
        self.action = ActionChains(self.driver)


    def drag_drop(self):

        elementDraggable = self.driver.find_element(*self.DRAGGABLE)
        elementDroppable = self.driver.find_element(*self.DROPPABLE)
        self.action.drag_and_drop(elementDraggable,elementDroppable).perform()