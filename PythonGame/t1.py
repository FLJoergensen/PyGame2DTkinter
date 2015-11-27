import Tkinter as TK
import time

vfl=[]
def genraster(w,h,linien,spalten,woff=0,hoff=0):
    l=[]
    import EDITOR as E
    wt=float(w-woff)/spalten
    ht=float(h-hoff)/linien
    x=0
    while x<spalten:
        y=0
        while y<linien:
            t=E.VField((wt*x+woff,ht*y+hoff),(wt*(x+1)+woff,ht*(y+1)+hoff))
            l.append(t)
            t.orb=str(y+1)+" liene | "+str(x+1)+" spalte"
            #print ((wt*x,ht*y),(wt*(x+1),ht*(y+1)),(x,y))
            y+=1
        x+=1
    return l

def lc(e):
    for item in vfl:
        if item.In((e.x,e.y)):
            print item.orb
            #print item.In((e.x,e.y))
            pass
    print (e.x,e.y)
def mc(e):
    startT=time.time()
    for item in vfl:
        if item.In((e.x,e.y)):
            print item.orb
            #print item.In((e.x,e.y))
            pass
    print (e.x,e.y)
    stopT=time.time()
    print stopT-startT
vfl=genraster(500,500,10,10)

root=TK.Tk()
TK.Button(root).pack()
c=TK.Canvas(root,width=500,height=500,background="#555555")
c.pack()
c.bind("<Button-1>",lc)
c.bind("<Button-2>",mc)
#c.bind("<Button-3>",rc)
root.mainloop()
