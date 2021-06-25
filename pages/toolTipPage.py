from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *
from pages.page import BasePageStart


class ToolTipPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.TOOL_TIP_BTN = (By.ID, "toolTipButton")
        self.BTN_MESSAGE = (By.ID, "buttonToolTip")
        self.TEXT_FIELD = (By.ID, "toolTipTextField")
        self.TEXT_FIELD_MESSAGE = (By.ID, "textFieldToolTip")


    def hover_button(self, locator, message):

        button = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(button).perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(message))

    def get_button_text(self):

        return self.driver.find_element(*self.BTN_MESSAGE).text


    def hover_input_field(self,textField, message):

        inputField = self.driver.find_element(*textField)
        action = ActionChains(self.driver)
        action.move_to_element(inputField).perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(message))

    def get_fieldMessage_text(self, textFieldMessage):

        return self.driver.find_element(*textFieldMessage).text
