
class Statistic:
    def __init__(self, username = None, accuracy = 0, wpm = 0, time_taken = 0, total = 0):
        self.username = username
        self.accuracy = accuracy
        self.wpm = wpm
        self.time_taken = time_taken
        self.total = total

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
        # pylint: disable=unused-argument
        return f'WPM: {self.wpm:.2f}'

    def accuracy_string(self):
        # pylint: disable=unused-argument
        return f'Accuracy: {int(self.accuracy)}%'
