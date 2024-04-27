from tkinter import
coro = Tk()
coro.title("Corona Virus Information")
coro.geometry('800x500+200+100')
coro.configure(bg= '#046173')
coro.iconbitmap('corona.ico')   #download only ico files




###Labels
mainlabel = Label(coro,text="Corona Virus Live Tracker" ,font=("Times 20 bold" ,30, "bold"), bg = "#05897A" ,width=33
                  ,fg = "black" ,bd=5)
mainlabel.place(x=0,y=0)


label1 = Label(coro,text="Country Name" ,font=("arial",20,"italic bold"), bg = "#046173")
label1.place(x=15,y=100)

label2 = Label(coro,text="Download File in ",font = ("arial",20,"italic bold"), bg = "#046173")
label2.place(x=15,y=200)

cntdata = StringVar()
entry1 = Entry(coro,textvariable = cntdata ,font = ("arial",15,"italic bold"),relief = RIDGE,bd = 2 , width = 32)
entry1.place(x = 280, y = 100)

#### BUTTONS

Inhtml = Button(coro,text = "Html", bg = "#2DAE9A", font = ("arial",15,"italic bold"),relief = RIDGE,activebackground = "#05945B" )