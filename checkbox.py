from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
window.title("Checkbox")
window.geometry("300x200+50+80")
lbl = Label(window, text="Which country are you from?", bd=5)
lbl.place(x=60, y=70)
data = ("India", "Pakistan", "Afganistan", "UK")
cb = Combobox(window, values=data)
cb.place(x=70, y=100)
btn = Button(window, text="Enter", fg="Green")
btn.place(x=120, y=150)
window.mainloop()