from selenium.common import TimeoutException
from src.apps.reporter_app.page.landing_page.landing_page_action import LandingPageAction
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.report_page.reporter_page_action import ReporterPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH
from src.config.test_config.conftest import test_search, test_reporter


class TestDeleteAttachment:

    def test_353_deleting_and_show_attached_file(self, test_search, test_reporter):
        """ Deleting attachment file in reporter page """

        wait = test_search.wait
        try:
            reporter_page = ReporterPageAction(test_search.driver)
            landing_page = LandingPageAction(test_search.driver)

            data = self.read_search_data()
            test_search.T332_click_and_send_key_search()

            test_search.T332_check_search_result()

            if landing_page.find_search_result_list() == "":
                logger.warning(f"the word <{data['search_input']}> not found in the search.")
                assert True
            else:
                landing_page.click_report_button()
                test_reporter.insert_attach(test_search)

                # Show thumb file attached
                reporter_page.wait_visibility_of_element_located_by_id(
                    wait, reporter_page.locator['thumb_file']
                )
                logger.info('Show attach file thumb is successfully')

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