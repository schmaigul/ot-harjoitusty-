import unittest
import time
from services.statistic_calculator import StatisticService

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statisticservice = StatisticService()
        self.statisticservice.time_start()
        time.sleep(3)

    def test_correct_elaped_time(self):
        self.assertEqual(3, int(self.statisticservice.calculate_elapsed_time()))

    def test_correct_accuracy(self):
        input = "I do not know how to write a sentence properly"
        sentence_label = "I do not now how to write  a sentence properly"
        self.assertEqual(90, int(self.statisticservice.calculate_accuracy(sentence_label, input)))

    def test_correct_wpm(self):
        input = "hehe hehe hehe"
        self.assertEqual(59, int(self.statisticservice.calculate_words_per_minute(input)))