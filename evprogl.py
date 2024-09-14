from tkinter import *
def mclick(event):
  print("Mouse got clicked...")

win = Tk()
win.title('Event Handling')
label = Label(win, text='Click me',bg='red')
label.pack()
label.bind('<Button>',mclick)
win.geometry("300x400+70+60")
win.mainloop()