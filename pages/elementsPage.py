from locator import *
from pages.page import BasePageStart

class ElementsPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.DYNAMIC_PROP_SECTION = (By.XPATH, "//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[9]/span[@class='text']")
        self.UPLOAD_SECTION = (By.XPATH, "//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']//div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[8]/span[@class='text']")

    def click_on_dynamic_properties(self):
        element = self.driver.find_element(*self.DYNAMIC_PROP_SECTION)
        element.location_once_scrolled_into_view
        element.click()

    def click_on_upload(self):
        element = self.driver.find_element(*self.UPLOAD_SECTION)
        element.location_once_scrolled_into_view
        element.click()
