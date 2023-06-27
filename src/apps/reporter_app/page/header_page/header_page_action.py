from selenium.webdriver.common.by import By
from src.config.page_config.base_page import BasePage
from src.apps.reporter_app.page.header_page.header_page_locators import HeaderPageLocators


class HeaderPageAction(BasePage):
    """
    All header page tests operations are in this class.
    """
    def __init__(self, driver):
        self.locator = HeaderPageLocators()
        super().__init__(driver)

    def click_search_button(self):
        self.driver.find_element(By.ID, self.locator['search_button']).click()

    def send_keys_search_input(self, search_input):
        self.driver.find_element(By.ID, self.locator['search_input']).send_keys(search_input)

    def click_report_button(self):
        self.driver.find_element(By.ID, self.locator['report_button']).click()



