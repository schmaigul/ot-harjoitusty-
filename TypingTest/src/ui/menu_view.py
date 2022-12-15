from tkinter import ttk, constants

from services.user_service import user_service

class MenuView:
    def __init__(self, root, handle_logout_view, handle_new_typing_test_view, handle_user_statistics_view):
        
        self._root = root
        self._handle_logout_view = handle_logout_view
        self._handle_new_typing_test_view = handle_new_typing_test_view
        self._handle_user_statistics_view = handle_user_statistics_view

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._root.geometry("300x200")
        self._frame = ttk.Frame(master = self._root)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
        
        self._initialize_header()
        self._initialize_start_typing_test_button()
        self._initialize_statistics_button()
        self._initialize_logout_button()

    def _initialize_header(self):

        username = user_service.get_current_user().username

        header = ttk.Label(master = self._frame,
                        text = f"Logged in as {username}",
                        font = ('consolas', 13, 'bold'))

        header.grid(column=0, row=0, padx = 5, pady = 5)

    def _initialize_start_typing_test_button(self):

        typing_test_button = ttk.Button(master = self._frame,
                                    text = "Start a typing test",
                                    command = self._handle_new_typing_test_view,
                                    width = 200)

        typing_test_button.grid(column = 0, row = 1, padx = 5, pady = 5)

    def _initialize_statistics_button(self):

        statistics_button = ttk.Button(master = self._frame,
                                    text = "Statistics",
                                    command = self._handle_user_statistics_view,
                                    width = 200)

        statistics_button.grid(column = 0, row = 2, padx = 5, pady = 5)

    def _initialize_logout_button(self):

        logout_button = ttk.Button(master = self._frame,
                                text = "Logout",
                                command = self._handle_logout,
                                width = 200)

        logout_button.grid(column = 0, row = 3, padx = 5, pady = 5)

    def _handle_logout(self):

        user_service.logout()
        self._handle_logout_view()