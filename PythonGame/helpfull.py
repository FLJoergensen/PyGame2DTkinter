ImagePath="content/image/"
ErrorImage=ImagePath+"ERROR.gif"
recDeep=3
def loadImage(path):
    import Tkinter as TK
    try:
        img=TK.PhotoImage(file=path)
    except:
        try:
            img=TK.PhotoImage(file=ImagePath+path)
        except:
            img=TK.PhotoImage(file=ErrorImage)
    return img
def loadSizedImage(width,height,path):
    img=loadImage(path)
    #print (img.width(),img.height())
    sw=float(width)/img.width()
    sh=float(height)/img.height()
    img=img.zoom(int(sw),int(sh))
    #img=img.zoom(sw,sh)
    #img=img.zoom(width,height)
    #print ((img.width(),img.height()),(width,height),(sw,sh))
    return img

def drawImageOnVField(canvas,vfield,imagepath):
    x,y=vfield.getCenter()
    xs=vfield.Koordmax[0]-vfield.Koordmin[0]
    ys=vfield.Koordmax[1]-vfield.Koordmin[1]
    img=loadSizedImage(xs,ys,imagepath)
    return canvas.create_image(x,y,anchor=TK.CENTER,image=img)
def drawLoadedImageOnVField(canvas,vfield,img):
    x,y=vfield.getCenter()
    return canvas.create_image(x,y,anchor=TK.CENTER,image=img)

def getAllImages(startpath=ImagePath,types=("*.gif","*.ppm","*.pgm")):
    import glob
    l=[]
    i=0
    while i<recDeep:
        it="**/"*i
        for t in types:
            l+=glob.glob(startpath+it+t)
        i+=1
    return l
def getAllImagesF(startpath=ImagePath,types=("*.gif","*.ppm","*.pgm")):
    import glob
    l=[]
    for t in types:
        l+=glob.iglob(startpath+t)
    return l
def getSizedAllImages(width,height,startpath=ImagePath,types=("*.gif","*.ppm","*.pgm")):
    l=getAllImages(startpath,types)
    dic={}
    for item in l:
        dic[item]=loadSizedImage(width,height,item)
    return (dic,l)


#clock
import time
import thread

class Clock:
    def __init__(self,delay=1):
        self._IsRunning=False
        self._licenner=set()
        self._delay=delay
        e=EventArg()
        e.caller=self
        e.type="clock"
        e.ticksequenz=0
        e.ticks=0
        self._e=e
    def Start(self):
        self._IsRunning=True
        thread.start_new(self._start,())
    def _start(self):
        while self._IsRunning:
            self._e.ticksequenz+=1
            self._e.ticks+=1
            for item in list(self._licenner):
                try:
                    thread.start_new(item,(self._e))
                except:
                    self._licenner.remove(item)
            time.sleep(self._delay)
        self._e.ticksequenz=0
    def Stop(self):
        self._Isrunning=False
    def setDelay(self,v):
        self._delay=float(v)
    def addFunc(self,func):
        self._licenner.add(func)
    def removeFunc(self,func):
        try:
            self._licenner.remove(func)
        except:
            pass
        if len(self._licenner)==0:
            self.Stop()
    def removeAll(self):
        self._licenner=set()
        self.Stop()
    def ActivChange(self):
        if self._IsRunning:
            thread.start_new(self.Stop,())
        else:
            thread.start_new(self.Start,())

class EventArg:
    pass

#Surch algo
def getMoves(ID,stepSize=1):
    i=stepSize
    if ID==4:
        return ((-1,0,i),(1,0,i),(0,-1,i),(0,1,i))
    if ID==16:
        return ((-1,0,i),(1,0,i),(0,-1,i),(0,1,i),
                (-2,0,i*2),(2,0,i*2),(0,-2,i*2),(0,2,i*2))
    if ID==8:
        return ((-1,0,i),(1,0,i),(0,-1,i),(0,1,i),
                (-1,-1,i),(1,1,i),(1,-1,i),(-1,1,i))
    return []
def AStern(BlockingMap,start=(0,0),end=(0,0)):
    import Queue
    import GameContent as GC
    q=Queue.PriorityQueue()
    pass

def getFullMap(BlockingMap,linkList=[]):
    class POINT:
        def __init__(self,x,y):
            self.x=x
            self.y=y
            self.B=False
            self.LINKED=[]
            self.LINKEDrev=[]
    import copy
    m=copy.deepcopy(BlockingMap)
    iy=0
    while iy<m.maxY:
        ix=0
        while ix<m.maxX:
            p=POINT(ix,iy)
            p.B=bool(m.getV(ix,iy))
            m.setV(ix,iy,p)
            ix+=1
        iy+=1
    for item in linkList:
        s,e=item
        xs,ys=s
        xe,ye=e
        sp=m.getV(xs,ys)
        ep=m.getV(xe,ye)
        if sp and ep:
            sp.LINKED.append(ep)
            ep.LINKED.append(sp)
    return m

def GuenstigsterPath(FullMap,start=(0,0),end=(0,0),moves=()):
    def GETcount(x,y):
        p=M.getV(x,y)
        return countDIC[p]
    def isBlocked(x,y):
        p=M.getV(x,y)
        return p.B
    import GameContent as GC
    countDIC={}
    M=FullMap
    templ=M.getAll()
    for i in templ:
        countDIC[i]=None
    S=M.getV(start[0],start[1])
    E=M.getV(end[0],end[1])
    if not (S and E and S!=E):
        return None
    #todo
    pass
