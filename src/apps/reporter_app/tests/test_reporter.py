import time
from src.logs.logs_config import logger
from src.apps.reporter_app.page.report_page.reporter_page_action import ReporterPageAction
from src.config.test_config.conftest import test_search


class TestReporter:

    def test_02_reporters(self, test_search):
        wait = test_search.wait

        reporter_page = ReporterPageAction(test_search.driver)
        test_search.test_01_searches()

        reporter_page.click_report_type_dropdown()

        reporter_page.click_bug_report_dropdown_button()
        logger.info('Click the Bug Report button in dropdown')

        reporter_page.wait_visibility_of_element_located_by_xpath(
            wait, reporter_page.locator['bug_report_dropdown_button']
        )
        logger.info('Bug Report button asserted successfully')

        reporter_page.click_attach_file_button()

        reporter_page.wait_visibility_of_element_located_by_xpath(
            wait, reporter_page.locator['assert_file_manager']
        )

        reporter_page.click_image_file()

        reporter_page.wait_visibility_of_element_located_by_xpath(
            wait, reporter_page.locator['assert_not_attach_file']
        )

        reporter_page.click_bug_report_text_input()

        reporter_page.insert_bug_report_text('ERROR')
        time.sleep(2)

