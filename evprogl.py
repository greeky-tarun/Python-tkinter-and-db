from tkinter import *
def mclick(event):
  print("Yes i love you ❤️")

win = Tk()
win.title('Event Handling')
label = Label(win, text='love Me',bg='red')
label.pack()
label.bind('<Button>',mclick)
win.geometry("300x400+70+60")
win.mainloop()