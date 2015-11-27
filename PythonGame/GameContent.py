
class Map:
    def __init__(self,sizeX,sizeY,value=None):
        import copy
        self.maxX=sizeX
        self.maxY=sizeY
        self.m=[]
        n=[None]*sizeX
        i=0
        while i<sizeY:
            self.m.append(copy.deepcopy(n))
            i+=1
        #self.m.append(n)
        #self.m=self.m*sizeY
        self.MapChanged=True
        self.setAll(value)
        self.fullItemList=self.getAll()
        pass
    def getV(self,x,y):
        try:
            return self.m[y][x]
        except:
            return None
        pass
    def getAll(self):
        if not self.MapChanged:
            return self.fullItemList
        l=[]
        for item in self.m:
            l=l+item
        self.fullItemList=l
        self.MapChanged=False
        return l
    def setV(self,x,y,v):
        try:
            self.MapChanged=True
            self.m[y][x]=v
            v.x=x
            v.y=y
            self.MapChanged=True
        except:
            pass
        pass
    def setAll(self,v):
        self.MapChanged=True
        import copy
        y=0
        while y<self.maxY:
            x=0
            while x<self.maxX:
                self.setV(x,y,copy.deepcopy(v))
                x+=1
            y+=1
        self.MapChanged=True
        pass
    pass

class Field:
    def __init__(self):
        self.x=0
        self.y=0
        self.fullblocked=False
        self.moveable=False
        self.buildable=False
        self.isBuildingblocked=False
        self.Buildable=False
        self.Building=None
        self.Link=[]
        self.draweSizePX=10
        self.draweKoord=(5,5)
        self.draweKoordmin=(0,0)
        self.draweKoordmax=(10,10)
        pass
    def In(self,koord):
        return self.draweKoordmin[0]<koord[0]<self.draweKoordmax[0] and self.draweKoordmin[0]<koord[0]<self.draweKoordmax[0]
    pass
class Chunk:
    def __init__(self,koord1,koord2):
        self.lowerField=set()
        self.Koordmin=(0,0)
        self.Koordmax=(0,0)
        self.setKoord(koord1,koord2)
    def setKoord(self,koord1,koord2):
        xmin=min(koord1[0],koord2[0])
        xmax=max(koord1[0],koord2[0])
        ymin=min(koord1[1],koord2[1])
        ymax=max(koord1[1],koord2[1])
        self.Koordmin=(xmin,ymin)
        self.Koordmax=(xmax,ymax)
    def In(self,koord):
        return self.Koordmin[0]<=koord[0]<=self.Koordmax[0] and self.Koordmin[0]<=koord[0]<=self.Koordmax[0]
    def inin(self,koord):
        l=[]
        if self.In(koord):
            for f in self.lowerField:
                if f.In(koord):
                    l.append(f)
                    try:
                        n=f.inin(koord)
                        l=l+n
                    except:
                        pass
        return l
    def getCenter(self):
        kdivX=self.Koordmin[0]-self.Koordmax[0]
        kdivY=self.Koordmin[1]-self.Koordmax[1]
        return (self.Koordmax[0]+kdivX,self.Koordmax[1]+kdivY)
    def getEges(self):
        k1=self.Koordmin
        k2=self.Koordmax
        return (k1,k2,(k1[0],k2[1]),(k2[0],k1[1]),self.getCenter())

class Path:
    def __init__(self,koord,parent,startKoord,endKoord):
        self._path=[]
        self._parent=parent
        self.koord=koord
    def __cmp__(self,other):
        return cmp(self.cost,other.cost)
    def getStart(self):
        pass
    def getEnd(self):
        pass
    def add(self,koord):
        pass
