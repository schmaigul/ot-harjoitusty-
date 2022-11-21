from tkinter import ttk, constants

class MenuView:
    def __init__(self, root, handle_logout_view, handle_new_typing_test_view):
        
        self._root = root
        self._handle_logout_view = handle_logout_view
        self._handle_new_typing_test_view = handle_new_typing_test_view
        self._handle_statistics_view = None

        self._frame = None
        self._user = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._root.geometry("250x100")
        self._frame = ttk.Frame(master = self._root)

        self._initialize_header()
        self._initialize_start_typing_test_button()
        self._initialize_statistics_button()
        self._initialize_logout_button()

    def _initialize_header(self):

        header = ttk.Label(master = self._frame, text = f"Logged in as {self._user}")

        header.grid(column=0, row=0, columnspan=1, padx = 5, pady = 5)

    def _initialize_start_typing_test_button(self):

        typing_test_button = ttk.Button(master = self._frame,
                                    text = "Start a typing test",
                                    command = self._handle_new_typing_test_view)

        typing_test_button.grid(column = 1, row = 1, columnspan=1, padx = 5, pady = 5)

    def _initialize_statistics_button(self):

        statistics_button = ttk.Button(master = self._frame, 
                                    text = "Statistics",
                                    command = self._handle_statistics_view)

        statistics_button.grid(column = 0, row = 1, columnspan=1, padx = 5, pady = 5)

    def _initialize_logout_button(self):

        logout_button = ttk.Button(master = self._frame,
                                text = "Logout",
                                command = self._handle_logout_view)

        logout_button.grid(column = 1, row = 0, columnspan = 1, padx = 5, pady = 5)