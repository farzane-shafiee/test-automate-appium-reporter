from selenium.common import TimeoutException
from src.apps.reporter_app.page.landing_page.landing_page_action import LandingPageAction
from src.apps.reporter_app.page.report_page.reporter_page_action import ReporterPageAction
from src.utils.process_data.data_handler import YAMLReader
from src.config.settings.base import SEARCH_INPUT_DATA_FILE_PATH
from src.logs_config.test_logger import logger
from src.config.test_config.conftest import test_search, test_reporter


class TestValidateCharacters:
    def test_357_validate_characters(self, test_search, test_reporter):
        """ Save report and Show my reports page """

        try:
            landing_page = LandingPageAction(test_search.driver)
            reporter_page = ReporterPageAction(test_search.driver)

            landing_page.click_report_button()
            logger.info(f"Click the report button on app")

            reporter_page.wait_visibility_of_element_located_by_xpath(
                test_search.wait, reporter_page.locator['assert_element']
            )
            assert reporter_page.assert_text() is not None, 'Selected Search result element not found'

            test_reporter.select_type_report_drop_down(test_search)  # open the drop/down

            test_reporter.insert_text_report(test_search)  # insert the text

            count_characters = reporter_page.get_count_character()  # get the number of characters
            assert count_characters == 1000, "Validation Error Count Characters"

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
