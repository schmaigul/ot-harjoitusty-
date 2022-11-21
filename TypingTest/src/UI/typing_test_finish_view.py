from tkinter import ttk, constants

class TypingTestFinishView:
    def __init__(self, root, handle_new_typing_test_view, handle_main_menu_view, statistic):

        self._root = root
        self._handle_new_typing_test_view = handle_new_typing_test_view
        self._handle_main_menu_view = handle_main_menu_view

        self._statistic = statistic
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._frame = ttk.Frame(master = self._root)

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

        title.grid(column = 1, row = 0, columnspan = 1, padx = 5, pady = 5, sticky = (constants.E, constants.W))


    def _initialize_statistics(self):

        stat = self._statistic

        wpm = ttk.Label(master = self._frame, text = stat.wpm_string(), font=('consolas', 12))
        time_taken = ttk.Label(master =self._frame, text = stat.time_taken_string(), font=('consolas', 12))
        accuracy = ttk.Label(master = self._frame, text = stat.accuracy_string(), font =('consolas', 12))

        wpm.grid(column=1, columnspan=1,  row = 1, padx = 5, pady = 5, sticky = (constants.E, constants.W))
        time_taken.grid(column=1, columnspan=1, row = 2, padx = 5, pady = 5, sticky = (constants.E, constants.W))
        accuracy.grid(column=1, columnspan=1, row = 3, padx = 5, pady = 5, sticky = (constants.E, constants.W))


    def _initialize_new_typing_test_button(self):
        
        typing_test_button = ttk.Button(
            master = self._frame,
            text = "New typing test",
            command = self._handle_new_typing_test_view
        )

        typing_test_button.grid(column = 1, columnspan = 2, row = 4, padx = 5, pady = 5)

    def _initialize_main_menu_button(self):
        
        main_menu_button = ttk.Button(
            master = self._frame,
            text = "Main menu",
            command = self._handle_main_menu_view
        )

        main_menu_button.grid(column = 1, columnspan = 2, row = 5, padx = 5, pady = 5)