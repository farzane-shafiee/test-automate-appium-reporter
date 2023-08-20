from selenium.common import TimeoutException
from src.apps.reporter_app.page.my_reports_page.my_reports_page_action import MyReportsPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH
from src.logs_config.test_logger import logger
from src.config.test_config.conftest import test_search, test_reporter


class TestMyReports:
    def test_my_reports(self, test_search, test_reporter):
        """ Show my reports page """

        wait = test_search.wait

        try:
            my_reporter_page = MyReportsPageAction(test_search.driver)
            test_reporter.select_type_report(test_search)
            test_reporter.insert_attach(test_search)
            test_reporter.insert_text_report(test_search)
            test_reporter.getting_os_date_time(test_search)

            logger.info('my reports page is opened')

            data = self.read_search_data()
            text_report_type = my_reporter_page.get_text_type_of_report()

            if text_report_type != "":  # Condition not empty my reports list
                len_my_report_list = len(my_reporter_page.my_reports_list())

                # Getting the number of items from the list of reports
                if len_my_report_list > 0 and data['report_type'] == text_report_type:
                    logger.info('my reports is saved and success.')

                    app_date_time = my_reporter_page.getting_date_time_my_report()
                    os_date_time = test_reporter.OS_DATE_TIME

                    # Test OS date/time with app date/time
                    if os_date_time == app_date_time:
                        logger.info('Date & Time of my report is recorded correctly')
                        assert True
                    else:
                        logger.error('Date & Time of my report is wrong')
            else:
                logger.error('my reports list is empty')
                assert False
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
