class Game:
    def __init__(self,mapSize=(10,10),fieldSize=50,UpdatesPSec=10,DrawPSec=20):
        import helpfull as HF
        import GameContent as GC
        self.UPS=HF.Clock(1.0/UpdatesPSec)
        self.DPS=HF.Clock(1.0/DrawPSec)
        self.map=GC.Map(mapSize[0],mapSize[1],None)
        pass
    def __del__(self):
        pass
    def start(self):
        pass
    def stop(self):
        pass
    def load(self):
        pass
    pass
