from tkinter import *
import tkinter.font as tkFont

root=Tk()
root.title("Számológép")
root.geometry("600x800")   
myFont = tkFont.Font(family="Helvetica", size=40, weight="bold")
btnFont =tkFont.Font(family="Helvetica", size=20)
btn7=Button(root,text="7",height=10,width=20).grid(row=2,column=0,sticky=W)
btn8=Button(root,text="8",height=10,width=20).grid(row=2,column=1,sticky=W)
btn9=Button(root,text="9",height=10,width=20).grid(row=2,column=2,sticky=W)



  

root.mainloop()