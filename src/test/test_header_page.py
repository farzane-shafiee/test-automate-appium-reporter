from src.logs.logs_config import logger
from src.test.conftest import BaseTest
from src.page.header_page.header_page import HeaderPage


class TestReporter(BaseTest):
    def test_search(self):
        header_page = HeaderPage(self.driver)

        header_page.wait_element_to_be_clickable(
            self.wait, header_page.locator['search_button']
        )
        header_page.click_search_button()
        logger.info('click search button')

