from selenium.webdriver.common.by import By
from src.tests.conftest import BasePage
from src.page.report_page.reporter_page_locators import ReporterPageLocators


class ReporterPage(BasePage):
    """
    All header page tests operations are in this class.
    """
    def __init__(self, driver):
        self.locator = ReporterPageLocators()
        super().__init__(driver)

    def click_report_type_dropdown(self):
        self.driver.find_element(By.ID, self.locator["report_type_dropdown"]).click()

