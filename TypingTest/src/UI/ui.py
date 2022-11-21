from ui.typing_test_view import TypingTestView
from ui.typing_test_finish_view import TypingTestFinishView

class ui:
    def __init__(self, root):
        self._root = root
        self._current_view = None

        self._show_typing_test_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_typing_test_view(self):
        self._hide_current_view()

        self._current_view = TypingTestView(self._root, self._show_typing_test_finish_view)
        
        self._current_view.pack()

    def _show_login_view(self):
        pass

    def _show_menu_view(self):
        pass

    def _show_typing_test_finish_view(self):
        self._hide_current_view()

        self._current_view = TypingTestFinishView(self._root, self._show_typing_test_view, self._show_menu_view)

        self._current_view.pack()

    def _show_personal_statistics_view(self):
        pass