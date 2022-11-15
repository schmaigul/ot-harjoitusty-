from essential_generators import DocumentGenerator
from services.statistic_calculator import StatisticService

class SentenceService:
    def __init__(self):
        self._sentence = None
        self_input = None
        self._generator = DocumentGenerator()
        self._statistic_calc = StatisticService()

    def get_sentence(self):
        return self.sentence

    def set_sentence(self, sentence):
        self.sentence = sentence

    def generate_sentence(self):

        sentence = self._generator.sentence()

        while (len(sentence.split()) < 12):
            sentence += " "
            sentence += self._generator.sentence()

        return sentence

    def evaluate(self, sentence_label, input):
        completed = False

        if not sentence_label.cget('text').startswith(input.get()):
            input.config(foreground='red')
        else:
            input.config(foreground="black")
        if len(input.get().split()) == len(sentence_label.cget('text').split()) and input.get()[-1] == sentence_label.cget('text')[-1]:
            input.config(foreground = "green")
            completed = True

        return completed