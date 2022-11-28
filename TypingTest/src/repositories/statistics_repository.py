from database_connection import get_statistics_database_connection
from entities.statistic import Statistic

def get_statistic_by_row(row):
    return Statistic(row['username'],
                    row['accuracy'],
                    row['wpm'],
                    row['time_taken'],
                    row['total']) if row else None

class StatisticsRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_user_statistics(self, username):
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from statistics where username = ?;",
            (username,)
        )

        row = cursor.fetchone()

        return get_statistic_by_row(row)

    def find_all_statistics(self):
        cursor = self.connection.cursor()

        rows = cursor.execute(
                "select * from statistics"
            ).fetchall()

        return list(map(get_statistic_by_row, rows))

    def insert_user_statistics(self, statistic):
        cursor = self.connection.cursor()

        cursor.execute('''INSERT INTO statistics
                    (username, accuracy, wpm, time_taken, total)
                    VALUES
                    (?, ? ,?, ?, ?);
                    ''',
                    (statistic.username,
                    statistic.accuracy,
                    statistic.wpm,
                    statistic.time_taken,
                    statistic.total,)
                    )

        self.connection.commit()

    def update_user_statistics(self, statistic):
        cursor = self.connection.cursor()

        cursor.execute('''UPDATE statistics
                    SET accuracy = ?, wpm = ?, time_taken = ?, total = ? WHERE username = ?;
                    ''',
                    (statistic.accuracy,
                    statistic.wpm,
                    statistic.time_taken,
                    statistic.total,
                    statistic.username,)
                    )

        self.connection.commit()

    def update_user_statistics_old(self, statistic):

        cursor = self.connection.cursor()

        current_stats = self.find_user_statistics(statistic.username)

        if current_stats is None:
            cursor.execute('''INSERT INTO statistics
                        (username, accuracy, wpm, time_taken, total) 
                        VALUES (?, ? ,?, ?, ?);''',
                        (statistic.username,
                        statistic.accuracy,
                        statistic.wpm,
                        statistic.time_taken,
                        statistic.total,)
                        )
        else:
            cursor.execute('''UPDATE statistics
                        SET accuracy = ?, wpm = ?, time_taken = ?, total = ?
                        WHERE username = ?;''',
                        (statistic.accuracy,
                        statistic.wpm,
                        statistic.time_taken,
                        statistic.total,
                        statistic.username,)
                        )

        self.connection.commit()

        return self.find_user_statistics(statistic.username)

    def delete_all_statistics(self):

        cursor = self.connection.cursor()

        cursor.execute("delete from statistics")

        self.connection.commit()

statistics_repository = StatisticsRepository(get_statistics_database_connection())
