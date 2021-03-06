import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import data
from pages.mainPage import MainPage
from pages.elementsPage import ElementsPage
from pages.dynamicPropertiesPage import  DynamicPropertiesPage


class DynamicProperties(unittest.TestCase):

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

    def test_dynamic_properties(self):
        mainPage = MainPage(self.driver)
        mainPage.click_on_elements()
        elementsPage = ElementsPage(self.driver)
        elementsPage.click_on_dynamic_properties()
        dynamicPropertiesP = DynamicPropertiesPage(self.driver)
        self.assertEqual(dynamicPropertiesP.get_random_text(),data.DynamicPropertiesData.randomTextId)
        self.assertEqual(dynamicPropertiesP.get_enable_button_false(), False)
        dynamicPropertiesP.visible_after_exception()
        self.assertEqual(dynamicPropertiesP.get_enable_button_true(), True)
        self.assertEqual(dynamicPropertiesP.get_color_assert(), data.DynamicPropertiesData.colorAsserting)
        self.assertEqual(dynamicPropertiesP.visible_after(), True)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()