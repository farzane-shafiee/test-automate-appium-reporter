from selenium.webdriver.common.by import By
from src.tests.conftest import BasePage
from src.page.header_page.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    """
    All header page tests operations are in this class.
    """
    def __init__(self, driver):
        self.locator = HeaderPageLocators()
        super().__init__(driver)

    def click_search_button(self):
        self.driver.find_element(By.ID, self.locator['search_button']).click()
        # self.find_element_by_id(self.locator['search_button']).click()

    def send_keys_search_input(self, search_input):
        self.driver.find_element(By.ID, self.locator['search_input']).send_keys(search_input)

    def click_report_button(self):
        self.driver.find_element(By.ID, self.locator['report_button']).click()

    def assert_text(self):
        text = self.driver.find_element(By.XPATH, self.locator['assert_element_clock'])
        return text.text
