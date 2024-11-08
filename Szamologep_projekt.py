from tkinter import *
import tkinter.font as tkFont

root=Tk()
root.title("Számológép")
root.geometry("600x800")   
myFont = tkFont.Font(family="Helvetica", size=40, weight="bold")
btnFont =tkFont.Font(family="Helvetica", size=20)
eredmeny=Label(root, text="", height=2, font=myFont, anchor="e", padx=10)
eredmeny.grid(row=0, column=0, columnspan=4)

btn1=Button(root,text="1",height=10,width=20).grid(row=1,column=0,sticky=W)
btn2=Button(root,text="2",height=10,width=20).grid(row=1,column=1,sticky=W)
btn3=Button(root,text="3",height=10,width=20).grid(row=1,column=2,sticky=W)
ossze =Button(root, text="+", width=5, height=2,command="+")
ossze.grid(row=1, column=4)

btn4=Button(root,text="4",height=10,width=20).grid(row=2,column=0,sticky=W)
btn5=Button(root,text="5",height=10,width=20).grid(row=2,column=1,sticky=W)
btn6=Button(root,text="6",height=10,width=20).grid(row=2,column=2,sticky=W)

btn7=Button(root,text="7",height=10,width=20).grid(row=3,column=0,sticky=W)
btn8=Button(root,text="8",height=10,width=20).grid(row=3,column=1,sticky=W)
btn9=Button(root,text="9",height=10,width=20).grid(row=3,column=2,sticky=W)



  

root.mainloop()