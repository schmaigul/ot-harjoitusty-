import unittest
from entities.user import User
from tests.testing_envionment.test_repositories import test_user_repository
from tests.testing_envionment.test_database_initialize import initialize_user_database

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_user_database()
        self.user_schmaigul = User(username="schmaigul", password="password")
        self.user_petteri = User(username="petteri", password="petsku")

    def test_create_user_entity(self):
        user = User("make", "matti")

        self.assertEqual(user.password, "matti")
        self.assertEqual(user.username, "make")

    def test_create(self):
        test_user_repository.create_user(self.user_petteri)
        all_users = test_user_repository.find_all_users()

        self.assertEqual(1, len(all_users))
        self.assertEqual(all_users[0].username, self.user_petteri.username)
        self.assertEqual(all_users[0].password, self.user_petteri.password)

    def test_find_user(self):
        test_user_repository.create_user(self.user_schmaigul)
        test_user_repository.create_user(self.user_petteri)

        user = test_user_repository.find_user(self.user_schmaigul.username)
        self.assertEqual("schmaigul", user.username)

        user2 = test_user_repository.find_user("petteri")
        self.assertEqual("petteri", user2.username)

    def test_delete_all(self):
        test_user_repository.create_user(self.user_schmaigul)
        test_user_repository.create_user(self.user_petteri)

        test_user_repository.delete_all_users()
        all_users = test_user_repository.find_all_users()
        
        self.assertEqual(0,len(all_users))