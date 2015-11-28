from distutils.core import setup
import py2exe, sys, os, platform

#sys.argv.append('py2exe')
def delRecDir(p):
    paths=list(os.walk(p))
    paths.reverse()
    for x in paths:
        for f in x[2]:
            l=x[0]+"/"+f
            if os.path.isfile(l):
                os.remove(l)
            if os.path.islink(l):
                os.unlink(l)
        os.rmdir(x[0])
def setupDIR():
    if not os.path.exists("bin"):
        os.mkdir("bin")
        fl=[]
        fl.append(open("bin/script32console.py","w"))
        fl.append(open("bin/script32windows.py","w"))
        fl.append(open("bin/script64console.py","w"))
        fl.append(open("bin/script64windows.py","w"))
        s='setup(console=["main.py"])'
        for f in fl:
            f.write(s)
    if os.path.exists("build"):
        delRecDir("build")
    if os.path.exists("dist"):
        delRecDir("dist")
def consoleNeedControle(p):
    try:
        f=open(p,"r")
        if "input(" in f.read():
            print "Need console"
            return True
        f.close()
        f=open(p,"r")
        for l in f:
            if "import " in l:
                st=l.split("import ",1)[1].split(" as ",1)[0].replace("\n","").replace(" ","").split(",")
                for s in st:
                    if consoleNeedControle(s+".py"):
                        return True
        f.close()
    except:
        return True
    return False
    pass

#windows
setupDIR()
WINDOWS=False
if not consoleNeedControle("main.py") or "W" in sys.argv:
    print "Use Windows mode"
    WINDOWS=True
    #sys.argv.append('W')
BIT=platform.architecture()[0]
if "32bit" == BIT:
    print "Setup 32-bit"
    if os.path.exists("bin/32bit"):
        delRecDir("bin/32bit")
    if WINDOWS:
        execfile("bin/script32windows.py")
    else:
        execfile("bin/script32console.py")
    os.renames("dist","bin/32bit")
    pass
if "64bit" == BIT:
    print "Setup 64-bit"
    if os.path.exists("bin/64bit"):
        delRecDir("bin/64bit")
    if WINDOWS:
        execfile("bin/script64windows.py")
    else:
        execfile("bin/script64console.py")
    os.renames("dist","bin/64bit")
    pass

try:
    delRecDir("dist")
    if "clean" in sys.argv:
        delRecDir("build")
except:
    print "not generated"
    pass
