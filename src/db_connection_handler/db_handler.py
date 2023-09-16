import mysql.connector
from src.db_connection_handler.db_abstract import (
    singleton,
    AbstractDBManager,
    QueryExecutionMixin
)


@singleton
class MySQLManager(AbstractDBManager, QueryExecutionMixin):
    """A base class for mysql database connection."""

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,

        )
        return self.connection

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_saved_log_query(self):
        if not self.connection:
            raise Exception("Not connected to the database.")
        cursor = self.connection.cursor()

        log_file = open('src/logs_config/logs.log', 'r')
        for values in log_file:
            query = "INSERT INTO reporter_logs (logs) VALUES (%s)"
            cursor.execute(query, (values,))
        self.connection.commit()
        return cursor
