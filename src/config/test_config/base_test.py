import json
import os
from dotenv import load_dotenv
from appium import webdriver
import yaml
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.common.exceptions import ConnectionRefusedError
from src.db_connection_handler.db_handler import MySQLManager
from src.logs.logs_config import logger


class BaseTest:
    driver = None
    wait = None
    mysql_manager = None

    @classmethod
    def setup_class(cls):
        """
        Remote and connect to device_data.
        """
        load_dotenv()
        cls.initialize_mysql_manager()

        try:
            cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.read_data_device())
        except Exception as e:
            logger.warning(f"Error connecting to:{e}")
            assert False
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    # @classmethod
    # def teardown_class(cls):
    #     cls.mysql_manager.close_connection()

    @classmethod
    def initialize_mysql_manager(cls):
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_port = os.environ.get('DB_PORT')
        db_database = os.environ.get('DB_DATABASE')

        # Check if environment variables are not None
        assert db_host is not None, 'DB_HOST is not set'
        assert db_user is not None, 'DB_USER is not set'
        assert db_password is not None, 'DB_PASSWORD is not set'
        assert db_port is not None, 'DB_PORT is not set'
        assert db_database is not None, 'DB_DATABASE is not set'

        # Connect to Mysql
        cls.mysql_manager = MySQLManager(
            host=db_host,
            user=db_user,
            password=db_password,
            port=int(db_port),
            database=db_database,
        )
        cls.mysql_manager.connect()
        
    @classmethod
    def read_data_device(cls):
        """
        Read data from YAML file and return a Json.
        """

        with open("device_data/data_device.yml") as file:
            data_device = yaml.safe_load(file)
            json_data = json.dumps(data_device)
            return json.loads(json_data)