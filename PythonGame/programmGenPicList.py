import os
import sys
p="content/images.list"

if not os.path.isfile(p):
    f=open(p,"w")
    f.close()
