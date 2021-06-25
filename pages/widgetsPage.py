from locator import *
from pages.page import BasePageStart

class WidgetsPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.TOOL_TIP = (By.XPATH,"//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[4]/div/ul[@class='menu-list']/li[7]")

    def click_on_tool_tip(self):
        element = self.driver.find_element(*self.TOOL_TIP)
        element.location_once_scrolled_into_view
        element.click()