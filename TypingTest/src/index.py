from tkinter import Tk, ttk, constants
from UI.ui import UI

window = Tk()
window.title("TypingTest")
window.geometry("500x400")
ui = UI(window)
ui._show_typing_test_view()

window.mainloop()