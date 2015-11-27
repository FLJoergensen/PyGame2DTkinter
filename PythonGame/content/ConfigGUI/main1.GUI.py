import glob

TK.Button(root,text="TowerDefv1",command=lambda:LoadGUI(root,G1.Game)).pack()


l=glob.glob("content/ConfigGUI/*.GUI.py")
print l
l.remove("content/ConfigGUI\\main.GUI.py")
for item in l:
    it=item[::-1]
    it=it.split(".",2)[2]
    it=it[::-1]
    TK.Button(root,text=it,command=lambda : LoadGUIFile(root,it)).pack()
