from selenium.common import TimeoutException
from src.logs.logs_config import logger
from src.apps.reporter_app.page.report_page.reporter_page_action import ReporterPageAction
from src.config.test_config.conftest import test_search
# from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH


class TestReporter:

    def test_02_reporters(self, test_search):
        wait = test_search.wait

        try:
            reporter_page = ReporterPageAction(test_search.driver)
            test_search.searches()

            reporter_page.click_report_type_dropdown()

            reporter_page.click_bug_report_dropdown_button()
            logger.info('Click the Bug Report button in dropdown')

            reporter_page.wait_visibility_of_element_located_by_xpath(
                wait, reporter_page.locator['bug_report_dropdown_button']
            )
            assert reporter_page.assert_click_dropdown() is not None, 'Drop Down selected not found'
            logger.info('Bug Report dropdown asserted successfully')

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

            test_search.mysql_manager.execute_saved_log_query()

        except Exception as e:
            logger.error(f'Assertion Error {str(e)}')  # Log the assertion error message
            test_search.mysql_manager.execute_saved_log_query()
            assert False

        except TimeoutException as e:
            logger.error(f'Timeout Exception {str(e)}')
            test_search.mysql_manager.execute_saved_log_query()
            assert False

