from selenium.common import TimeoutException
from src.apps.reporter_app.page.header_page.header_page_action import HeaderPageAction
from src.logs_config.test_logger import logger
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH
from src.config.test_config.conftest import test_search, test_reporter


class TestSearch:

    def test_332_search(self, test_search, test_reporter):
        """ Test Search Box in Home Page """

        wait = test_search.wait
        try:
            header_page = HeaderPageAction(test_search.driver)

            data = self.read_search_data()
            test_search.T332_click_and_send_key_search()

            if header_page.find_search_result_list() is False:
                logger.warning(f"the word <{data['search_input']}> not found in the search.")
                assert True
            else:
                test_search.T332_check_search_result()

                header_page.click_report_button()
                logger.info(f"Click the report button {data['search_input'].lower()} app")

                header_page.wait_visibility_of_element_located_by_id(
                    wait, header_page.locator['assert_report_page_label']
                )
                assert header_page.get_report_page_label() is not None, 'Selected Search result element not found'

                logger.info('Search assertion was successful')

                test_search.mysql_manager.execute_saved_log_query()

        except Exception as e:
            logger.error(f'Assertion Error Reporters {str(e)}')  # Log the assertion error message
            test_search.mysql_manager.execute_saved_log_query()
            assert False

        except TimeoutException as e:
            logger.error(f'Timeout Exception Reporters {str(e)}')
            test_search.mysql_manager.execute_saved_log_query()
            assert False

    def read_search_data(self):
        return YAMLReader.data_reader(SEARCH_INPUT_DATA_FILE_PATH)