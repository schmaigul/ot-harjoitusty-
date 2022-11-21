from essential_generators import DocumentGenerator

class SentenceService:
    def __init__(self):
        self._generator = DocumentGenerator()

    def generate_sentence(self):

        sentence = self._generator.sentence()

        while len(sentence.split()) < 10:
            sentence += " "
            sentence += self._generator.sentence()

        return sentence

    def evaluate(self, sentence_label, usr_input):
        completed = False
        color = None

        if not sentence_label.startswith(usr_input):
            color = 'red'
        else:
            color = 'black'
        if ((len(usr_input.split()) == len(sentence_label.split()))
                and (usr_input[-1] == sentence_label[-1])):
            color = 'green'
            completed = True

        return completed, color
