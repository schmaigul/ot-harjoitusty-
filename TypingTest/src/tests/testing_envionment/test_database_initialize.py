from tests.testing_envionment.test_database_connection import get_user_database_connection, get_statistics_database_connection

def drop_user_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()

def create_user_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')

    connection.commit()

def drop_statistics_tables(connection):

    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists statistics
    ''')

def create_statistics_tables(connection):

    cursor = connection.cursor()

    cursor.execute('''
        create table statistics (
            username text primary key,
            accuracy int,
            wpm int,
            time_taken int,
            total int,
            max_wpm int,
            min_wpm int
        );
    ''')

def initialize_user_database():
    connection_users = get_user_database_connection()

    drop_user_tables(connection_users)
    create_user_tables(connection_users)

def initialize_statistics_database():
    connection_statistics = get_statistics_database_connection()

    drop_statistics_tables(connection_statistics)
    create_statistics_tables(connection_statistics)

if __name__ == "__main__":
    initialize_user_database()
    initialize_statistics_database()