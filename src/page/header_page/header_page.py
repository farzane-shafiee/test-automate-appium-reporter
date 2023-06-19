from src.test.conftest import BasePage
from src.page.header_page.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    def __init__(self, driver):
        self.locator = HeaderPageLocators()
        super().__init__(driver)

    def click_search_button(self):
        self.find_element_by_id(self.locator['search_button']).click()
