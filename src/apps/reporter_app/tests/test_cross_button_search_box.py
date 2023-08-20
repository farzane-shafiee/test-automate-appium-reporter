from selenium.common import TimeoutException
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.header_page.header_page_action import HeaderPageAction
from src.config.test_config.base_test import BaseTest
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH


class TestCrossButtonSearchBox(BaseTest):

    def test_cross_button_search_box(self):
        """
        Click the cross button in Search box and close search box.
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

            header_page.click_cross_button_search_box()

            header_page.wait_visibility_of_element_located_by_xpath(
                self.wait, header_page.locator['assert_cross_button']
            )
            logger.info('cross button is clicked and clear search input')

            header_page.click_cross_button_search_box()

            header_page.wait_visibility_of_element_located_by_id(
                self.wait, header_page.locator['search_button']
            )
            logger.info('cross button is clicked and closed search box')

            self.mysql_manager.execute_saved_log_query()

        except Exception as e:
            logger.error(f'Assertion Error Cross Button {str(e)}')  # Log the assertion error message
            self.mysql_manager.execute_saved_log_query()
            assert False

        except TimeoutException as e:
            logger.error(f'Timeout Exception Cross Button: {str(e)}')
            self.mysql_manager.execute_saved_log_query()
            assert False

    def read_search_data(self):
        return YAMLReader.data_reader(SEARCH_INPUT_DATA_FILE_PATH)
