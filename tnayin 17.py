# # 1
# from tkinter import *
# ee=Tk()
# class Tnayin():
#     z=[LEFT,RIGHT]
#     x=0
#     y=1
#     def __init__(self):
#         self.f1=Frame(ee)
#         self.f2=Frame(ee)
#         self.l1 = Label(self.f1,text=" 111 ", bg="green", fg="red", font="20",width=20,height=10)
#         self.l2 = Label(self.f1,text=" 222 ", bg="yellow", fg="red", font="20",width=20,height=10)
#         self.l3 = Label(self.f2,text=" 333 ", bg="magenta", fg="red", font="20",width=20,height=10)
#         self.l4 = Label(self.f2,text=" 444 ", bg="black", fg="red", font="20",width=20,height=10)
#         self.l1.pack(side=LEFT)
#         self.l2.pack(side=RIGHT)
#         self.l3.pack(side=LEFT)
#         self.l4.pack(side=RIGHT)
#         self.f1.pack()
#         self.f2.pack()
#         self.l1.bind_all("<Button-3>", self.color)
#         self.l1.bind("<Button-1>", self.move)
#         self.l2.bind("<Button-1>", self.move)
#         self.l3.bind("<Button-1>", self.move)
#         self.l4.bind("<Button-1>", self.move)
#
#     def color(self,event):
#             self.l1.config(bg="gray")
#             self.l2.config(bg="gray")
#             self.l3.config(bg="gray")
#             self.l4.config(bg="gray")
#     def move(self,event):
#         self.x,self.y=self.y,self.x
#         self.l1.pack(side=self.z[self.x])
#         self.l2.pack(side=self.z[self.y])
#         self.l3.pack(side=self.z[self.x])
#         self.l4.pack(side=self.z[self.y])
#
# obj=Tnayin()
# ee.mainloop()

#2
from tkinter import *
qq=Tk()
class Redactor():

    def __init__(self):
        self.l = Label( text="5  ", bg="green", fg="red", font="20", width=20, height=10)
        self.t=Text(font="20", width=20, height=10)
        self.t.pack()
        self.l.pack()
        self.l.bind_all("<Button-1>",self.f1)

    def f1(self,event):
        exec(self.t.get(1.0, END))
obj=Redactor()

def print(*args):
        for i in args:
            obj.l["text"] += str(i) + " "
        obj.l["text"] += "\n"

qq.mainloop()