import os
from dotenv import load_dotenv
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from src.db_connection_handler.db_handler import MySQLManager
from src.logs_config.test_logger import logger
from src.utils.process_data.data_handler import YAMLReader


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

        cls.driver.implicitly_wait(1)
        cls.wait = WebDriverWait(cls.driver, 20)

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
        return YAMLReader.data_reader("device_data/data_device.yml")

