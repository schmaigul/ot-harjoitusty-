import time
from entities.statistic import Statistic

class StatisticService(Statistic):
    def __init__(self):
        super().__init__()
        self._typos = 0
        self._start_time = 0

    def calculate_statistics(self, sentence_label, usr_input):

        self.time_taken = self.calculate_elapsed_time()
        self.wpm = self.calculate_words_per_minute(usr_input)
        self.accuracy = self.calculate_accuracy(sentence_label, usr_input)

    def time_start(self):
        self._start_time = time.time()

    def calculate_elapsed_time(self):
        current_time = time.time()
        return current_time-self._start_time

    def calculate_words_per_minute(self, usr_input):

        length = len(usr_input.split())

        if length == 1:
            return 0

        time_taken_in_seconds = self.calculate_elapsed_time()
        wpm = length/(time_taken_in_seconds)*60

        return wpm

    def calculate_accuracy(self, sentence_label, usr_input):

        input_length = len(usr_input)
        correct_so_far = sentence_label[:input_length]

        if len(usr_input.split()) == 0:
            return 0

        acc = len(set(usr_input.split()) & set(correct_so_far.split()))

        acc = acc/len(usr_input.split())

        return acc*100
