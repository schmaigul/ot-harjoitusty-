from services.user_service import user_service, UserExistError, EmptyPasswordError

from tkinter import ttk, constants, StringVar

class CreateUserView:
    def __init__(self, root, handle_login_view):

        self._root = root
        self._handle_login_view = handle_login_view

        self._frame = None
        self._username_form = None
        self._password_form = None

        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._root.geometry("330x130")
        self._frame = ttk.Frame(master = self._root)
        self._frame.grid_columnconfigure(1, weight = 1, minsize = 200)

        self._initialize_error_label()
        self._initialize_create_user_header()
        self._initialize_username_and_password_label()
        self._initialize_username_and_password_form()
        self._initialize_create_account_button()
        self._initialize_login_view_button()

    def _initialize_error_label(self):

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(master=self._frame,
                                textvariable = self._error_variable,
                                font = ('consolas', 10, 'bold'),
                                foreground = 'red')

        self._error_label.grid(row = 0, column = 1, columnspan = 2, padx=5, pady=1)

    def _initialize_create_user_header(self):

        create_user_header = ttk.Label(master = self._frame,
                                text = "Create a new user",
                                font=('consolas', 10, "bold")
                                )

        create_user_header.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = constants.W)

    def _initialize_username_and_password_label(self):

        username_label = ttk.Label(master=self._frame,
                                text = "Username",
                                font=('consolas', 10, "bold"))

        password_label = ttk.Label(master=self._frame,
                                text = "Password",
                                font=('consolas', 10, "bold"))

        username_label.grid(column = 0, row = 1, padx= 5, pady = 5)
        password_label.grid(column = 0, row = 2, padx = 5, pady = 5)

    def _initialize_username_and_password_form(self):

        self._username_form = ttk.Entry(master = self._frame)
        self._password_form = ttk.Entry(master = self._frame, show = "*")

        self._username_form.grid(column = 1, row = 1, padx = 5, pady = 5, sticky = (constants.E, constants.W))
        self._password_form.grid(column = 1, row = 2, padx = 5, pady = 5, sticky = (constants.E, constants.W))

    def _initialize_create_account_button(self):

        create_user_button = ttk.Button(master = self._frame,
                                    text = "Create user",
                                    command = self._handle_create_user)

        create_user_button.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = (constants.E, constants.W))

    def _initialize_login_view_button(self):

        login_button = ttk.Button(master = self._frame,
                                text = "Back to login",
                                command = self._handle_login_view)

        login_button.grid(column = 0, row = 3, padx = 5, pady = 5, sticky = (constants.E, constants.W))

    def _handle_create_user(self):

        username = self._username_form.get()
        password = self._password_form.get()

        try:
            user = user_service.create_user(username, password)
            self._handle_login_view()
        except UserExistError:
            self._error_variable.set("User already exists")
            self._error_label.grid(row = 0, column = 1, columnspan = 2, padx=5, pady=1)
        except EmptyPasswordError:
            self._error_variable.set("Password cannot be empty")
            self._error_label.grid(row = 0, column = 1, columnspan = 2, padx=5, pady=1)
    
