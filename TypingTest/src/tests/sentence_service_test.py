import unittest

from services.sentence_service import SentenceService

class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentenceservice = SentenceService()

    def test_sentence_length(self):
        sentence = self.sentenceservice.generate_sentence()
        length = len(sentence.split())

        self.assertEqual(True, (length >= 10))

    def test_sentence_evaluate_wrong(self):
        
        sentence = "I dont know how to"
        example_sentence = "I dunno know how to write"
        completed, color = self.sentenceservice.evaluate(example_sentence, sentence)
        self.assertEqual('red', color)
        self.assertEqual(False, completed)

    def test_sentence_evaluate_not_finished(self):

        sentence = "I dont know"
        example_sentence = "I dont know how to write"
        completed, color = self.sentenceservice.evaluate(example_sentence, sentence)
        self.assertEqual('black', color)
        self.assertEqual(False, completed)

    def test_sentence_evaluate_finished(self):

        sentence = "I dont know how to write"
        example_sentence = "I dont know how to write"
        completed, color = self.sentenceservice.evaluate(example_sentence, sentence)
        self.assertEqual('green', color)
        self.assertEqual(True, completed)

    
        

