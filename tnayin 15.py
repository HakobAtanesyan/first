from tkinter import *
Aa=Tk()
class Hasv():
    def __init__(self):
        self.var=BooleanVar()
        self.var1=BooleanVar()
        self.e=Entry()
        self.t=Text()
        self.b2 = Button(text="save", width=10, height=0, command=self.f2)
        self.b1 = Button(text="open", width=10, height=0, command=self.f1)
        self.b3 = Button(text="ok", width=10, height=0, command=self.f3)
        self.b4 = Button(text="Text dashti guyn", width=15, height=0, command=self.f4)
        self.e.pack()
        self.t.pack()
        self.b1.pack()
        self.b2.pack()
        self.var.set(0)
        self.var1.set(0)
        ra1 = Radiobutton(text="red", variable=self.var, value=0)
        ra2 = Radiobutton(text="green", variable=self.var, value=1)
        ra3 = Radiobutton(text="yellow", variable=self.var1, value=1)
        ra4 = Radiobutton(text="magenta", variable=self.var1, value=0)
        ra1.pack(anchor=SE)
        ra2.pack(anchor=SE)
        ra3.pack(anchor=SW)
        ra4.pack(anchor=SW)
        self.b3.pack(anchor=SE)
        self.b4.pack(anchor=SW)
    def f1(self):
        self.o = open(self.e.get())
        self.t.insert(1.0,self.o.read())
    def f2(self):
        self.s = open(self.e.get(), 'w')
        self.s.write(self.t.get(1.0, END))
    def f3(self):
        if self.var.get()==0:
            self.t.config(bg="red",fg="white")
            Aa.config(bg="white")
        else:
            self.t.config(bg="green",fg="red")
            Aa.config(bg="black")
    def f4(self):
        if self.var1.get() == 0:
            self.e.config(bg="magenta")
        else:
            self.e.config(bg="Yellow")
obj=Hasv()
Aa.mainloop()