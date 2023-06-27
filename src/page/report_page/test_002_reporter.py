import time
from src.logs.logs_config import logger
from src.page.report_page.reporter_page_action import ReporterPageAction
from src.page.header_page.test_001_search import TestSearch


class TestReporter:

    wait = None

    def test_02_reporters(self):
        run_search_test = TestSearch()
        run_search_test.setup_class()  # Set up the test environment for search
        self.wait = run_search_test.wait

        reporter_page = ReporterPageAction(run_search_test.driver)
        run_search_test.test_01_searches()

        reporter_page.click_report_type_dropdown()

        reporter_page.click_bug_report_dropdown_button()
        logger.info('Click the Bug Report button in dropdown')

        reporter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, reporter_page.locator['bug_report_dropdown_button']
        )
        logger.info('Bug Report button asserted successfully')

        reporter_page.click_attach_file_button()

        reporter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, reporter_page.locator['assert_file_manager']
        )

        reporter_page.click_image_file()

        reporter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, reporter_page.locator['assert_not_attach_file']
        )

        reporter_page.click_bug_report_text_input()

        reporter_page.insert_bug_report_text('ERROR')
        time.sleep(2)

