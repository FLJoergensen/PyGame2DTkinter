import GameContent as GC
import GUI
class World:
    def __init__(self,width,height,value=GUI.DrawObj()):
        self.map=GC.Map(width,height,value)
        pass
    def AddX(self,front=False,back=False):
        for l in self.map.m:
            if front:
                l.insert(0,None)
            if back:
                l.append(None)
        if front:
            self.map.maxX+=1
        if back:
            self.map.maxX+=1
        pass
    def AddY(self,top=False,bot=False):
        l=[None]*self.map.maxX
        if top:
            self.map.m.insert(0,l)
            self.map.maxY+=1
        if bot:
            self.map.m.append(l)
            self.map.maxY+=1
        pass
    pass
def P(vfield,e):
    print (vfield.column,vfield.row,e.x,e.y)
class VField:
    def __init__(self,koord1,koord2):
        self.setKoord(koord1,koord2)
        self.clickList=[]
        self.column=0
        self.row=0
    def In(self,koord):
        return self.Koordmin[0]<=koord[0]<=self.Koordmax[0] and self.Koordmin[1]<=koord[1]<=self.Koordmax[1]
    def setKoord(self,koord1,koord2):
        xmin=min(koord1[0],koord2[0])
        xmax=max(koord1[0],koord2[0])
        ymin=min(koord1[1],koord2[1])
        ymax=max(koord1[1],koord2[1])
        self.Koordmin=(int(xmin),int(ymin))
        self.Koordmax=(int(xmax),int(ymax))
    def getCenter(self):
        kdivX=(self.Koordmin[0]-self.Koordmax[0])/2
        kdivY=(self.Koordmin[1]-self.Koordmax[1])/2
        return (self.Koordmax[0]+kdivX,self.Koordmax[1]+kdivY)
    def getEges(self):
        k1=self.Koordmin
        k2=self.Koordmax
        return (k1,k2,(k1[0],k2[1]),(k2[0],k1[1]),self.getCenter())
    def clickEvent(self,e):
        for item in self.clickList:
            try:
                item(self,e)
            except:
                pass
class GUIField(GUI.DrawObj):
    def __init__(self):
        self.Layer={}
        self.Layer["blocked"]=False
        for i in range(10):
            self.Layer[i]=None

class WorldStruct:
    def __init__(self):
        self.WorldType=""
        self.UsedImages=[]
        self.GUIMap=None
        self.CollisionMap=None
        self.TriggerMap=None
        self.ObjectMap=None
        
