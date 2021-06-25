from locator import *
from pages.page import BasePageStart

class InteractionsPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.DROPPABLE = (By.XPATH, "//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[5]/div/ul[@class='menu-list']/li[4]/span[@class='text']")


    def click_on_droppable(self):
        element = self.driver.find_element(*self.DROPPABLE)
        element.location_once_scrolled_into_view
        element.click()