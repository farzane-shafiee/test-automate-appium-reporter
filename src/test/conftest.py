import json
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, element):
        return self.driver.find_element(By.ID, element)

    @staticmethod
    def wait_visibility_of_element_located(wait, element):
        return wait.until(
            EC.visibility_of_element_located(
                (By.ID, element)
            )
        )

    @staticmethod
    def wait_element_to_be_clickable(wait, element):
        return wait.until(
            EC.visibility_of_element_located(
                (By.ID, element)
            )
        )


class BaseTest:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.read_data_device())
        cls.driver.implicitly_wait(30)
        cls.wait = WebDriverWait(cls.driver, 300)

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()

    @classmethod
    def read_data_device(cls):
        """
        Read data from YAML file and return a dictionary.
        """

        with open("src/device/data_device.yml") as file:
            data_device = yaml.safe_load(file)
            json_data = json.dumps(data_device)
            return json.loads(json_data)