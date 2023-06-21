import time
import pytest

from src.logs.logs_config import logger
from src.tests.conftest import BaseTest
from src.page.report_page.reporter_page import ReporterPage


class TestReporter(BaseTest):

    def test_02_reporters(self):

        reporter_page = ReporterPage(self.driver)

        logger.info('Connected device is successfully')

        reporter_page.wait_element_to_be_clickable_by_id(
            self.wait, reporter_page.locator['report_button']
        )

        reporter_page.click_report_button()
        logger.info('Click the report button')

        reporter_page.wait_visibility_of_element_located_by_xpath(
            self.wait, reporter_page.locator['assert_element']
        )
        logger.info('Report assertion was successfully')

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


