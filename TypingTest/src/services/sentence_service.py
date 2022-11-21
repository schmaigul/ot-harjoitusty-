from essential_generators import DocumentGenerator
from services.statistic_calculator import StatisticService

class SentenceService:
    def __init__(self):
        self._generator = DocumentGenerator()
        self._statistic_calc = StatisticService()

    def generate_sentence(self):

        sentence = self._generator.sentence()

        while len(sentence.split()) < 10:
            sentence += " "
            sentence += self._generator.sentence()

        return sentence

    def evaluate(self, sentence_label, usr_input):
        completed = False
        input_text = usr_input.get()
        ex_sentence = sentence_label.cget('text')

        if not ex_sentence.startswith(input_text):
            usr_input.config(foreground='red')

        else:
            usr_input.config(foreground="black")

        if ((len(input_text.split()) == len(ex_sentence.split()))
                and (input_text[-1] == ex_sentence[-1])):

            usr_input.config(foreground = "green")
            completed = True

        return completed
