import unittest
from services.statistic_service import statistic_service
from services.user_service import user_service

from entities.user import User
from entities.statistic import Statistic

class TestStatisticService(unittest.TestCase):
    def setUp(self):
        statistic_service.delete_all_statistics()
        self.user1 = User("schmaigul", "123")
        user_service.create_user(self.user1.username, self.user1.password)
        user_service.login(self.user1.username, self.user1.password)

        self.statistic1 = Statistic("schmaigul", 11,12,13,69)
        self.statistic2 = Statistic("schmaigul", 13,14,15,70)
        self.statistic3 = Statistic("petteri", 1,2,3,4,100)

    def test_set_round_statistic(self):
        statistic_service.set_round_statistic(self.statistic1)

        self.assertEqual(self.statistic1.wpm, statistic_service.get_round_statistic())

    def test_update_user_statistic_new(self):

        statistic_service.update_user_total_statistics(self.statistic1)
        statistic_service.get_current_user_statistic()
