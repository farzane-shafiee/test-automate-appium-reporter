from src.logs.logs_config import logger
from src.apps.reporter_app.page.header_page.header_page_action import HeaderPageAction
from src.config.test_config.base_test import BaseTest


class TestSearch(BaseTest):

    def searches(self):
        """
        Search box test.
        """

        header_page = HeaderPageAction(self.driver)

        try:
            logger.info('Connected device_data is successfully')

            header_page.wait_element_to_be_clickable_by_id(
                self.wait, header_page.locator['search_button']
            )
            assert header_page.locator['search_button']
            header_page.click_search_button()
            logger.info('Click the search button')

            header_page.send_keys_search_input('clock')
            logger.info('Insert the word "clock" in the search box')

            header_page.wait_visibility_of_element_located_by_xpath(
                self.wait, header_page.locator['assert_element_clock']
            )

            header_page.click_report_button()
            logger.info('Click the report button Clock app')

            header_page.wait_visibility_of_element_located_by_xpath(
                self.wait, header_page.locator['assert_element_clock']
            )

            logger.info('Search assertion was successful')
            # time.sleep(3)
        except Exception as e:
            logger.warning(f'Failed to exception {e}')
            self.mysql_manager.execute_query1()
            assert False
