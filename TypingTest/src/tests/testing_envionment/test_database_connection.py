import sqlite3
from tests.testing_envionment.testconf import TEST_USER_DATABASE_PATH, TEST_STATISTICS_DATABASE_PATH

def get_user_database_connection():

    connection = sqlite3.connect(TEST_USER_DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection

def get_statistics_database_connection():
    
    connection = sqlite3.connect(TEST_STATISTICS_DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection
