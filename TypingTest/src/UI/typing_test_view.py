from tkinter import ttk, constants, StringVar, Text, WORD, INSERT

from entities.statistic import Statistic
from services.sentence_service import SentenceService
from services.statistic_calculator import StatisticService

class TypingTestView:

    def __init__(self, root, handle_typing_test_finish_view):
        self._root = root
        self._handle_show_typing_test_finish_view = handle_typing_test_finish_view

        self._sentence_service = None
        self._statistics_service = None 

        self._frame = None
        self._running = False
        self._sentence_label = None
        self._sentence_form = None

        self._wpm = None
        self._time_taken = None
        self._accuracy = None
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        
        self._root.geometry("500x400")
        self._frame = ttk.Frame(master = self._root)
        self._frame.option_add("*Label.Font", "consolas 30")
        self._frame.option_add("*Button.Font", "consolas 30")

        self._sentence_service = SentenceService()
        self._statistics_service = StatisticService()

        self._initialize_title()
        self._initialize_test_sentence()
        self._initialize_typing_form()
        self._initialize_statistics()

    def _initialize_title(self):

        title = ttk.Label(
            master = self._frame,
            text = "Write the following text:", font=('consolas', 12, "bold"))

        title.grid(column=1, row=0, columnspan=1, padx = 5, pady = 5)


    def _initialize_test_sentence(self):
        
        test_sentence = self._sentence_service.generate_sentence()

        label = ttk.Label(master = self._frame, text = test_sentence, font=('consolas', 13), wraplength=500)

        label.grid(column=1, row=1, columnspan=1, padx = 5, pady = 5, sticky = (constants.E, constants.W))

        self._sentence_label = label

    def _initialize_typing_form(self):
        

        typingform = ttk.Entry(master = self._frame, font=('arial', 13))
        typingform.grid(column = 1, row = 2, columnspan=1, padx = 5, pady = 5, sticky=(constants.E, constants.W))

        self._sentence_form = typingform

        typingform.bind("<KeyRelease>", self.evaluate_input)

        typingform.focus()

    def _initialize_statistics(self):
        
        self._wpm = ttk.Label(master = self._frame, text = f'WPM: 0', font=('consolas', 12))
        self._time_taken = ttk.Label(master =self._frame, text = f'Time taken: 0s', font=('consolas', 12))
        self._accuracy = ttk.Label(master = self._frame, text = f'Accuracy: 100%', font =('consolas', 12))

        self._wpm.grid(column=1, columnspan=1, padx = 5, pady = 5)
        self._time_taken.grid(column=1, columnspan=1, padx = 5, pady = 5)
        self._accuracy.grid(column=1, columnspan=1, padx = 5, pady = 5)

    def evaluate_input(self, event):
        if not self._running:
            self._running = True
            self._statistics_service.time_start()

        completed, color = self._sentence_service.evaluate(self._sentence_label.cget('text'), self._sentence_form.get())
        self._sentence_form.config(foreground = color)

        if not completed:
            self.update_statistics()
        
        #If the text is finished, change view to statistics
        if completed:
            self._frame.after(1000, self.save_and_complete)
    
    def update_statistics(self):

        input = self._sentence_form.get()
        sentence_label = self._sentence_label.cget("text")

        self._statistics_service.calculate_statistics(sentence_label, input)

        self._wpm.config(text = self._statistics_service.wpm_string())
        self._time_taken.config(text = self._statistics_service.time_taken_string())
        self._accuracy.config(text = self._statistics_service.accuracy_string())

    def save_and_complete(self):

        input = self._sentence_form.get()
        sentence_label = self._sentence_label.cget("text")
        
        time_taken = self._statistics_service.calculate_elapsed_time()
        wpm = self._statistics_service.calculate_words_per_minute(input)
        accuracy = self._statistics_service.calculate_accuracy(sentence_label, input)

        final_statistic = Statistic(time_taken, wpm, accuracy)
        
        self._handle_show_typing_test_finish_view(final_statistic)


