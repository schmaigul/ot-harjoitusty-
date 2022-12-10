from database_connection import get_user_database_connection
from entities.user import User

class UserRepository:
    '''
    Class responsible for statistics-related database operations
    '''

    def __init__(self, connection):
        '''Class constructor

        Args:
            connection: Connection-object for the database
        '''

        self.connection = connection

    def create_user(self, user):
        '''Creates a new user to the database

        Args:
            user: User-object

        Returns:
            The same User-object in the parameters
        '''

        cursor = self.connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?);",
            (user.username, user.password)
        )

        self.connection.commit()

        return user

    def find_all_users(self):
        '''Finds all the users in the database and returns them in a list of User-objects

        Returns:
            A list of User-objects
        '''

        cursor = self.connection.cursor()

        rows = cursor.execute(
                "select * from users;"
            ).fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def find_user(self, username):
        '''Searches user on the user database based on username,
        returns User-object if username is found

        Args:
            username: username :D

        Returns: User-object if username is found
        '''

        cursor = self.connection.cursor()

        cursor.execute(
            "select * from users where username = ?;",
            (username,)
        )

        row = cursor.fetchone()

        return User(row["username"], row["password"]) if row else None

    def delete_all_users(self):
        '''Removes all users from the database
        '''
        cursor = self.connection.cursor()

        cursor.execute("delete from users;")

        self.connection.commit()

#This variable will be used by the application and services to avoid multiple
#instances of UserRepository
user_repository = UserRepository(get_user_database_connection())
