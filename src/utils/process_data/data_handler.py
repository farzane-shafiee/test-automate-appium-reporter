from abc import ABC, abstractmethod
import yaml
import json


class DataReader(ABC):
    """Abstract class for reading data from a file"""

    @abstractmethod
    def data_reader(self, file_path):
        pass


class YAMLReader(DataReader):
    """Class for reading data from a YAML file"""

    @classmethod
    def data_reader(cls, file_path):
        with open(file_path) as file:
            data_device = yaml.safe_load(file)
            json_data = json.dumps(data_device)
            return json.loads(json_data)


class JSONReader(DataReader):
    """A class  for reading JSON data from  a file"""

    def data_reader(self, file_path):
        pass



