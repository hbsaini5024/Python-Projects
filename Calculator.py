#Make Calcuclator By Using Python TKinter

from tkinter import*
root =   Tk()

root.geometry('550x750')
root.title('HB Calculator')

def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())      #evaluate the string

        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    pass

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, padx=20, pady=20)



f = Frame(root, bg="grey")
b = Button(f, text='9', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='8', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='7', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text='6', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='5', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='4', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text='3', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='2', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='1', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text='0', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=26,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='-', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='*', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text='/', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='%', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='=', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text='c', font='lucida 25 bold', padx=24, pady=10)
b.pack(side=LEFT, anchor='nw', padx=19,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='+', font='lucida 25 bold', padx=25, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
b = Button(f, text='c', font='lucida 25 bold', padx=26, pady=10)
b.pack(side=LEFT, anchor='nw', padx=20,pady=10)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()