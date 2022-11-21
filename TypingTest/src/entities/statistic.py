
class Statistic:
    def __init__(self, time_taken = 0, wpm = 0, accuracy = 0):

        self.time_taken = time_taken
        self.wpm = wpm
        self.accuracy = accuracy

    def get_time_taken(self):
        return self.time_taken

    def get_wpm(self):
        return self.wpm

    def get_accuracy(self):
        return self.accuracy

    def time_taken_string(self, event = None):
        # pylint: disable=unused-argument
        return f'Time taken: {self.time_taken:.2f}s'

    def wpm_string(self, event = None):
        # pylint: disable=unused-argument
        return f'WPM: {self.wpm:.2f}'

    def accuracy_string(self, event = None):
        # pylint: disable=unused-argument
        return f'Accuracy: {int(self.accuracy)}%'
