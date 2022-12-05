from tkinter import ttk, constants, StringVar

from services.statistic_service import statistic_service

class UserStatisticsView:

    def __init__(self, root, handle_menu_view):

        self._root = root
        self._handle_show_menu_view = handle_menu_view

        self._frame = None
        self._user_statistic = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._root.geometry("280x300")
        self._frame = ttk.Frame(master = self._root)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        self._user_statistic = statistic_service.get_current_user_statistic()

        if self._user_statistic is None:
            self._initialize_no_statistics_title()
        else:
            self._initialize_yes_statistics_title()
            self._initialize_wpm()
            self._initialize_total_played()
            self._initialize_accuracy()
            self._initialize_max_wpm()
            self._initialize_min_wpm()

        self._initialize_menu_button()

    def _initialize_no_statistics_title(self):

        label = ttk.Label(
            master = self._frame,
            text = "You haven't done any typing tests",
            font = ("consolas", 14, "bold")
        )
        label.grid(row = 1, column = 0, pady = 10)

    def _initialize_yes_statistics_title(self):

        username = self._user_statistic.username

        username_label = ttk.Label(
            master = self._frame,
            text = f"{username}'s statistics",
            font = ("consolas", 15, "bold")
        )

        username_label.grid(row = 1, column = 0, pady = 10)
        
    def _initialize_wpm(self):

        wpm = self._user_statistic.wpm_string()

        label = ttk.Label(
            master = self._frame,
            text = wpm,
            font = ("consolas", 13)
        )

        label.grid(row = 2, column = 0, pady = 5)

    def _initialize_total_played(self):

        total = self._user_statistic.total_string()

        total_label = ttk.Label(
            master = self._frame,
            text = total,
            font = ("consolas", 13)
        )

        total_label.grid(row = 3, column = 0, pady = 5)

    def _initialize_accuracy(self):

        accuracy = self._user_statistic.accuracy_string()

        acc_label = ttk.Label(
            master = self._frame,
            text = accuracy,
            font = ("consolas", 13)
        )

        acc_label.grid(row = 4, column = 0, pady = 5)

    def _initialize_max_wpm(self):

        max_wpm = self._user_statistic.max_wpm_string()

        max_wpm_label = ttk.Label(
            master = self._frame,
            text = max_wpm,
            font = ("consolas", 13)
        )

        max_wpm_label.grid(row = 5, column = 0, pady = 5)

    def _initialize_min_wpm(self):

        min_wpm = self._user_statistic.min_wpm_string()

        min_wpm_label = ttk.Label(
            master = self._frame,
            text = min_wpm,
            font = ("consolas", 13)
        )

        min_wpm_label.grid(row = 6, column = 0, pady = 5)

    def _initialize_menu_button(self):

        button = ttk.Button(
            master = self._frame,
            text = "Main menu",
            command = self._handle_show_menu_view
        )

        button.grid(column = 0, pady = 5)
