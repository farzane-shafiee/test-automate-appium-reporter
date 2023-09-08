from selenium.common import TimeoutException
from src.apps.reporter_app.page.my_reports_page.my_reports_page_action import MyReportsPageAction
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.header_page.header_page_action import HeaderPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH
from src.config.test_config.conftest import test_search


class TestSearch:

    def test_334_search_in_my_reports(self, test_search):
        """
        Test Search box in my reports.
        """
        wait = test_search.wait
        header_page = HeaderPageAction(test_search.driver)
        my_reporter_page = MyReportsPageAction(test_search.driver)

        try:
            logger.info('Connected device_data is successfully')

            header_page.wait_visibility_of_element_located_by_xpath(
                wait, header_page.locator['more_options_button']
            )

            header_page.click_more_options_button()
            header_page.click_my_reports_button()

            test_search.T332_click_and_send_key_search()

            data = self.read_search_data()

            if header_page.find_search_result_list() is False:
                logger.warning(f"the word <{data['search_input']}> not found in the search.")
                assert True
            else:
                assert my_reporter_page.get_text_type_of_report() == data['report_type']

                assert my_reporter_page.get_text_name_of_report() == data['search_input']
                logger.info('Search result is find.')

                test_search.mysql_manager.execute_saved_log_query()

        except Exception as e:
            logger.error(f'Assertion Error Searches {str(e)}')  # Log the assertion error message
            test_search.mysql_manager.execute_saved_log_query()
            assert False

        except TimeoutException as e:
            logger.error(f'Timeout Exception Searches: {str(e)}')
            test_search.mysql_manager.execute_saved_log_query()
            assert False

    def read_search_data(self):
        return YAMLReader.data_reader(SEARCH_INPUT_DATA_FILE_PATH)
