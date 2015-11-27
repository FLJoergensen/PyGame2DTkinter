from distutils.core import setup
import py2exe,sys

sys.argv.append('py2exe')

ref=["mainsub.py"]
setup(name="PyGame",
      console=["main.py"],
      data_files=ref,
      zipfile=None,
      options = {'py2exe': {'optimize': 2}})
