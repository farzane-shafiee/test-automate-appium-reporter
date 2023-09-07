from selenium.common import TimeoutException
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.my_reports_page.my_reports_page_action import MyReportsPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH
from src.config.test_config.conftest import test_search, test_reporter


class TestCorrectnessOfReportedText:

    def test_Correctness_of_the_reported_text(self, test_search, test_reporter):
        """ Deleting attachment file in reporter page """

        wait = test_search.wait
        try:
            my_reporter_page = MyReportsPageAction(test_search.driver)

            test_search.searches()

            my_reporter_page.wait_visibility_of_element_located_by_id(
                wait, my_reporter_page.locator['dialog_text_frame_layout']
            )

            logger.info('Correctness of the reported text is successfully')

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