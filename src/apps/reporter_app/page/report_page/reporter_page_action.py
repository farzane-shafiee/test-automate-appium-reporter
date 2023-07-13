from selenium.webdriver.common.by import By
from src.config.page_config.base_page import BasePage
from src.apps.reporter_app.page.report_page.reporter_page_locators import ReporterPageLocators


class ReporterPageAction(BasePage):
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

    def get_reports_type_list(self):
        elements = self.driver.find_elements(By.XPATH, self.locator['report_type_list'])
        return elements

    def click_attach_file_button(self):
        self.driver.find_element(By.ID, self.locator['attach_file_button']).click()

    def click_image_file(self):
        self.driver.find_element(By.ID, self.locator['image_file']).click()

    def click_bug_report_text_input(self):
        self.driver.find_element(By.ID, self.locator['bug_report_text_input']).click()

    def insert_bug_report_text(self, text):
        self.driver.find_element(By.ID, self.locator['bug_report_text_input']).send_keys(text)
        self.driver.press_keycode(4)

    def click_send_report_button(self):
        self.driver.find_element(By.ID, self.locator['send_report_button']).click()

    def assert_file_manager(self):
        element = self.driver.find_element(By.XPATH, self.locator['assert_file_manager'])
        return element

    def assert_file_attached(self):
        element = self.driver.find_element(By.XPATH, self.locator['assert_not_attach_file'])
        return element

    def click_success_send_report_message(self):
        self.driver.find_element(By.ID, self.locator['close_message_button']).click()


