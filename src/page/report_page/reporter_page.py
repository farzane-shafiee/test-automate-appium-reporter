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

    def click_report_button(self):
        self.driver.find_element(By.ID, self.locator['report_button']).click()

    def assert_text(self):
        text = self.driver.find_element(By.XPATH, self.locator['assert_element'])
        return text.text

    def click_report_type_dropdown(self):
        self.driver.find_element(By.ID, self.locator["report_type_dropdown"]).click()

    def click_bug_report_dropdown_button(self):
        self.driver.find_element(By.XPATH, self.locator['bug_report_dropdown_button']).click()

    def click_attach_file_button(self):
        self.driver.find_element(By.ID, self.locator['attach_file_button']).click()

    def click_image_file(self):
        self.driver.find_element(By.ID, self.locator['image_file']).click()

    def click_bug_report_text_input(self):
        self.driver.find_element(By.ID, self.locator['bug_report_text_input']).click()

    def insert_bug_report_text(self, text):
        self.driver.find_element(By.ID, self.locator['bug_report_text_input']).send_keys(text)
