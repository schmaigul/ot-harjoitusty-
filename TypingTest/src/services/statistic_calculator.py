import time

class StatisticService:
    def __init__(self):
        self._typos = 0
        self._start_time = 0

    def time_start(self):
        self._start_time = time.time()

    def calculate_elapsed_time(self):
        current_time = time.time()
        return current_time-self._start_time
    
    def calculate_words_per_minute(self, input):
        length = len(input.split())
        if (length == 1):
            return 0
        time_taken_in_seconds = self.calculate_elapsed_time()
        wpm = length/(time_taken_in_seconds)*60
        return wpm

    def calculate_accuracy(self, sentence_label, input):
        input_length = len(input)
        correct_so_far = sentence_label[:input_length]
        
        acc = len(set(input.split()) & set(correct_so_far.split()))
        
        if len(input.split()) == 0:
            return 0

        acc = acc/len(input.split())

        return acc*100
