from tkinter import *
win = Tk()

win.title('Buttons')
win.minsize(300, 300)

b1 = Button(win, text="Java")
b2 = Button(win, text="Oracle")
b3 = Button(win, text="Python")
b4 = Button(win, text="C++")

b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)

win.mainloop()