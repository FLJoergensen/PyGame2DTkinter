from Tkinter import *
import Tkinter as TK
import tkFileDialog as FD

def LoadImages():
    #from Tkinter import *
    #import tkFileDialog as FD
    return FD.askopenfilenames(filetypes=(("PGM","*.pgm"),("PPM","*.ppm"),("GIF","*.gif"))).split(" ")

#imgacc
imgaccstr=""
viewLayer=None
binded=False
basicWorld=None
def CreatEditor():
    global imgaccstr,viewLayer,binded,basicWorld
    W,WSteps=(32*30,30)
    H,HSteps=(32*30,30)
    import GUI
    import helpfull as HF
    import EDITOR as E
    ListB=None
    ListBContain=set()
    def setLayer(LAYER):
        global viewLayer
        viewLayer=LAYER
        changeLayer(LAYER)
    def changeLayer(LAYER):
        c.delete(TK.ALL)
        if LAYER==None or LAYER=="combo":
            for i in range(10):
                drawLayer(i)
            if LAYER=="combo":
                drawLayer("blocked")
            pass
        else:
            drawLayer(LAYER)
        pass
    def drawLayer(LAYER):
        if LAYER=="blocked":
            for item in l:
                if basicWorld.map.getV(item.column,item.row).Layer[LAYER]:
                    x1,y1=item.Koordmin
                    x2,y2=item.Koordmax
                    c.create_rectangle(x1,y1,x2,y2,fill="red")
        else:
            for item in l:
                if basicWorld.map.getV(item.column,item.row).Layer[LAYER]!=None:
                    gf=basicWorld.map.getV(item.column,item.row)
                    s,ID=gf.Layer[LAYER]
                    img=imgdic[s]
                    x,y=item.getCenter()
                    imgID=c.create_image(x,y,anchor=TK.CENTER,image=img)
                    gf.Layer[LAYER]=(s,imgID)
    def loadimg():
        imgs=LoadImages()
        for item in imgs:
            if not item in ListBContain:
                ListBContain.add(item)
                ListB.insert(1,item)
    def loadingImageIn(e):
        c.focus_set()
        global imgaccstr
        s=ListB.selection_get()
        imgaccstr=s
    def SaveMap(name="unknowe.WORLD"):
        #ToDo Test
        import GameContent as GC
        import copy
        SW=E.WorldStruct()
        SW.WorldType="basic"
        x=basicWorld.map.maxX
        y=basicWorld.map.maxY
        SW.CollisionMap=GC.Map(x,y,False)
        TM={}
        for i in range(10):
            TM[i]=None
        SW.GUIMap=GC.Map(x,y,TM)
        allL=basicWorld.map.getAll()
        allimageL=set()
        allimageL.add(HF.ErrorImage)
        for item in allL:
            for i in range(10):
                allimageL.add(item.Layer[i])
        try:
            allimageL.remove(None)
        except:
            pass
        SW.UsedImages=list(allimageL)
        iy=0
        while iy<y:
            ix=0
            while ix<x:
                r=basicWorld.map.getV(ix,iy).Layer
                b=r.pop("blocked")
                if b:
                    SW.CollisionMap.setV(ix,iy,True)
                TMtemp=copy.deepcopy(TM)
                for i in range(10):
                    tempr=r[i]
                    if tempr==None:
                        TMtemp[i]=None
                    else:
                        try:
                            TMtemp[i]=SW.UsedImages.index(tempr)
                        except:
                            TMtemp[i]=None
                SW.GUIMap.setV(ix,iy,r)
                ix+=1
            iy+=1
        import pickle
        of=FD.asksaveasfile("wb",defaultextension=".WORLD",filetypes=(("World","*.WORLD"),),initialdir="content/Maps/basic/",initialfile=name)
        pickle.dump(SW,of,pickle.HIGHEST_PROTOCOL)
        of.close()
        pass
    def LoadMap():
        global basicWorld
        import pickle
        of=FD.askopenfile("rb",defaultextension=".WORLD",filetypes=(("World","*.WORLD"),),initialdir="content/Maps/",initialfile="unknowe.WORLD")
        WS=pickle.load(of)
        x=WS.GUIMap.maxX
        y=WS.GUIMap.maxY
        bw=E.World(x,y)
        iy=0
        while iy<y:
            ix=0
            while ix<x:
                g=WS.GUIMap.getV(ix,iy)
                c=WS.CollisionMap.getV(ix,iy)
                g["blocked"]=c
                gf=E.GUIField()
                gf.Layer=g
                bw.map.setV(ix,iy,gf)
                ix+=1
            iy+=1
        basicWorld=bw
        changeLayer("combo")
        pass
    def CreateDrawCanvas(vfield,e):
        global viewLayer
        x,y=vfield.getCenter()
        gf=basicWorld.map.getV(vfield.column,vfield.row)
        if e.num==1 or e.state==264:
            if gf.Layer.has_key(viewLayer) and viewLayer!=None and viewLayer!="blocked":
                img=imgdic[imgaccstr]
                imgID=c.create_image(x,y,anchor=TK.CENTER,image=img)
                if gf.Layer[viewLayer]!=None:
                    c.delete(gf.Layer[viewLayer][1])
                gf.Layer[viewLayer]=(imgaccstr,imgID)
                pass
            if viewLayer=="blocked":
                gf.Layer[viewLayer]=True
            pass
        if e.num==3 or e.state==1032:
            if gf.Layer.has_key(viewLayer) and viewLayer!=None and viewLayer!="blocked":
                if gf.Layer[viewLayer]!=None:
                    c.delete(gf.Layer[viewLayer][1])
                gf.Layer[viewLayer]=None
                pass
            if viewLayer=="blocked":
                gf.Layer[viewLayer]=False
            pass
        pass
    def changeBind(b):
        global binded
        if not b:
            c.bind("<0>",lambda x:setLayer(0))
            c.bind("<1>",lambda x:setLayer(1))
            c.bind("<2>",lambda x:setLayer(2))
            c.bind("<3>",lambda x:setLayer(3))
            c.bind("<4>",lambda x:setLayer(4))
            c.bind("<5>",lambda x:setLayer(5))
            c.bind("<6>",lambda x:setLayer(6))
            c.bind("<7>",lambda x:setLayer(7))
            c.bind("<8>",lambda x:setLayer(8))
            c.bind("<9>",lambda x:setLayer(9))
        else:
            tempBindList=("<0>","<1>","<2>","<3>","<4>","<5>","<6>","<7>","<8>","<9>")
            for item in tempBindList:
                c.unbind(item)
        binded=b
    #World
    basicWorld=E.World(WSteps,HSteps,E.GUIField())
    #World END
    uclock=HF.Clock(0.5)
    uclock.addFunc(lambda x:PP("Update"))
    uclock.addFunc(lambda x:changeLayer(viewLayer))
    root=TK.Tk()
    root.title("Editor")
    #root.bind("<Alt-u>",lambda x: uclock.ActivChange())
    root.bind("<Control-s>",lambda x: SaveMap())
    root.bind("<Control-l>",lambda x: LoadMap())
    c,l=GUI.newPlayField(W,H,WSteps,HSteps,root,"#777777",("<Button-1>","<B1-Motion>","<Button-3>","<B3-Motion>"))
    for item in l:
        item.clickList.append(CreateDrawCanvas)
    c.bind("<Enter>",loadingImageIn)
    c.bind("<F5>",lambda x:changeLayer(viewLayer))
    c.bind("<F6>",lambda x:changeLayer("combo"))
    #c.bind("<F7>",lambda x:changeBind(not binded))
    binded=True
    #c.bind("<0>",lambda x:setLayer(0))
    #c.bind("<1>",lambda x:setLayer(1))
    #c.bind("<2>",lambda x:setLayer(2))
    #c.bind("<3>",lambda x:setLayer(3))
    #c.bind("<4>",lambda x:setLayer(4))
    #c.bind("<5>",lambda x:setLayer(5))
    #c.bind("<6>",lambda x:setLayer(6))
    #c.bind("<7>",lambda x:setLayer(7))
    #c.bind("<8>",lambda x:setLayer(8))
    #c.bind("<9>",lambda x:setLayer(9))
    c.grid(row=0,column=0)
    #load Images
    width=W/WSteps#1000/20
    height=H/HSteps#1000/20
    imgdic,il=HF.getSizedAllImages(width,height)
    #load Images END
    f=TK.Frame(root)
    f.grid(row=0,column=1)
    TK.Label(f,text="Label Selection").pack()
    TK.Button(f,text="None",command=lambda:setLayer(None)).pack()
    TK.Button(f,text="block",command=lambda:setLayer("blocked")).pack()
    TK.Button(f,text=str(0),command=lambda:setLayer(0)).pack()
    TK.Button(f,text=str(1),command=lambda:setLayer(1)).pack()
    TK.Button(f,text=str(2),command=lambda:setLayer(2)).pack()
    TK.Button(f,text=str(3),command=lambda:setLayer(3)).pack()
    TK.Button(f,text=str(4),command=lambda:setLayer(4)).pack()
    TK.Button(f,text=str(5),command=lambda:setLayer(5)).pack()
    TK.Button(f,text=str(6),command=lambda:setLayer(6)).pack()
    TK.Button(f,text=str(7),command=lambda:setLayer(7)).pack()
    TK.Button(f,text=str(8),command=lambda:setLayer(8)).pack()
    TK.Button(f,text=str(9),command=lambda:setLayer(9)).pack()
    #section pic select
    TK.Label(f,text="Texture Selection").pack()
    #TK.Button(f,text="Load Image",command=loadimg).pack()
    #TK.Button(f,text="None",command=loadimg).pack()
    #TK.Button(f,text="Image",command=loadimg).pack()
    #TK.Button(f,text="Color",command=loadimg).pack()
    ListB=TK.Listbox(f,width=50)
    #ListB.insert(0,HF.ErrorImage)
    for item in il:
        #print item
        ListB.insert(0,item)
    ListB.select_set(0)
    ListB.pack()
    root.mainloop()

