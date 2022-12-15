from tkinter import ttk, constants, StringVar, Text, WORD, INSERT

from entities.statistic import Statistic
from services.sentence_service import SentenceService
from services.statistic_calculator import StatisticCalculator
from services.statistic_service import statistic_service
from services.user_service import user_service

class TypingTestView:

    def __init__(self, root, handle_typing_test_finish_view, handle_main_menu_view):
        self._root = root
        self._handle_show_typing_test_finish_view = handle_typing_test_finish_view
        self._handle_back_to_menu_view = handle_main_menu_view

        self._sentence_service = None
        self._statistic_calculator = None 

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
        self._statistic_calculator = StatisticCalculator()

        self._initialize_title()
        self._initialize_back_to_main_menu()
        self._initialize_test_sentence()
        self._initialize_typing_form()
        self._initialize_statistics()

    def _initialize_title(self):

        title = ttk.Label(
            master = self._frame,
            text = "Write the following text:",
            font=('consolas', 15, "bold")
            )

        title.grid(column=1, row=0, columnspan=1, padx = 5, pady = 5)

    def _initialize_test_sentence(self):
        
        test_sentence = self._sentence_service.generate_sentence()

        label = ttk.Label(master = self._frame, text = test_sentence, font=('consolas', 13), wraplength=490)

        label.grid(column=1, row=1, columnspan=1, padx = 5, pady = 5, sticky = (constants.E, constants.W))

        self._sentence_label = label

    def _initialize_typing_form(self):

        typingform = ttk.Entry(master = self._frame, font=('arial', 13))
        typingform.grid(column = 1, row = 2, columnspan=1, padx = 5, pady = 5, sticky=(constants.E, constants.W))

        self._sentence_form = typingform

        typingform.bind("<KeyRelease>", self.evaluate_input)

        typingform.focus()

    def _initialize_back_to_main_menu(self):

        main_menu_button = ttk.Button(
            master = self._frame,
            text = "Back to Main Menu",
            command = self._handle_back_to_menu_view
        )

        main_menu_button.grid(column = 1, row = 3, padx = 5, pady = 5)

    def _initialize_statistics(self):

        self._accuracy = ttk.Label(master = self._frame, text = f'Accuracy: 100%', font =('consolas', 13))
        self._wpm = ttk.Label(master = self._frame, text = f'WPM: 0', font=('consolas', 13))
        self._time_taken = ttk.Label(master =self._frame, text = f'Time taken: 0s', font=('consolas', 13))

        self._accuracy.grid(column=1, columnspan=1, padx = 5, pady = 5)
        self._wpm.grid(column=1, columnspan=1, padx = 5, pady = 5)
        self._time_taken.grid(column=1, columnspan=1, padx = 5, pady = 5)

    def evaluate_input(self, event):
        sentence_label = self._sentence_label.cget('text')
        usr_input = self._sentence_form.get()

        if not self._running:
            self._running = True
            self._statistic_calculator.time_start()

        completed, color = self._sentence_service.evaluate(sentence_label, usr_input)
        self._sentence_form.config(foreground = color)

        if not completed:
            self.update_statistics()

        if completed:
            self._save_and_complete()
    
    def update_statistics(self):
        
        #Retrieve the current input and sentence
        usr_input = self._sentence_form.get()
        sentence_label = self._sentence_label.cget("text")

        #Update current statistics to statistic service
        self._statistic_calculator.calculate_statistics(sentence_label, usr_input)

        #Set statistic labels as corresponding statistic attributes
        self._accuracy.config(text = self._statistic_calculator.accuracy_string())
        self._wpm.config(text = self._statistic_calculator.wpm_string())
        self._time_taken.config(text = self._statistic_calculator.time_taken_string())

    def _save_and_complete(self):

        #Retrieve current statistics to local variables
        accuracy = self._statistic_calculator.accuracy
        wpm = self._statistic_calculator.wpm
        time_taken = self._statistic_calculator.time_taken

        #make a final statistic
        round_statistic = Statistic(username = user_service.get_current_user().username, accuracy = accuracy, wpm = wpm, time_taken = time_taken, total = 1, max_wpm = wpm, min_wpm = wpm)
        statistic_service.set_round_statistic(round_statistic)

        self._frame.after(1000, self._update_and_change_view)

    def _update_and_change_view(self):

        statistic_service.update_user_total_statistics()
        self._handle_show_typing_test_finish_view()

