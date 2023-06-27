import json
from appium import webdriver
import yaml
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest:
    driver = None
    wait = None

    @classmethod
    def setup_class(cls):
        """
        Remote and connect to device_data.
        """
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.read_data_device())
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.close_app()

    @classmethod
    def read_data_device(cls):
        """
        Read data from YAML file and return a Json.
        """

        with open("device_data/data_device.yml") as file:
            data_device = yaml.safe_load(file)
            json_data = json.dumps(data_device)
            return json.loads(json_data)