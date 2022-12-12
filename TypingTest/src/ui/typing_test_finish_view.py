from tkinter import ttk, constants

from services.statistic_service import statistic_service

class TypingTestFinishView:
    def __init__(self, root, handle_new_typing_test_view, handle_main_menu_view):

        self._root = root
        self._handle_new_typing_test_view = handle_new_typing_test_view
        self._handle_main_menu_view = handle_main_menu_view

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._root.geometry("300x270")
        self._frame = ttk.Frame(master = self._root)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        self._initialize_header()
        self._initialize_statistics()
        self._initialize_new_typing_test_button()
        self._initialize_main_menu_button()

    def _initialize_header(self):

        title = ttk.Label(
            master = self._frame,
            text = "Well done!",
            font = ('consolas', 12, "bold")
        )

        title.grid(column = 0, row = 0, padx = 5, pady = 5)


    def _initialize_statistics(self):

        stat = statistic_service.get_round_statistic()

        accuracy = ttk.Label(master = self._frame, text = stat.accuracy_string(), font =('consolas', 12))
        wpm = ttk.Label(master = self._frame, text = stat.wpm_string(), font=('consolas', 12))
        time_taken = ttk.Label(master =self._frame, text = stat.time_taken_string(), font=('consolas', 12))

        wpm.grid(column=0, row = 1, padx = 5, pady = 5)
        time_taken.grid(column=0, row = 2, padx = 5, pady = 5)
        accuracy.grid(column=0, row = 3, padx = 5, pady = 5)


    def _initialize_new_typing_test_button(self):
        
        typing_test_button = ttk.Button(
            master = self._frame,
            text = "New typing test",
            command = self._handle_new_typing_test_view
        )

        typing_test_button.grid(column = 0, row = 4, padx = 5, pady = 5)

    def _initialize_main_menu_button(self):
        
        main_menu_button = ttk.Button(
            master = self._frame,
            text = "Main menu",
            command = self._handle_main_menu_view
        )

        main_menu_button.grid(column = 0, row = 5, padx = 5, pady = 5)
