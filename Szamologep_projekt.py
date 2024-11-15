from tkinter import *
import tkinter.font as tkFont

root=Tk()
root.title("Számológép")
root.geometry("800x1000")
input=""
elsoszam=None
muvelet=""

def szamgomb(num):
    global input
    if input == "0":
        input = str(num)
    else:
        input += str(num)
    kiiras.config(text=input)
    
def clear():
    global input,elsoszam,muvelet
    input=""
    elsoszam=None
    muvelet=""


kiiras = Label(root, text="0", width=16, height=2, anchor="e", font=("Arial", 24))
kiiras.grid(row=0, column=0, columnspan=4)   
myFont = tkFont.Font(family="Helvetica", size=40, weight="bold")
btnFont =tkFont.Font(family="Helvetica", size=20)
eredmeny=Label(root, text="", height=2, font=myFont, anchor="e", padx=10)
eredmeny.grid(row=0, column=0, columnspan=4)

btn1=Button(root,text="1",height=10,width=20,command=).grid(row=1,column=0,sticky=W)
btn2=Button(root,text="2",height=10,width=20).grid(row=1,column=1,sticky=W)
btn3=Button(root,text="3",height=10,width=20).grid(row=1,column=2,sticky=W)
ossze =Button(root, text="+", width=20, height=10,command="+")
ossze.grid(row=1, column=4)

btn4=Button(root,text="4",height=10,width=20).grid(row=2,column=0,sticky=W)
btn5=Button(root,text="5",height=10,width=20).grid(row=2,column=1,sticky=W)
btn6=Button(root,text="6",height=10,width=20).grid(row=2,column=2,sticky=W)
kivon=Button(root,text="-",height=10,width=20,command="-").grid(row=2,column=4)

btn7=Button(root,text="7",height=10,width=20).grid(row=3,column=0,sticky=W)
btn8=Button(root,text="8",height=10,width=20).grid(row=3,column=1,sticky=W)
btn9=Button(root,text="9",height=10,width=20).grid(row=3,column=2,sticky=W)

torles=Button(root,text="C",height=10,width=20).grid(row=4,column=0)
btn0=Button(root,text="0",height=10,width=20).grid(row=4,column=1)



  

root.mainloop()