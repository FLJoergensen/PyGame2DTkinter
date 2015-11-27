import Tkinter as TK
import thread

c=None
i=0
def lc(e):
    global c,i
    img=TK.PhotoImage(file="content/image/ERROR.gif")
    print c.create_image(50+i,50+i,anchor=TK.CENTER,image=img)
    i+=10
    pass

root=TK.Tk()
img=TK.PhotoImage(file="content/image/ERROR.gif")
c=TK.Canvas(root,width=500,height=500,background="#555555")
c.bind("<Button-1>",lc)
c.pack()
thread.start_new(root.mainloop,())
#print c.create_image(50,50,anchor=TK.CENTER,image=img)
#lc("")
#root.update_idletasks()
#tk.update()
