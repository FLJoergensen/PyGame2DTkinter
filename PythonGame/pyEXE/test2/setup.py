from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'optimize': 2,'bundle_files': 1}},
    console = [{'script': "main.py"}],
    zipfile = None,)
#windows
