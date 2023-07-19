from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def wait_visibility_of_element_located_by_id(wait, element):
        """
        Wait for the element to be visible by ID attribute
        :param wait: WebDriverWait
        :param element: Locator element
        :return: Time sleep
        """
        return wait.until(
            EC.visibility_of_element_located(
                (By.ID, element)
            )
        )

    @staticmethod
    def wait_visibility_of_element_located_by_xpath(wait, element):
        """
        Wait for the element to be visible by XPATH attribute
        :param wait: WebDriverWait
        :param element: Locator element
        :return: Time sleep
        """
        return wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, element)
            )
        )

    @staticmethod
    def wait_element_to_be_clickable_by_id(wait, element):
        """
        Wait for the element to be clickable by ID attribute
        :param wait: WebDriverWait
        :param element: Locator element
        :return: Time sleep
        """
        return wait.until(
            EC.element_to_be_clickable(
                (By.ID, element)
            )
        )

    @staticmethod
    def getting_os_date_time():
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H')
        return formatted_datetime
