import data
from locator import *
from pages.page import BasePageStart

class UploadPage(BasePageStart.BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.UPLOAD_FILE = (By.ID, "uploadFile")
        self.ALERT_MESSAGE = (By.ID, "uploadedFilePath")

    def upload_file(self):

        self.driver.find_element(*self.UPLOAD_FILE).send_keys(data.UploadData.filePath)

    def get_alert_message(self):

        return self.driver.find_element(*self.ALERT_MESSAGE).text


