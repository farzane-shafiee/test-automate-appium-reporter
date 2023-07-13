from selenium.common import TimeoutException
from src.logs.logs_config import logger
from src.apps.reporter_app.page.header_page.header_page_action import HeaderPageAction
from src.config.test_config.base_test import BaseTest
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH


class TestSearch(BaseTest):

    def searches(self):
        """
        Search box test.
        """

        header_page = HeaderPageAction(self.driver)

        try:
            logger.info('Connected device_data is successfully')

            header_page.wait_element_to_be_clickable_by_id(
                self.wait, header_page.locator['search_button']
            )
            assert header_page.assert_search_button() is not None, 'Search button element not found'

            header_page.click_search_button()
            logger.info('Click the search button')

            data = self.read_search_data()

            header_page.send_keys_search_input(data['search_input'])
            logger.info(f"Insert the word <{data['search_input']}> in the search box")

            if len(header_page.find_search_result_list()) >= 1:
                for items in header_page.find_search_result_list():
                    if data['search_input'].lower() in items.text.lower():
                        logger.info('Search result is find.')
                        assert True
                    else:
                        logger.error(f'search result: {items.text.lower()}, data input is not equal search result.')
                        assert False
            else:
                logger.error('Search result is empty.')
                assert False

            header_page.wait_visibility_of_element_located_by_xpath(
                self.wait, header_page.locator['assert_search_result']
            )

            header_page.click_report_button()
            logger.info('Click the report button Clock app')

            header_page.wait_visibility_of_element_located_by_xpath(
                self.wait, header_page.locator['assert_search_result']
            )
            assert header_page.assert_search_result() is not None, 'Selected Search result element not found'

            logger.info('Search assertion was successful')

        except Exception as e:
            logger.error(f'Assertion Error {str(e)}')  # Log the assertion error message
            self.mysql_manager.execute_saved_log_query()
            assert False

        except TimeoutException as e:
            logger.error(f'Timeout Exception: {str(e)}')
            self.mysql_manager.execute_saved_log_query()
            assert False

    def read_search_data(self):
        return YAMLReader.data_reader(SEARCH_INPUT_DATA_FILE_PATH)
