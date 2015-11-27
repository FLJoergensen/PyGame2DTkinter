#http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
import Tkinter as TK
import time

t=True
E=None
E1=None
def lc(e):
    global E
    print "leftklick"
    print e
    E=e
def mc(e):
    global E1
    print "midleklick"
    print e
    E1=e
def t(e):
    print "test"
def changeC(e):
    global ID,t
    c.delete(ID)
    if t:
        ID=c.create_rectangle(0,0,50,50,fill="black")
    else:
        ID=c.create_rectangle(0,0,50,50,fill="#FF0000")
    t=not t
def CC(e):
    global ID,t,ID2
    if t:
        c.itemconfig(ID,fill="black")
    else:
        c.itemconfig(ID,fill="#FF0000")
    t=not t
def setFocus(e):
    e.widget.focus_set()
def unsetFocus(e):
    root.focus_set()

root=TK.Tk()
#e=TK.Entry(root)
#e.bind("<Shift-Up>",t)
#e.bind("<Up>",t)
#e.bind("<Left>",t)
#e.bind("<Right>",t)
#e.bind("<Down>",t)
#e.place(x=20,y=30,width=120,height=25)
c=TK.Canvas(root,width=500,height=500,background="#555555")
c.bind("<Button-1>",lc)
c.bind("<F5>",mc)
#c.bind("<Motion>",changeC)
c.bind("<Motion>",CC)
c.bind("<Shift-Up>",t)
c.bind("<Return>",t)
c.bind("<Enter>",setFocus)
c.bind("<Leave>",unsetFocus)
c.grid(row=0,column=0)
#c.focus_set()
#e.focus_set()
ID=c.create_rectangle(0,0,50,50,fill="black")
import helpfull as HF
img=HF.loadSizedImage(200,200,"content/image/wall.gif")
print img
c.create_image(120,50,anchor=TK.CENTER,image=img)
root.mainloop()
