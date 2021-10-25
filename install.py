#!/usr/bin/python3
# Black-Webbrowser v1.5
import os,subprocess
try:
    from tkinter import *
    from tkinter.ttk import *
    from ttkbootstrap import Style
except ImportError:
    subprocess.getoutput("pip install tk-tools")

class black_webbrowser(Tk):
    def __init__(self):
        super(black_webbrowser,self).__init__()
        self.title('black-Webbrowser/Installing')
        self.photo = PhotoImage(file = './Scr/black.png')
        self.style = Style("cyborg")
        label_l = Label(self,text='black-Webbrowser',background='white',foreground='black',font=("None",15))
        label_l.place(bordermode=INSIDE,x=120,y=20)
        self.install_b = Button(self,text='Install',width=9,command=self.install)
        self.install_b.place(bordermode=OUTSIDE,x=160,y=110)
        self.exit_b = Button(self,text='Exit',width=9,command=self.ext)
        self.exit_b.place(bordermode=OUTSIDE,x=160,y=145)

        self.config(background='white')
        self.iconphoto(False,self.photo)
        self.resizable(False,False)
        self.geometry("400x300")
        self.mainloop()
    def install(self):
        global pr
        pr = Progressbar(self,orient='horizontal',mode='determinate',length=200)
        pr.place(bordermode=INSIDE,x=105,y=65)
        pr.start(55)
        pr.after(6000,self.install_2)
    def install_2(self):
        subprocess.getoutput("chmod a+x black.py")
        pr.stop()
        pr.destroy()
        label_mess = Label(self,text='Complete!',foreground='black',background='white')
        label_mess.place(bordermode=INSIDE,x=170,y=65)
        self.install_b.destroy()
        self.exit_b.place(bordermode=OUTSIDE,x=160,y=110)

    def ext(self):
        self.destroy()
        self.quit()
        quit()
if __name__ == '__main__':
    window = black_webbrowser()
