import Tkinter as TK
import thread,time

import helpfull as HF
import GUI

c=None
root=None
x=20
y=20
TID=0
def Game():
    gui1()
    pass
def gui():
    global c,root
    root=TK.Tk()
    c,l=GUI.newPlayField(32*x,32*y,x,y,root,"black",("<Button-1>",))
    c.grid(column=0,row=0)
    menueFrame=TK.Frame(root)
    TK.Button(menueFrame,text="T1",command=lambda:setTID(1)).pack()
    menueFrame.grid(column=1,row=0)
    #thread.start_new(root.mainloop,())
    root.mainloop()
def gui1():
    global c,root
    root=TK.Tk()
    fc=TK.Frame(root).grid(column=0,row=0)
    f=TK.Frame(root).grid(column=1,row=0)
    c,l=GUI.newPlayField(32*x,32*y,x,y,fc,"black",("<Button-1>",))
    #scrolbar
    hbar=TK.Scrollbar(c,orient=TK.HORIZONTAL)
    hbar.pack(side=TK.BOTTOM,fill=TK.X)
    hbar.config(command=c.xview)
    vbar=TK.Scrollbar(c,orient=TK.VERTICAL)
    vbar.pack(side=TK.RIGHT,fill=TK.Y)
    vbar.config(command=c.yview)
    c.pack()
    c.config(width=32*10,height=32*10)
    c.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    c.pack(side=TK.LEFT,expand=True,fill=TK.BOTH)
    #end
    #thread.start_new(root.mainloop,())
    #c.config(width=32*10,height=32*10)
    root.mainloop()
    pass
def setTID(ID):
    global TID
    TID=ID
