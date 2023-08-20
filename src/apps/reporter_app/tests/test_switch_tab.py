from selenium.common import TimeoutException
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.header_page.header_page_action import HeaderPageAction
from src.config.test_config.base_test import BaseTest
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH


class TestSwitchTab(BaseTest):

    def test_switch_tab(self):
        """
        switch tab Device and App action is tested
        """

        header_page = HeaderPageAction(self.driver)

        try:
            logger.info('Switch tab test is running')

            header_page.wait_element_to_be_clickable_by_id(
                self.wait, header_page.locator['home_page_title']
            )
            assert header_page.get_home_page_title() is not None, 'Home page not loaded'

            header_page.click_device_tab()
            header_page.click_app_tab()
            header_page.click_device_tab()
            logger.info('Switch tab test is successful')

            self.mysql_manager.execute_saved_log_query()

        except Exception as e:
            logger.error(f'Assertion Error Searches {str(e)}')  # Log the assertion error message
            self.mysql_manager.execute_saved_log_query()
            assert False

        except TimeoutException as e:
            logger.error(f'Timeout Exception Searches: {str(e)}')
            self.mysql_manager.execute_saved_log_query()
            assert False

    def read_search_data(self):
        return YAMLReader.data_reader(SEARCH_INPUT_DATA_FILE_PATH)
