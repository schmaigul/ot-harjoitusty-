from tkinter import Tk
from ui.ui import ui

window = Tk()
window.title("TypingTest")
window.geometry("500x400")
ui = ui(window)

window.mainloop()
