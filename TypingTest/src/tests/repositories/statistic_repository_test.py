import unittest
from entities.statistic import Statistic
from tests.testing_envionment.test_repositories import test_statistics_repository
from tests.testing_envionment.test_database_initialize import initialize_statistics_database


class TestStatisticRepository(unittest.TestCase):
    def setUp(self):
        initialize_statistics_database()
        self.statistic = Statistic("schmaigul", 20, 30, 50, 1)
        self.statistic2 = Statistic("schmaigul", 30, 50, 60, 200)
        self.statistic3 = Statistic("petteri", 10, 2, 3, 4)
    
    def test_find_all_empty(self):

        stats = test_statistics_repository.find_user_statistics("schmaigul")

        self.assertEqual(None, stats)

    def test_find_all_multiple(self):

        test_statistics_repository.insert_user_statistics(self.statistic)
        test_statistics_repository.insert_user_statistics(self.statistic3)

        stats = test_statistics_repository.find_all_statistics()

        self.assertEqual(2, len(stats))

    def test_insert_statistic(self):
        test_statistics_repository.insert_user_statistics(self.statistic)
        stats = test_statistics_repository.find_user_statistics(self.statistic.username)

        self.assertEqual(self.statistic.accuracy, stats.accuracy)

    def test_update_statistic(self):
        test_statistics_repository.insert_user_statistics(self.statistic)
        test_statistics_repository.update_user_statistics(self.statistic2)

        stats = test_statistics_repository.find_user_statistics(self.statistic2.username)

        self.assertEqual(self.statistic2.accuracy, stats.accuracy)

    def test_delete_all_statistics(self):

        test_statistics_repository.insert_user_statistics(self.statistic)
        test_statistics_repository.insert_user_statistics(self.statistic3)

        test_statistics_repository.delete_all_statistics()

        stats = test_statistics_repository.find_all_statistics()

        self.assertEqual([], stats)
