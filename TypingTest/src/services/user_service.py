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
    def __init__(self, user_repository = default_user_repository):

        self.user_repository = user_repository
        self.user = None

    def login(self, username, password):

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

user_service = UserService()
