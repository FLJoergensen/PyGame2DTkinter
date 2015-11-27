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
