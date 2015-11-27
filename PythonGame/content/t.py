import glob

L=("image/**/*.gif","image/*/*.gif","image/*.gif","/**/*.gif","/*.gif")

for i in L:
    g=glob.iglob(i)
    print i
    print list(g)
