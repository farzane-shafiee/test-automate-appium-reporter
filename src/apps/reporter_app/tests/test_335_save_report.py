from selenium.common import TimeoutException
from src.apps.reporter_app.page.landing_page.landing_page_action import LandingPageAction
from src.apps.reporter_app.page.my_reports_page.my_reports_page_action import MyReportsPageAction
from src.apps.reporter_app.page.report_page.reporter_page_action import ReporterPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH
from src.logs_config.test_logger import logger
from src.config.test_config.conftest import test_search, test_reporter


class TestSaveReports:
    def test_335_save_report(self, test_search, test_reporter):
        """ Save report and Show my reports page """

        try:
            my_reporter_page = MyReportsPageAction(test_search.driver)
            landing_page = LandingPageAction(test_search.driver)
            reporter_page = ReporterPageAction(test_search.driver)

            data = self.read_search_data()

            test_search.T332_click_and_send_key_search()
            test_search.T332_check_search_result()

            if landing_page.find_search_result_list() == "":
                logger.warning(f"the word <{data['search_input']}> not found in the search.")
                assert True
            else:
                landing_page.click_report_button()

                test_reporter.select_type_report_drop_down(test_search)
                test_reporter.insert_attach(test_search)

                test_reporter.insert_text_report(test_search)
                test_reporter.getting_os_date_time(test_search)  # Getting OS date time

                reporter_page.wait_visibility_of_element_located_by_id(
                    test_search.wait, reporter_page.locator['message_text']
                )

                reporter_page.click_success_send_report_message()
                logger.info('Click on the close button of success message')

                my_reporter_page.wait_visibility_of_element_located_by_xpath(
                    test_search.wait, my_reporter_page.locator['assert_my_reports_label']
                )
                text_report_page = my_reporter_page.get_text_my_report_page()

                assert text_report_page == "my reports"  # Condition show my reports page
                logger.info('my reports page is opened')

                # Condition not empty my reports list
                assert my_reporter_page.my_reports_list() != "", "My reports list is empty."

                test_search.mysql_manager.execute_saved_log_query()

        except Exception as e:
            logger.error(f'Assertion Error My Reports {str(e)}')  # Log the assertion error message
            test_search.mysql_manager.execute_saved_log_query()
            assert False

        except TimeoutException as e:
            logger.error(f'Timeout Exception My Reports: {str(e)}')
            test_search.mysql_manager.execute_saved_log_query()
            assert False

    def read_search_data(self):
        return YAMLReader.data_reader(SEARCH_INPUT_DATA_FILE_PATH)
