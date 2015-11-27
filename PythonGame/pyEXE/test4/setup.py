from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
def setupDIR(n):
    try:
        os.mkdir("bin")
    except:
        pass
    try:
        os.remove("build")
    except:
        pass
    try:
        os.remove("dist")
    except:
        pass
#windows
if "32" in sys.platform:
    print "Setup 32-bit"
    setup(
        options = {'py2exe': {'optimize': 2,'bundle_files': 1}},
        console = [{'script': "main.py"}],
        zipfile = None,)
    os.renames("dist","bin/bin-32bit")
    pass
else:
    if "64" in sys.platform:
        print "Setup 64-bit"
        pass
    else:
        print "Setup ??-bit"
        pass
