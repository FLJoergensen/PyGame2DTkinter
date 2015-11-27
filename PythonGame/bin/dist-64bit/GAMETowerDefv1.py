import Tkinter as TK
import thread,time

import helpfull as HF
import GUI

c=None
root=None
x=20
y=20
def Game():
    gui()
    pass
def gui():
    global c,root
    root=TK.Tk()
    fc=TK.Frame(root).grid(column=0,row=0)
    f=TK.Frame(root).grid(column=1,row=0)
    c,l=GUI.newPlayField(32*x,32*y,x,y,fc,"black",("<Button-1>",))
    #scrolbar
    hbar=TK.Scrollbar(fc,orient=TK.HORIZONTAL)
    hbar.pack(side=TK.BOTTOM,fill=TK.X)
    hbar.config(command=c.xview)
    vbar=TK.Scrollbar(fc,orient=TK.VERTICAL)
    vbar.pack(side=TK.RIGHT,fill=TK.Y)
    vbar.config(command=c.yview)
    c.pack()
    c.config(width=32*10,height=32*10)
    c.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    c.pack(side=TK.LEFT,expand=True,fill=TK.BOTH)
    #end
    thread.start_new(root.mainloop,())
    #c.config(width=32*10,height=32*10)
    pass
