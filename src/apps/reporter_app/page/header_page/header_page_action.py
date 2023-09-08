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

    def assert_search_button(self):
        element = self.driver.find_element(By.ID, self.locator['search_button'])
        return element

    def get_report_page_label(self):
        search_result = self.driver.find_element(By.ID, self.locator['assert_report_page_label'])
        return search_result

    def click_cross_button_search_box(self):
        self.driver.find_element(By.ID, self.locator['cross_button']).click()

    def get_home_page_title(self):
        element = self.driver.find_element(By.ID, self.locator['home_page_title'])
        return element

    def click_device_tab(self):
        self.driver.find_element(By.ID, self.locator['device_tab']).click()

    def click_app_tab(self):
        self.driver.find_element(By.ID, self.locator['app_tab']).click()

    def click_more_options_button(self):
        self.driver.find_element(By.XPATH, self.locator['more_options_button']).click()

    def click_my_reports_button(self):
        self.driver.find_element(By.ID, self.locator['my_reports_button']).click()
