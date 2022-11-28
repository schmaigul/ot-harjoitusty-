import unittest
from repositories.statistics_repository import statistics_repository
from repositories.user_repository import user_repository
from entities.statistic import Statistic

class TestStatisticRepository(unittest.TestCase):
    def setUp(self):
        statistics_repository.delete_all_statistics()

        self.statistic = Statistic("schmaigul", 20, 30, 50, 1)
        self.statistic2 = Statistic("schmaigul", 30, 50, 60, 200)
        self.statistic3 = Statistic("petteri", 10, 2, 3, 4)
    
    def test_find_all_empty(self):

        stats = statistics_repository.find_user_statistics("schmaigul")

        self.assertEqual(None, stats)

    def test_find_all_multiple(self):

        statistics_repository.insert_user_statistics(self.statistic)
        statistics_repository.insert_user_statistics(self.statistic3)

        stats = statistics_repository.find_all_statistics()

        self.assertEqual(2, len(stats))

    def test_set_new_user_statistic(self):

        new_stats = statistics_repository.update_user_statistics_old(self.statistic)
        self.assertEqual(self.statistic.wpm, new_stats.wpm)

    def test_update_statistic_old(self):

        statistics_repository.update_user_statistics_old(self.statistic)
        new_stats = statistics_repository.update_user_statistics_old(self.statistic2)

        self.assertEqual(self.statistic2.total, new_stats.total)

    def test_insert_statistic(self):
        statistics_repository.insert_user_statistics(self.statistic)
        stats = statistics_repository.find_user_statistics(self.statistic.username)

        self.assertEqual(self.statistic.accuracy, stats.accuracy)

    def test_update_statistic(self):
        statistics_repository.insert_user_statistics(self.statistic)
        statistics_repository.update_user_statistics(self.statistic2)

        stats = statistics_repository.find_user_statistics(self.statistic2.username)

        self.assertEqual(self.statistic2.accuracy, stats.accuracy)

    def test_delete_all_statistics(self):

        statistics_repository.insert_user_statistics(self.statistic)
        statistics_repository.insert_user_statistics(self.statistic3)

        statistics_repository.delete_all_statistics()

        stats = statistics_repository.find_all_statistics()

        self.assertEqual([], stats)