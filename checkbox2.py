from tkinter import *
window = Tk()
window.title('Choose Checkbox')
lb = Label(window, text='Choose your favorite video game', font=("Helvetica", 15))
lb.place(x=80, y=60)
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text="Cricket", variable = v1)
C2 = Checkbutton(window, text="Football", variable = v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)
window.geometry("400x200+10+10")
window.mainloop()