from tkinter import *
exp=''
def GetValue(event):
    global exp
    v=event.widget.cget("text")

    if v=="Clear":
        exp=''
        val.set('')
        screen.update()
    elif v=='=':
        cal=str(eval(exp))
        val.set(cal)
        screen.update()
    else:
        exp=exp+v
        val.set(exp)
        screen.update()
        

root=Tk()
root.geometry()

val=StringVar()

screen=Entry(root,text=val,font='black 35 bold',fg="black",bg="yellow")
screen.pack()
f=Frame(root)

b=Button(f,text="Clear",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text=".",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="=",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

f.pack()
f=Frame(root)

b.bind("<Button-1>",GetValue)

b=Button(f,text="1",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="2",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="3",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

f.pack()
f=Frame(root)
b.bind("<Button-1>",GetValue)

b=Button(f,text="4",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="5",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="6",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

f.pack()
f=Frame(root)

b.bind("<Button-1>",GetValue)

b=Button(f,text="7",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="8",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="9",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

f.pack()
f=Frame(root)

b.bind("<Button-1>",GetValue)

b=Button(f,text="0",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)


f.pack()
f=Frame(root)

b.bind("<Button-1>",GetValue)

b=Button(f,text="/",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="*",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="-",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

b.bind("<Button-1>",GetValue)

b=Button(f,text="+",padx=30,font="lucida 35 bold")
b.pack(side="left",padx=20,pady=10)

f.pack()
f=Frame(root)

b.bind("<Button-1>",GetValue)

root.mainloop()