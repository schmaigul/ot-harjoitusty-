import re
import unicodedata

from essential_generators import DocumentGenerator

class SentenceService:
    '''Class responsible of generating and evaluating typing test sentences and user inputs.
    Generates sentences using essential_generators-library.
    '''

    def __init__(self):
        self._generator = DocumentGenerator()

    def text_cleaner(self, text):
        '''Removes punctuation and unwanted characters from a string,
        used to strip the generated sentence.

        Args:
            text: String, sentence to be cleaned

        Returns:
            String, cleaned text
        '''

        text = re.sub(r'--', ' ', text)
        text = re.sub(r'[\[].*?[\]]', '', text)
        text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
        text = text.replace('\n', ' ').replace('\r', ' ')
        text = ' '.join(text.split())

        #canonical normalization, decomposes unicode characters to ascii to make it writeable
        text = unicodedata.normalize("NFD", text)

        return text

    def generate_sentence(self):
        '''Generates a random sentence with essential_generators-library

        Returns:
            String, clean normalized text with >= 10 words
        '''

        sentence = self._generator.sentence()

        while len(sentence.split()) < 10:
            sentence += " "
            sentence += self._generator.sentence()
            sentence = self.text_cleaner(sentence)

        return sentence

    def evaluate(self, sentence_label, usr_input):
        '''Returns a color corresponding whether the user has written the sentence
        label correctly thus far.

        Args:
            sentence_label: String, sentence that the user input will be compared to
            usr_input: String, text that the user has written so far

        Returns: String, a color label corresponding to the evaluation between the two sentences,
        If user input does not match with the start of the sentence label, then return red
        If user has written everything correctly so far but is not finished, return black
        If user has written everything correctly and finished, return green
        '''

        completed = False
        color = None

        if not sentence_label.startswith(usr_input):
            color = 'red'
        else:
            color = 'black'
        if ((len(usr_input.split()) == len(sentence_label.split()))
                and (usr_input.split()[-1] == sentence_label.split()[-1])):
            color = 'green'
            completed = True

        return completed, color
