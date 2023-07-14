from selenium.common import TimeoutException, StaleElementReferenceException
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.report_page.reporter_page_action import ReporterPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH


class TestReporter:

    def reporters(self, test_search):
        """ insert and saved report for app that selected """

        wait = test_search.wait

        try:
            reporter_page = ReporterPageAction(test_search.driver)
            test_search.searches()

            reporter_page.click_report_type_dropdown()
            logger.info('Drop down is selected')

            data = self.read_search_data()
            get_reports_type_list = reporter_page.get_reports_type_list()
            # find report type item in list of drop down
            for item in get_reports_type_list:
                try:
                    if item.text == data['report_type']:
                        item.click()
                        logger.info('report type selected is successfully')
                    else:
                        logger.info('Continue ...')

                except StaleElementReferenceException:
                    # Handle the stale element exception
                    logger.warning('StaleElementReferenceException occurred. Retrying...')
                    get_reports_type_list = reporter_page.get_reports_type_list()
                    continue

            reporter_page.click_attach_file_button()

            reporter_page.wait_visibility_of_element_located_by_xpath(
                wait, reporter_page.locator['assert_file_manager']
            )
            assert reporter_page.assert_file_manager() is not None, 'File manager not found'
            logger.info('Click the attach file button asserted successfully')

            reporter_page.click_image_file()

            reporter_page.wait_visibility_of_element_located_by_xpath(
                wait, reporter_page.locator['assert_not_attach_file']
            )
            assert reporter_page.assert_file_attached() is not None, 'File not attached'
            logger.info('Select image asserted successfully')

            reporter_page.click_bug_report_text_input()

            data = test_search.read_search_data()

            reporter_page.insert_bug_report_text(data['description'])
            logger.info('Insert text asserted successfully')

            reporter_page.click_send_report_button()
            logger.info('Click the send button asserted successfully')

            reporter_page.wait_visibility_of_element_located_by_id(

                wait, reporter_page.locator['message_text']
            )
            reporter_page.click_success_send_report_message()
            logger.info('Click on the close button of success message')

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