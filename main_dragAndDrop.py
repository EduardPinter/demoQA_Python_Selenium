import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.mainPage import MainPage
from pages.interactionsPage import InteractionsPage
from pages.droppablePage import DroppablePage


class DragAndDrop(unittest.TestCase):

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
        mainPage.click_on_interactions()
        interactionsPage = InteractionsPage(self.driver)
        interactionsPage.click_on_droppable()
        droppablePage = DroppablePage(self.driver)
        droppablePage.drag_drop()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()