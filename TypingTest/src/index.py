from tkinter import Tk
from ui.ui import ui

window = Tk()
window.title("TypingTest")
window.geometry("540x400")
ui = ui(window)

window.mainloop()
