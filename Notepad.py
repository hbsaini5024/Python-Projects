#Notepad Making Using Python Tkinter

from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)  #remove all characters Between line 1 and Oth Character

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
                                                             ("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),
                                                                                               ("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            #Save as a NewFile
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the File
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad By Harsh Bobby 2020")


if __name__ == '__main__':
    #Basic Tkinter Setup
    root = Tk()
    root.title('HB Notepad')
    root.geometry('600x500')


    #Add TextArea using Text Widget
    TextArea = Text(root)
    TextArea.pack(fill=BOTH, expand=True)
    file = None

    #Create a MenuBar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)

    #To Open a New File
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing File
    FileMenu.add_command(label="Open", command=openFile)

    #To Save the Current File
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    #File Menu Ends

    #Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)

    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    #Edit Menu Ends

    #Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)

    HelpMenu.add_command(label='About Notepad', command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    #Help Menu Ends
    root.config(menu=MenuBar)

    #Adding Scrollbar(Lecture 22)
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()