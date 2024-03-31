#20NU1A05A6 S.VEERABABU OWN PROJECT 
from tkinter import *
mw=Tk()

def call():
    add1=0
    add2=0
    add1=float(Entry1.get())+float(Entry2.get())+float(Entry3.get())+float(Entry4.get())+float(Entry5.get())+float(Entry6.get())+float(Entry7.get())+float(Entry8.get())+float(Entry9.get())
    add1+=float(Entry10.get())+float(Entry11.get())+float(Entry12.get())
    
    add2=float(Entry1.get())*float(E1.get())+float(Entry2.get())*float(E2.get())+float(Entry3.get())*float(E3.get())+float(Entry4.get())*float(E4.get())+float(Entry5.get())*float(E5.get())
    add2+=float(Entry6.get())*float(E6.get())+float(Entry7.get())*float(E7.get())+float(Entry8.get())*float(E8.get())+float(Entry9.get())*float(E9.get())+float(Entry10.get())*float(E10.get())
    add2+=float(Entry11.get())*float(E11.get())+float(Entry12.get())*float(E12.get())
    add2/=add1
    
    res="Student SGPA IS:\n"+str(add2)+"\n And Total credits are: "+str(add1)
    l1=Label(mw,text=res,font="14",fg="aqua",border="5")
    l1.place(x=740,y=240)


def del1():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry9.delete(0,END)
    entry10.delete(0,END)
    entry11.delete(0,END)
    entry12.delete(0,END)
def del2():
    Entry1.delete(0,END)
    Entry2.delete(0,END)
    Entry3.delete(0,END)
    Entry4.delete(0,END)
    Entry5.delete(0,END)
    Entry6.delete(0,END)
    Entry7.delete(0,END)
    Entry8.delete(0,END)
    Entry12.delete(0,END)
    Entry9.delete(0,END)
    Entry10.delete(0,END)
    Entry11.delete(0,END)
    
def del3():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    E6.delete(0,END)
    E7.delete(0,END)
    E8.delete(0,END)
    E9.delete(0,END)
    E10.delete(0,END)
    E11.delete(0,END)
    E12.delete(0,END)





    
label1=Label(mw,text="STUDENT SGPA CALCULATOR",font="14",fg="green",bg="yellow")
label2=Label(mw,text="Enter subject names",font="14",fg="green",bg="yellow")
label3=Label(mw,text="Enter Credit of subject",font="14",fg="green",bg="yellow")
label4=Label(mw,text="Enter Points scored",font="14",fg="green",bg="yellow")
label5=Label(mw,text="STUDENT SGPA",font="14",fg="green",bg="yellow")

entry1=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry2=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry3=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry4=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry5=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry6=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry7=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry8=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry9=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry10=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry11=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
entry12=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")

Entry1=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry2=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry3=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry4=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry5=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry6=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry7=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry8=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry9=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry10=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry11=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
Entry12=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")

E1=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E2=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E3=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E4=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E5=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E6=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E7=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E8=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E9=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E10=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E11=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")
E12=Entry(mw,font="arial",width="15",fg="black",bg="aqua",border="5")



button1=Button(mw,text="Click to calculate sgp",bg="brown",font="5",command=call)
button2=Button(mw,text="Click to clear",bg="brown",command=del1)
button3=Button(mw,text="Click to clear",bg="brown",command=del2)
button4=Button(mw,text="Click to clear",bg="brown",command=del3)


label1.place(x=640,y=0)
label2.place(x=30,y=70)
label3.place(x=300,y=70)
label4.place(x=570,y=70)
label5.place(x=840,y=70)

entry1.place(x=30,y=140)
entry2.place(x=30,y=190)
entry3.place(x=30,y=240)
entry4.place(x=30,y=290)
entry5.place(x=30,y=340)
entry6.place(x=30,y=390)
entry7.place(x=30,y=440)
entry8.place(x=30,y=490)
entry9.place(x=30,y=540)
entry10.place(x=30,y=590)
entry11.place(x=30,y=640)
entry12.place(x=30,y=700)

Entry1.place(x=300,y=140)
Entry2.place(x=300,y=190)
Entry3.place(x=300,y=240)
Entry4.place(x=300,y=290)
Entry5.place(x=300,y=340)
Entry6.place(x=300,y=390)
Entry7.place(x=300,y=440)
Entry8.place(x=300,y=490)
Entry9.place(x=300,y=540)
Entry10.place(x=300,y=590)
Entry11.place(x=300,y=640)
Entry12.place(x=300,y=700)

E1.place(x=570,y=140)
E2.place(x=570,y=190)
E3.place(x=570,y=240)
E4.place(x=570,y=290)
E5.place(x=570,y=340)
E6.place(x=570,y=390)
E7.place(x=570,y=440)
E8.place(x=570,y=490)
E9.place(x=570,y=540)
E10.place(x=570,y=590)
E11.place(x=570,y=640)
E12.place(x=570,y=700)




button1.place(x=840,y=140)
button2.place(x=30,y=750)
button3.place(x=300,y=750)
button4.place(x=570,y=750)


string="  Instructions to use\n\n1.this can take 12 values of each column\nlike subject,credits,points each \nhas 12 entries.\n2.for sgpa calculations requires credits,poins scored.\nso subjects entries are optional\n\nNote:\nif you required less than 12 entries \nit means if u had only 5 subjects total\nthen enter 5 subjects credits and points \nand fill remaining all entries of credits,points\n columns entry values as 0"
Label(mw,text=string,font="5",fg="green",bg="yellow").place(x=1040,y=450)
mw.mainloop()
