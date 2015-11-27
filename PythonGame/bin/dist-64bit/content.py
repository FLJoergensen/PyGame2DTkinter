import time
import thread

class Clock:
    def __init__(self):
        self._IsRunning=False
        self._licenner=set()
        self._delay=1
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
            elf._e.ticks+=1
            for item in self._licener:
                try:
                    thread.start_new(item,(self._e))
                except:
                    self._licener.remove(item)
            time.sleep(self._delay)
        elf._e.ticksequenz=0
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
    def removeAll(self):
        self._licenner=set()

class EventArg:
