from selenium.common import StaleElementReferenceException
from src.apps.reporter_app.page.my_reports_page.my_reports_page_action import MyReportsPageAction
from src.logs_config.test_logger import logger
from src.apps.reporter_app.page.report_page.reporter_page_action import ReporterPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH


class TestReporter:

    def __init__(self):
        self.OS_DATE_TIME = None

    def select_type_report_drop_down(self, test_search):
        """ insert and saved report for app that selected """

        reporter_page = ReporterPageAction(test_search.driver)

        reporter_page.click_report_type_dropdown()
        logger.info('Drop down is selected')

        data = self.read_search_data()
        get_reports_type_list = reporter_page.get_reports_type_list()

        # find report type item in list of drop down
        for item in get_reports_type_list:
            try:
                if item.text.lower() == data['report_type']:
                    item.click()
                    logger.info('report type selected is successfully')
                else:
                    logger.info('Continue ...')

            except StaleElementReferenceException:
                # Handle the stale element exception
                logger.warning('StaleElementReferenceException occurred. Retrying...')
                get_reports_type_list = reporter_page.get_reports_type_list()
                continue

    def insert_attach(self, test_search):
        reporter_page = ReporterPageAction(test_search.driver)

        # Attach the image
        reporter_page.click_attach_file_button()

        reporter_page.wait_visibility_of_element_located_by_xpath(
            test_search.wait, reporter_page.locator['assert_file_manager']
        )
        assert reporter_page.assert_file_manager() is not None, 'File manager not found'
        logger.info('Click the attach file button asserted successfully')

        reporter_page.click_image_file()
        reporter_page.wait_visibility_of_element_located_by_xpath(
            test_search.wait, reporter_page.locator['assert_not_attach_file']
        )
        assert reporter_page.assert_file_not_attached() is not None, 'File not attached'
        logger.info('Select image asserted successfully')

    def insert_text_report(self, test_search):
        reporter_page = ReporterPageAction(test_search.driver)

        # Insert text into reporter input
        reporter_page.click_bug_report_text_input()
        data = self.read_search_data()
        reporter_page.insert_bug_report_text(data['description'])  # test for characters limit to be write
        logger.info('Insert text asserted successfully')

        reporter_page.click_send_report_button()
        logger.info('Click the send button asserted successfully')

    def getting_os_date_time(self, test_search):
        reporter_page = ReporterPageAction(test_search.driver)

        # Getting OS date & time
        self.OS_DATE_TIME = reporter_page.getting_os_date_time()

    def T344_T340_check_name_type_time_in_my_report_page(self, test_search):
        """
        Checking my report list
        """

        my_reporter_page = MyReportsPageAction(test_search.driver)
        data = self.read_search_data()

        if len(my_reporter_page.my_reports_list()) >= 1:
            logger.info('List is exist.')

            # Comparison type
            assert data['report_type'].lower() == my_reporter_page.get_text_type_of_report()
            logger.info('my reports "type" is comparison.')

            # Comparison OS date/time with app date/time
            app_date_time = my_reporter_page.getting_date_time_my_report()
            os_date_time = self.OS_DATE_TIME
            assert os_date_time == app_date_time, 'Date & Time of my report is wrong'
            logger.info('my reports "date/time" is comparison.')

            # Comparison name
            assert data['search_input'].lower() == my_reporter_page.get_text_name_of_report
            logger.info('my reports "name app" is comparison.')

        else:
            logger.error('Search result is empty.')
            assert False

    def read_search_data(self):
        return YAMLReader.data_reader(SEARCH_INPUT_DATA_FILE_PATH)