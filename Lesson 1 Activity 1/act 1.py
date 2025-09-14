from tkinter import *

root=Tk()

root.geometry("400x300")

root.title("main")

def topvin():
    
    top=Toplevel()

    top.geometry("180x100")

    top.title("top level")

    l2=Label(top,text="This is the top level window")

    l2.pack()

    top.mainloop()

l=Label(root,text="This is the root window")

btn=Button(root,text="Click here to open another window",command=topvin)

l.pack()

btn.pack()