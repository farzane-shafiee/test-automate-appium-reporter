import json

import pytest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # def find_element_by_id(self, element):
    #     return self.driver.find_element(By.ID, element)

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


class BaseTest:
    driver = None
    wait = None

    @classmethod
    def setup_class(cls):
        """
        Remote and connect to device.
        """
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.read_data_device())
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def read_data_device(cls):
        """
        Read data from YAML file and return a Json.
        """

        with open("device/data_device.yml") as file:
            data_device = yaml.safe_load(file)
            json_data = json.dumps(data_device)
            return json.loads(json_data)


# @pytest.fixture()
# def search_button(driver):
#     driver.find_element(By.ID, locator['search_button']).click()
#     driver.find_element(By.ID, locator['search_input']).send_keys(search_input)
#
# @pytest.fixture(scope="session")
# def search(self, search_input):
#
#     self.wait_element_to_be_clickable_by_id(
#         self.wait, self.locator['search_button']
#     )
#
#
#     self.wait_visibility_of_element_located_by_xpath(
#         self.wait, self.locator['assert_element_clock']
#     )
#
#     self.driver.find_element(By.ID, self.locator['report_button']).click()
#
#     self.wait_visibility_of_element_located_by_xpath(
#         self.wait, self.locator['assert_element_clock']
#     )