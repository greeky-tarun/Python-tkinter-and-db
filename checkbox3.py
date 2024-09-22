from tkinter import *
window = Tk()
window.title("multiple CheckBox")
window.geometry("300x300+10+10")
lb = Label(window, text="Language Known", font=("Helvetica", 15))
lb.place(x=80, y=60)

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

c1 = Checkbutton(window, text="English", variable= v1)
c2 = Checkbutton(window, text="Hindi", variable= v2)
c3 = Checkbutton(window, text="Odia", variable = v3)
c4 = Checkbutton(window, text="Bengali", variable=v4)

c1.place(x=100,y=100)
c2.place(x=100, y=130)
c3.place(x=100, y=160)
c4.place(x=100, y=190)

window.mainloop()