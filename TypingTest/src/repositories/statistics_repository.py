from database_connection import get_statistics_database_connection
from entities.statistic import Statistic

def get_statistic_by_row(row):
    '''Returns a Statistics-object from a suitable sqlite3 row.

    Args: sqlite3 row

    Returns: Statistics-object or None if row is not found
    '''

    return Statistic(row['username'],
                    row['accuracy'],
                    row['wpm'],
                    row['time_taken'],
                    row['total'],
                    row['max_wpm'],
                    row['min_wpm']) if row else None

class StatisticsRepository:
    '''
    Class responsible for statistics-related database operations
    '''

    def __init__(self, connection):
        '''Class constructor.

        Args:
            connection: Connection-object for the database
        '''

        self.connection = connection

    def find_user_statistics(self, username):
        '''Returns user statistics

        Args:
            username: current users username

        Returns:
            Statistics-object if there is a statistic with the associated username
        '''

        cursor = self.connection.cursor()

        cursor.execute(
            "select * from statistics where username = ?;",
            (username,)
        )

        row = cursor.fetchone()

        return get_statistic_by_row(row)

    def find_all_statistics(self):
        '''Returns all statistics in the database

        Returns:
            A list of Statistic-objects
        '''
        cursor = self.connection.cursor()

        rows = cursor.execute(
                "select * from statistics"
            ).fetchall()

        return list(map(get_statistic_by_row, rows))

    def insert_user_statistics(self, statistic):
        '''Creates a new Statistic to the database

        Args:
            statistic: A Statisticc-object
        '''
        cursor = self.connection.cursor()

        cursor.execute('''INSERT INTO statistics
                    (username, accuracy, wpm, time_taken, total, max_wpm, min_wpm)
                    VALUES
                    (?, ? ,?, ?, ?, ?, ?);
                    ''',
                    (statistic.username,
                    statistic.accuracy,
                    statistic.wpm,
                    statistic.time_taken,
                    statistic.total,
                    statistic.max_wpm,
                    statistic.min_wpm,)
                    )

        self.connection.commit()

    def update_user_statistics(self, statistic):
        '''Updates a row in the database

        Args:
            statistic: Statistic-object
        '''
        cursor = self.connection.cursor()

        cursor.execute('''UPDATE statistics
                    SET accuracy = ?, wpm = ?, time_taken = ?, total = ?, max_wpm = ?, min_wpm = ? WHERE username = ?;
                    ''',
                    (statistic.accuracy,
                    statistic.wpm,
                    statistic.time_taken,
                    statistic.total,
                    statistic.max_wpm,
                    statistic.min_wpm,
                    statistic.username,)
                    )

        self.connection.commit()

    def delete_all_statistics(self):
        '''Removes all statistics from the database
        '''
        cursor = self.connection.cursor()

        cursor.execute("delete from statistics")

        self.connection.commit()


#This variable will be used by the application and services to avoid making
#multiple instances of StatisticsRepository
statistics_repository = StatisticsRepository(get_statistics_database_connection())
