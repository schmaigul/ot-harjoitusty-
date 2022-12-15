import time
from entities.statistic import Statistic

class StatisticCalculator(Statistic):
    '''Class responsible for calculating real time statistics for typing test
    '''
    def __init__(self):
        super().__init__()
        self._typos = 0
        self._start_time = 0

    def calculate_statistics(self, sentence_label, usr_input):
        '''Updates all the statistics calculated during the typing test

        Args:
            sentence_label: String, label that user needs to write
            usr_input: String, text written by the user
        '''

        self.accuracy = self.calculate_accuracy(sentence_label, usr_input)
        self.time_taken = self.calculate_elapsed_time()
        self.wpm = self.calculate_words_per_minute(usr_input)

    def time_start(self):
        '''Starts to count time
        '''

        self._start_time = time.time()

    def calculate_elapsed_time(self):
        '''Returns the elapsed time since the typing test was started

        Returns:
            Float, time taken since calling time_start()
        '''

        current_time = time.time()
        return current_time-self._start_time

    def calculate_words_per_minute(self, usr_input):
        '''Returns user wpm

        Args:
            usr_input: text written by the user

        Returns:
            Float, words written per minute by the user
        '''

        length = len(usr_input.split())

        if length == 1:
            return 0

        time_taken_in_seconds = self.calculate_elapsed_time()
        wpm = length/(time_taken_in_seconds)*60

        return wpm

    def calculate_accuracy(self, sentence_label, usr_input):
        '''Calculates and return user accuracy vs the given sentence

        Args:
            sentence_label: String, label that user needs to write
            usr_input: String, text written by the user

        Returns:
            Float, user accuracy in percentages
        '''

        input_length = len(usr_input)
        correct_so_far = sentence_label[:input_length]

        if len(usr_input.split()) == 0:
            return 0

        #find the number of differing characters between the texts by using sets
        acc = len(set(usr_input.split()) & set(correct_so_far.split()))

        acc = acc/len(usr_input.split())

        return acc*100
