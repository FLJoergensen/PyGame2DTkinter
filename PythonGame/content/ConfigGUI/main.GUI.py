import glob

l=glob.glob("GAME*.py")
for item in l:
    if item.startswith("GAME"):
        print item
        s=item
        s=s.replace(".py","")
        modul=__import__(s)
        s=s.replace("GAME","")
        TK.Button(root,text=s,command=lambda:LoadGUI(root,modul.Game)).pack()
