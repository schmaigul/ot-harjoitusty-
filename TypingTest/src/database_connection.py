import sqlite3
from config import USER_DATABASE_PATH
from config import STATISTICS_DATABASE_PATH


def get_user_database_connection():

    print(USER_DATABASE_PATH)
    connection = sqlite3.connect(USER_DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection

def get_statistics_database_connection():

    connection = sqlite3.connect(STATISTICS_DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection
