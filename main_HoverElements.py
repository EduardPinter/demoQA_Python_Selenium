import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import data
from pages.mainPage import MainPage
from pages.widgetsPage import WidgetsPage
from pages.toolTipPage import ToolTipPage


class HoverElements(unittest.TestCase):

    def setUp(self):

        self.browserName = input("Enter the browser you want to use -> ")

        if self.browserName == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.browserName == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            print("Browser name ==> " + self.browserName)

        self.driver.get("https://demoqa.com")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_hover_elements(self):
        mainPage = MainPage(self.driver)
        mainPage.click_on_widgets()
        widgetsPage = WidgetsPage(self.driver)
        widgetsPage.click_on_tool_tip()
        toolTipPage = ToolTipPage(self.driver)
        toolTipPage.hover_button(toolTipPage.TOOL_TIP_BTN,toolTipPage.BTN_MESSAGE)
        self.assertEqual(toolTipPage.get_button_text(), data.HoverElementsData.buttonMessageHover,
                         f'Expected result {data.HoverElementsData.buttonMessageHover=},'
                         f' Actual result {toolTipPage.get_button_text()=}')
        tooltip_message_hover = toolTipPage.hover_input_field(toolTipPage.TEXT_FIELD,toolTipPage.TEXT_FIELD_MESSAGE)
        self.assertEqual(toolTipPage.get_fieldMessage_text(toolTipPage.TEXT_FIELD_MESSAGE),
                         data.HoverElementsData.inputFieldMessage,
                         f'Expected result {data.HoverElementsData.inputFieldMessage=},'f'Actual result {tooltip_message_hover=}')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()