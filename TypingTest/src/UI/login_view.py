from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_menu_view, handle_create_user_view):

        self._root = root
        self._handle_menu_view = handle_menu_view
        self._handle_create_user_view = handle_create_user_view

        self._frame = None
        self._username_form = None
        self._password_form = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self): 

        self._root.geometry("250x100")
        self._frame = ttk.Frame(master = self._root)

        self._initialize_username_and_password_label()   
        self._initialize_username_and_password_form()
        self._initialize_login_and_create_user_button()


    def _initialize_username_and_password_label(self):

        username_label = ttk.Label(master=self._frame,
                                text = "Username",
                                font=('consolas', 10, "bold"))
        password_label = ttk.Label(master=self._frame,
                                text = "Password",
                                font=('consolas', 10, "bold"))

        username_label.grid(column = 0, row = 0, padx= 5, pady = 5)
        password_label.grid(column = 0, row = 1, padx = 5, pady = 5)

    def _initialize_username_and_password_form(self):

        self._username_form = ttk.Entry(master = self._frame)
        self._password_form = ttk.Entry(master = self._frame)

        self._username_form.grid(column = 1, row = 0, padx = 5, pady = 5)
        self._password_form.grid(column = 1, row = 1, padx = 5, pady = 5)

    def _initialize_login_and_create_user_button(self):

        login_button = ttk.Button(master = self._frame,
                                text = "Login", 
                                command = self._handle_login)

        create_user_button = ttk.Button(master = self._frame,
                                    text = "Create user",
                                    command = self._handle_create_user_view)

        login_button.grid(column = 0, row = 2, padx = 5, pady = 5)
        create_user_button.grid(column = 1, row = 2, padx = 5, pady = 5)

    def _handle_login(self):

        username = self._username_form.get()
        password = self._password_form.get()

        #HERE CREATE LOGIC FOR CHECKING THE CORRECT LOGIN

        self._handle_menu_view()