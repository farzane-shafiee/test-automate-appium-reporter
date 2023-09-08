from selenium.webdriver.common.by import By
from src.config.page_config.base_page import BasePage
from src.apps.reporter_app.page.landing_page.landing_page_locators import LandingPageLocators


class LandingPageAction(BasePage):
    """
    All Landing page tests operations are in this class.
    """
    def __init__(self, driver):
        self.locator = LandingPageLocators()
        super().__init__(driver)

    def click_report_button(self):
        self.driver.find_element(By.ID, self.locator['report_button']).click()

    def find_search_result_list(self):
        if self.driver.find_elements(By.XPATH, self.locator['search_result_list']):
            elements = self.driver.find_elements(By.XPATH, self.locator['search_result_list'])
            return elements
        else:
            return ""
