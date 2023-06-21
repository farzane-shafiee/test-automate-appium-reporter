import time
import pytest
from src.logs.logs_config import logger
from src.page.header_page.header_page import HeaderPage
from src.tests.conftest import BaseTest


class TestSearch(BaseTest):

    @classmethod
    def teardown_class(cls):
        pass

    def test_01_searches(self):
        """
        tests search box.
        """
        header_page = HeaderPage(self.driver)

        logger.info('Connected device is successfully')

        header_page.wait_element_to_be_clickable_by_id(
            self.wait, header_page.locator['search_button']
        )
        header_page.click_search_button()
        logger.info('Click the search button')

        header_page.send_keys_search_input('clock')
        logger.info('Insert the word "clock" in the search box')

        header_page.wait_visibility_of_element_located_by_xpath(
            self.wait, header_page.locator['assert_element_clock']
        )

        header_page.click_report_button()
        logger.info('Click the report button Clock app')

        header_page.wait_visibility_of_element_located_by_xpath(
            self.wait, header_page.locator['assert_element_clock']
        )

        logger.info('Search assertion was successful')
        time.sleep(3)
