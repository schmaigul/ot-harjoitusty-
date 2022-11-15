
class TypingTestFinishView:
    def __init__(self, handle_new_typing_test_view, handle_main_menu_view):

        self._handle_new_typing_test_view = handle_new_typing_test_view
        self._handle_main_menu_view = handle_main_menu_view

        self.initialize()

    def _initialize(self):

        self._initialize_statistics()
        self._initialize_new_typing_test_button()
        self._initialize_main_menu_button()

    def _initialize_statistics(self):
        pass

    def _initialize_new_typing_test_button(self):
        pass

    def _initialize_main_menu_button(self):
        pass