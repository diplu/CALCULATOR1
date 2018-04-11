from Tkinter import *
def iCalc(source,side):
    Storeobj=Frame(source,borderwidth=4,bd=4,bg="powder blue")
    Storeobj.pack(side=side,expand=YES,fill=BOTH)
    return Storeobj
def button(source,side,text,command=None):
    Storeobj=Button(source,text=text,command=command)
    Storeobj.pack(side=side,expand=YES,fill=BOTH)
    return Storeobj
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*font','arial 20 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title('calculator')
        display=StringVar()
        Entry(self,relief=RIDGE,textvariable=display,justify='right',bd=30,bg='powder blue').pack(side=TOP,expand=YES,fill=BOTH)
        for clearbut in (["C"]):
            erase=iCalc(self,TOP)
            for ichar in  clearbut:
                button(erase,LEFT,ichar,lambda Storeobj=display, q=ichar: Storeobj.set(''))
        for NumBut in("789/","456*","123-", "0.+"):
            FunctionNum=iCalc(self,TOP)
            for iEquals in NumBut:
                     button(FunctionNum,RIGHT,iEquals,lambda Storeobj=display,q=iEquals:Storeobj.set(Storeobj.get()+q))
            EqualsButton=iCalc(self,TOP)
            for iEquals in "=":
                if iEquals=='=':
                    btniEquals=button(EqualsButton,LEFT,iEquals)
                    btniEquals.bind('<ButtonRelease-1>',lambda e,s=self,Storeobj=display:s.calc(Storeobj),'+')
                else:
                    btriEquals=button(EqualsButton,LEFT,iEquals,lambda Storeobj=display,s='%s'%iEquals:Storeobj.set(Stroeobj.get()+s))
    def calc(self,display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("Error")
if __name__ =='__main__':
    app().mainloop()
