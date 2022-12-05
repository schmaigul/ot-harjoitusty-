import unittest
import time
from services.statistic_calculator import StatisticCalculator

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistic_calc = StatisticCalculator()
        self.statistic_calc.time_start()
        time.sleep(3)

    def test_correct_elaped_time(self):
        self.assertEqual(3, int(self.statistic_calc.calculate_elapsed_time()))

    def test_correct_accuracy(self):
        input = "I do not know how to write a sentence properly"
        sentence_label = "I do not now how to write  a sentence properly"
        self.assertEqual(90, int(self.statistic_calc.calculate_accuracy(sentence_label, input)))

    def test_correct_wpm(self):
        input = "hehe hehe hehe"
        self.assertEqual(59, int(self.statistic_calc.calculate_words_per_minute(input)))

    def test_calculate_statistics(self):

        self.statistic_calc.calculate_statistics(
            "I do not know how to write a sentence properly",
            "I do not know how to write")

        self.assertEqual(100, self.statistic_calc.get_accuracy())

        
        