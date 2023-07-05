from abc import ABC, abstractmethod


def singleton(class_):
    """A class decorator for a singleton class."""

    instances = {}

    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return wrapper


class AbstractDBManager(ABC):
    """ An abstract base class for database connections. """

    @abstractmethod
    def connect(self):
        """Establishes a database connection."""
        pass

    @abstractmethod
    def disconnect(self):
        """Closes the database connection."""
        pass


class QueryExecutionMixin:
    @abstractmethod
    def execute_query(self):
        pass