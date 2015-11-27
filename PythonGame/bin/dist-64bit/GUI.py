class DrawObj:
    def draw(self,canvas,layer=0):
        pass
    def destroy(self,canvas,layer=-1):
        pass
    def update(self,e):
        pass
    pass

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
            t.row=y
            t.column=x
            l.append(t)
            y+=1
        x+=1
    return l
def newPlayField(width,height,row,column,root=None,background="#000000",binds=()):
    #return TK.Canvas()
    def click(e):
        for item in L:
            if item.In((e.x,e.y)):
                item.clickEvent(e)
    import Tkinter as TK
    c=TK.Canvas(root,width=width,height=height,background=background)
    L=genraster(width,height,row,column)
    for item in binds:
        c.bind(item,click)
    return (c,L)
