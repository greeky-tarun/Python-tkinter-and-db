from tkinter import *
window = Tk()
window.title("Input window")
window.geometry("300x200+10+10")
lb = Label(window, text="Hello Tarun Kumar", fg='red', font=("Helvetica", 16))
lb.place(x=80, y=100)
lb.pack(side=TOP)
txtfield = Entry(window, text="Enter login Id", bd=5)
# adding padding from top to 50 so it will show in center
txtfield.pack(pady=40)
txtfld = Entry(window, show="*", bd=5)
txtfld.place(x=83, y=105)
btn = Button(window, text="Enter", fg='Green')
btn.pack(pady=(0, 5))
window.mainloop()