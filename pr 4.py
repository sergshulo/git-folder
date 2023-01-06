from tkinter import *
s = 'Вивчайте мову Python! '
tk = Tk()
tk.geometry('300x100')
tk.title('Реклама')
lab = Label(tk, text=s, font=('Cosmic Sans MS', 18, 'bold'), width=20, height=40, bg='yellow', fg='red')
lab.pack()
def clock():
    global s
    s = s[1:] + s[0]
    lab.config(text=s)
    tk.after(200, clock)
clock()
tk.mainloop()
