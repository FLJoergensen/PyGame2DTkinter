import math
class TOWER:
    ALL=[]
    def __init__(self):
        TOWER.ALL.append(self)
        self.X=0
        self.Y=0
        self.Range=10
        self.DmgEffect={"slow":0.2,
                        "DMGWorld":0,
                        "DMGTech":0,
                        "DMGExplod":0,
                        "DMGBullit":0,
                        "DMGFire":0,
                        "HORROR":0,
                        "ELECTRIC":0}
        pass
    def __del__(self):
        TOWER.ALL.remove(self)
        pass
    def EFFECT(self,T,attr=""):
        T.TMPATTR["speed"]-=T.ATTR["ResistenceSlow"]*self.DmgEffect["slow"]*T.TMPATTR["speed"]
        dI=("DMGWorld","DMGTech","DMGExplod","DMGBullit","DMGFire")
        rI=("ResistenceDmg","ResistenceTechDmg","ResistenceExplodDmg","ResistenceBullitDmg","ResistenceFireDmg")
        i=0
        while i < len(dI) or i < len(rI):
            T.TMPATTR["hp"]-=T.ATTR[rI[i]]*self.DmgEffect[dI[i]]
            i+=1
        if T.ATTR["ResistenceHORROR"]*self.DmgEffect["HORROR"] >= T.ATTR["HOORORLVL"]:
            h=T.ATTR["ResistenceHORROR"]*self.DmgEffect["HORROR"]/float(T.ATTR["HOORORLVL"])
            T.TMPATTR["hp"]-=h
            T.ATTR["HOORORLVL"]*=1.5
            if T.TMPATTR["speed"]-0.1*h < 0.01:
                T.TMPATTR["speed"]=0.01
            else:
                T.TMPATTR["speed"]-=0.1*h
        if T.ATTR["ResistenceElectric"]*self.DmgEffect["ELECTRIC"] >= T.ATTR["ELECTRICLVL"]:
            h=T.ATTR["ResistenceElectric"]*self.DmgEffect["ELECTRIC"]/float(T.ATTR["ELECTRICLVL"])
            T.TMPATTR["hp"]-=h
            T.ATTR["ELECTRICLVL"]*=1.1
            if T.TMPATTR["speed"]-0.15*h < 0.01:
                T.TMPATTR["speed"]=0.01
            else:
                T.TMPATTR["speed"]-=0.15*h
        pass
    def UPDATE(self):
        for u in UNIT.ALL:
            r=math.sqrt(pow(u.X-self.X,2)+pow(u.Y-self.Y,2))
            if r<=self.Range:
                E=Effect(self,u,"",1)
                E.UPDATE()
            pass
        pass
class Effect:
    ALL=[]
    def __init__(self,FROM,Target,attr="",lifeValue=1):
        Effect.ALL.append(self)
        self.owner=FROM
        self.target=Target
        self.attr=attr
        self.LValue=lifeValue
    def __del__(self):
        try:
            Effect.remove(self)
        except:
            pass
        pass
    def UPDATE(self):
        if self.LValue==0:
            Effect.ALL.remove(self)
        else:
            self.owner.EFFECT(self.target,self.attr)
            self.LValue-=1
        pass
class UNIT:
    ALL=[]
    def __init__(self,name,move=(1,1)):
        UNIT.ALL.append(self)
        self.X=0
        self.Y=0
        self.move=move
        self.name=name
        self.ATTR={"speed":10,"hp":100,"maxhp":100,"HOORORLVL":100,"ELECTRICLVL":100,
                   "ResistenceSlow":1,
                   "ResistenceDmg":1,
                   "ResistenceTechDmg":1,
                   "ResistenceExplodDmg":1,
                   "ResistenceBullitDmg":1,
                   "ResistenceFireDmg":1,
                   "ResistenceHORROR":1,
                   "ResistenceElectric":1}
        self.TMPATTR=self.ATTR
        pass
    def __del__(self):
        UNIT.ALL.remove(self)
        pass
    def EFFECT(self,T,attr=""):
        pass
    def UPDATE(self):
        if self.TMPATTR["hp"]<=0:
            UNIT.ALL.remove(self)
        self.X=self.TMPATTR["speed"]*self.move[0]
        self.Y=self.TMPATTR["speed"]*self.move[1]
        self.TMPATTR["speed"]=self.ATTR["speed"]
        if self.TMPATTR["hp"]>self.TMPATTR["maxhp"]:
            self.TMPATTR["hp"]=self.TMPATTR["maxhp"]
        self.ATTR["hp"]=self.TMPATTR["hp"]
        pass

def Tank():
    u=UNIT("TANK")
    u.ATTR={"speed":10,"hp":1000,"maxhp":1000,"HOORORLVL":50,"ELECTRICLVL":60,
            "ResistenceSlow":0.4,
            "ResistenceDmg":1.5,
            "ResistenceTechDmg":1.2,
            "ResistenceExplodDmg":1.2,
            "ResistenceBullitDmg":0.2,
            "ResistenceFireDmg":0.5,
            "ResistenceHORROR":0.1,
            "ResistenceElectric":1.5}
def TDev():
    t=TOWER()
    t.DmgEffect={"slow":0.9,
                 "DMGWorld":0,
                 "DMGTech":3,
                 "DMGExplod":5,
                 "DMGBullit":10,
                 "DMGFire":10,
                 "HORROR":100,
                 "ELECTRIC":1}

def Update(updates=1,P=False):
    i=0
    while i<updates:
        n=[]
        n+=TOWER.ALL
        n+=Effect.ALL
        n+=UNIT.ALL
        for u in n:
            u.UPDATE()
        #TOWER.UPDATE()
        #Effect.UPDATE()
        #UNIT.UPDATE()
        i+=1
        if P:
            print "Update",i
            print "Tower",len(TOWER.ALL),"Effect",len(Effect.ALL),"Units",len(UNIT.ALL)
