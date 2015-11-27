from distutils.core import setup
import py2exe,sys,glob

sys.argv.append('py2exe')

try:
    ref=glob.glob("*.py")
    for r in ("main.py","RUN.py","setup.py"):
        ref.remove(r)
except:
    ref=[]

#https://docs.python.org/2/distutils/apiref.html
setup(name="PyGame",
      console=["main.py"],
      data_files=ref,
      zipfile=None,
      options = {'py2exe': {'optimize': 2}})
