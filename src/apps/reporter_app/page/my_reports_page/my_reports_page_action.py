import datetime

from selenium.webdriver.common.by import By
from src.config.page_config.base_page import BasePage
from src.apps.reporter_app.page.my_reports_page.my_reports_page_locators import MyReportsPageLocators


class MyReportsPageAction(BasePage):
    """
    All my reports page tests operations are in this class.
    """
    def __init__(self, driver):
        self.locator = MyReportsPageLocators()
        super().__init__(driver)

    def my_reports_list(self):
        element = self.driver.find_elements(By.ID, self.locator['my_reports_list'])
        return element

    def get_text_type_of_report(self):
        text_element = self.driver.find_element(By.ID, self.locator['assert_report_type_label']).text
        return text_element

    def getting_date_time_my_report(self):
        text = self.driver.find_element(By.ID, self.locator['date_time_label']).text
        date_time_text = text.split(":", 1)[0]  # split minutes and seconds
        return date_time_text