def NewGUIonFile(name="test"):
    root=TK.Tk()
    execfile("content/ConfigGUI/"+name+".GUI.py")
    root.mainloop()
def LoadGUIFile(scGUI,name):
    acGUI.destroy()
    NewGUIonFile(name)
def PP(e):
    print e
def mainFrame():
    import glob
    root=TK.Tk()
    #root.bind("<Alt-e>",lambda x:CreatEditor())
    root.bind("<Control-e>",lambda x:LoadGUI(root,CreatEditor))
    #execfile("content/ConfigGUI/main.GUI.py")
    l=glob.glob("GAME*.py")
    for item in l:
        if item.startswith("GAME"):
            s=item
            s=s.replace(".py","")
            modul=__import__(s)
            s=s.replace("GAME","")
            TK.Button(root,text=s,command=lambda:LoadGUI(root,modul.Game)).pack()
    root.mainloop()
def LoadGUI(acGUI,GUIFunc):
    acGUI.destroy()
    GUIFunc()
mainFrame()
#CreatEditor()
#FD.asksaveasfile("wb",defaultextension=".WORLD",filetypes=(("World","*.WORLD"),),initialdir="content/Maps/",initialfile="Unknowen.WORLD")
#FD.askopenfile("rb",defaultextension=".WORLD",filetypes=(("World","*.WORLD"),),initialdir="content/Maps/",initialfile="unknowe.WORLD")
