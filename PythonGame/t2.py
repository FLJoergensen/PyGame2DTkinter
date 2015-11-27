import Tkinter as TK
import GUI
import EDITOR

root=TK.Tk()
c,l=GUI.newPlayField(1000,1000,20,20,root,"black",("<Button-1>",))
for item in l:
    item.clickList.append(EDITOR.P)
c.pack()
root.mainloop()
