class Statistic:
    '''Class that represents users typing test statistics.

    Attributes:
        username: String,
        accuracy: Float, accuracy of a the tests
        wpm: Float, words per minute
        time_taken: Float, total time taken for the tests
        total: Integer, users total number of typing tests
        max_wpm: Float, maximum words per minute
        min_wpm: Float, minumum words per minute
    '''

    def __init__(self, username = None,
                accuracy = 0, wpm = 0,
                time_taken = 0, total = 0,
                max_wpm = 0, min_wpm = 0):

        self.username = username
        self.accuracy = accuracy
        self.wpm = wpm
        self.time_taken = time_taken
        self.total = total
        self.max_wpm = max_wpm
        self.min_wpm = min_wpm

    def get_time_taken(self):
        return self.time_taken

    def get_wpm(self):
        return self.wpm

    def get_accuracy(self):
        return self.accuracy

    def get_total(self):
        return self.total

    def time_taken_string(self):
        return f'Time taken: {self.time_taken:.2f}s'

    def wpm_string(self):
        return f'WPM: {self.wpm:.2f}'

    def accuracy_string(self):
        return f'Accuracy: {int(self.accuracy)}%'

    def total_string(self):
        return f'Total games played: {self.total}'

    def max_wpm_string(self):
        return f'Fastest wpm: {self.max_wpm:.2f}'

    def min_wpm_string(self):
        return f'Slowest wpm: {self.min_wpm:.2f}'
