from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserNotFoundError(Exception):
    pass

class UserExistError(Exception):
    pass

class IncorrectPasswordError(Exception):
    pass

class EmptyPasswordError(Exception):
    pass

class UserService:
    '''Class responsible for handling user-related operations
    '''

    def __init__(self, user_repository = default_user_repository):
        '''Constructor for the class

        Args:
            user_repository: UserRepository-object to handle the database operations
        '''

        self.user_repository = user_repository
        self.user = None

    def login(self, username, password):
        '''Logs in the user based on username and password if the credentials are correct

        Args:
            username: String, user inputted username
            password: String, user inputted password

        Returns:
            User-object corresponding to the logged in user

        Raises:
            UserNotFoundError
            IncorrectPasswordError
        '''

        user = self.user_repository.find_user(username)

        if not user:
            raise UserNotFoundError("Invalid username")
        if user.password != password:
            raise IncorrectPasswordError("Invalid password")

        self.user = user

        return user

    def logout(self):
        self.user = None

    def create_user(self, username, password):
        '''Creates a new user to the database if the credentials are legal

        Args:
            username: String, user inputted username
            password: String, user inputted password

        Returns:
            User-object of the newly created user

        Raises:
            UserExistsError
            EmptyPasswordError
        '''

        existing_user = self.user_repository.find_user(username)

        if existing_user:
            raise UserExistError("This username is taken")
        if len(password) == 0:
            raise EmptyPasswordError("Password cannot be empty")

        user = self.user_repository.create_user(User(username, password))

        return user

    def get_all_users(self):
        return self.user_repository.find_all_users()

    def get_current_user(self):
        return self.user

    def delete_all_users(self):
        self.user_repository.delete_all_users()

#This variable will be used by the application and services to avoid making multiple
#instances of UserService
user_service = UserService()
