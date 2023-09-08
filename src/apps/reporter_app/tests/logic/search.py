import time

from src.apps.reporter_app.page.landing_page.landing_page_action import LandingPageAction
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.header_page.header_page_action import HeaderPageAction
from src.config.test_config.base_test import BaseTest
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH


class TestSearch(BaseTest):

    def __init__(self):
        self.item = None

    def T332_click_and_send_key_search(self):
        """
        Click search box and send data to input search box.
        """

        header_page = HeaderPageAction(self.driver)

        logger.info('Connected device_data is successfully')

        header_page.wait_element_to_be_clickable_by_id(
            self.wait, header_page.locator['search_button']
        )
        assert header_page.assert_search_button() is not None, 'Search button element not found'

        header_page.click_search_button()
        logger.info('Click the search button')

        data = self.read_search_data()
        time.sleep(2)

        header_page.send_keys_search_input(data['search_input'])
        logger.info(f"Insert the word <{data['search_input']}> in the search box")

    def T332_check_search_result(self):
        """
        Checking the result of the search
        """

        landing_page = LandingPageAction(self.driver)
        data = self.read_search_data()

        if len(landing_page.find_search_result_list()) >= 1:

            for item in landing_page.find_search_result_list():
                if data['search_input'].lower() in item.text.lower():
                    logger.info(f'search result: {item.text.lower()}, data input is equal search result.')
                    break
                else:
                    logger.warning(f'search result: {item.text.lower()}, data input is not equal search result.')
                continue
        else:
            logger.error('Search result is empty.')
            assert False


    def read_search_data(self):
        return YAMLReader.data_reader(SEARCH_INPUT_DATA_FILE_PATH)
