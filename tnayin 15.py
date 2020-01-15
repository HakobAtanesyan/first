from tkinter import *
ss=Tk()

def func1(event):
    # l2.config(text=t.get(1.0,END))
    exec(t.get(1.0,END))
def print(*args):
    for i in args:
        l2["text"]+=str(i)+" "
    l2["text"] +="\n"
def fe(event):
    l3.config(bg="red")
    b.config(bg="red")
def fl(event):
    l3.config(bg="white")
    b.config(bg="yellow")
l1=Label(text=" 111 ", bg="green", fg="white",width=20, height=20 )
l2=Label(text="222", bg="green", fg="white", font="20",width=20, height=10,anchor=W)
l3=Label(text="222", bg="yellow", fg="black", font="20",width=10, height=0)
b=Button(text="Enter", width=5, height=0,)
t=Text(width=20, height=10)
l3.bind("<Enter>",fe)
l3.bind("<Leave>",fl)
t.bind("<FocusIn>",fl)
b.bind("<Enter>",fe)
b.bind("<Leave>",fl)
l1.pack()
l2.pack()
l3.pack()
t.pack()
b.pack()
ss.bind("<Control-Return>",func1)
ss.mainloop()