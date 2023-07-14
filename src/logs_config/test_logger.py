import logging


logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
test_filehandler = logging.FileHandler(filename='logs_config/logs.log', mode='a')
test_formatter = logging.Formatter('%(asctime)s   -   %(funcName)s   -   %(levelname)s   -   %(message)s')
test_filehandler.setFormatter(test_formatter)
logger.addHandler(test_filehandler)
