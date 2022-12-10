import unittest
from services.user_service import UserService
from services.statistic_service import StatisticService
from tests.testing_envionment.test_repositories import test_statistics_repository, test_user_repository

from services.user_service import IncorrectPasswordError, EmptyPasswordError, UserNotFoundError, UserExistError

from entities.user import User
from entities.statistic import Statistic

class TestStatisticService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(
            test_user_repository
        )
        self.statistic_service = StatisticService(
            test_statistics_repository,
            self.user_service
        )
        self.statistic_service.delete_all_statistics()
        self.user_service.delete_all_users()
        self.user1 = User("schmaigul", "123")
        self.user_service.create_user(self.user1.username, self.user1.password)
        self.user_service.login(self.user1.username, self.user1.password)

        self.statistic1 = Statistic("schmaigul", 11,12,13,69)
        self.statistic2 = Statistic("schmaigul", 13,14,15,70)
        self.statistic3 = Statistic("petteri", 1,2,3,100)

    def test_set_round_statistic(self):
        self.statistic_service.set_round_statistic(self.statistic1)

        self.assertEqual(self.statistic1.wpm, self.statistic_service.get_round_statistic().wpm)

    def test_update_user_statistic_new(self):

        self.statistic_service.set_round_statistic(self.statistic2)

        self.statistic_service.update_user_total_statistics()

        self.assertEqual("schmaigul", self.statistic_service.get_current_user_statistic().username)

    def test_update_user_statistic_existing(self):
        
        stat1 = Statistic("schmaigul", 100, 50, 10, 1, 50, 50)

        self.statistic_service.set_round_statistic(stat1)

        self.statistic_service.update_user_total_statistics()

        stat2 = Statistic("schmaigul", 90, 20, 5, 1, 20, 20)

        self.statistic_service.set_round_statistic(stat2)

        self.statistic_service.update_user_total_statistics()

        new_stat = self.statistic_service.get_current_user_statistic()

        self.assertEqual(95, int(new_stat.accuracy))
        self.assertEqual(35, int(new_stat.wpm))

    def test_total_increase(self):

        self.statistic_service.set_round_statistic(self.statistic2)

        self.statistic_service.update_user_total_statistics()

        new_total = self.statistic_service.get_current_user_statistic().total

        self.assertEqual(70, new_total)

    def test_invalid_login(self):

        self.user_service.logout()

        self.assertRaises(IncorrectPasswordError,
        lambda: self.user_service.login("schmaigul", "pieru")
        )

    def test_existing_username(self):

        self.user_service.logout()

        self.assertRaises(UserExistError,
        lambda: self.user_service.create_user("schmaigul", "pieru"))

    def test_empty_password(self):

        self.user_service.logout()

        self.assertRaises(EmptyPasswordError,
        lambda: self.user_service.create_user("pekkamatias", ""))

    def test_user_not_found(self):

        self.assertRaises(UserNotFoundError,
        lambda: self.user_service.login("pekkamartinoja", "pekkis"))

    def test_get_all_users(self):

        self.user_service.create_user("pekkamartinoja", "makkispekkis")

        self.assertEqual(2, len(self.user_service.get_all_users()))
