from selenium.common import TimeoutException
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.report_page.reporter_page_action import ReporterPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH
from src.config.test_config.conftest import test_search, test_reporter


class TestDeleteAttachment:

    def test_deleting_attached_file(self, test_search, test_reporter):
        """ Deleting attachment file in reporter page """

        wait = test_search.wait
        try:
            reporter_page = ReporterPageAction(test_search.driver)
            test_reporter.select_type_report(test_search)
            test_reporter.insert_attach(test_search)

            # Delete attached file
            logger.info('Deleting attach file test is running')
            reporter_page.click_attach_file_button()

            assert reporter_page.assert_file_attached() is not None, 'File not deleted'

            reporter_page.wait_visibility_of_element_located_by_xpath(
                wait, reporter_page.locator['assert_attach_file']
            )
            logger.info('Deleting attach file is successfully')

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