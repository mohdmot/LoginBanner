# Login Banner
# With Tkiner GUI
#
# By Zaky
#
# You Can Use it for Your Scripts
# Only Replace "Logo.png" With Your Logo
#
#
# Enjoy !!!


from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class OBJ () :
    def __init__ (self,root) :
        def login () :
            username=str(UserVar.get())
            password=str(PassVar.get())
            print(f'User : {username}\nPass : {password}')
        def passText (e):
            PassEntry.delete(0, END)
            PassEntry['show']='*'
        def userText (e):
            UserEntry.delete(0, END)
        Label(root,width=300,height=300,bg='#090909').place(x=0,y=0)
        Label(root,text='Login',font=('Arial Black',28),fg='#ffffff',bg='#090909').place(x=95,y=95)
        Label(root,width=300,height=6,bg='#000000').place(x=0,y=0)
        Label(root,width=300,height=300,bg='#000000').place(x=0,y=285)
        logo1=Image.open('Logo.png')
        self.Logo = ImageTk.PhotoImage(logo1)
        Label(image=self.Logo,bd=0).place(x=50,y=5)
        ##############################################################
        UserVar=StringVar() #
        PassVar=StringVar() #
        #####################
        UserEntry=ttk.Entry(root,width=45,textvariable=UserVar)
        UserEntry.place(x=25,y=160)
        UserEntry.bind("<Button>",userText)
        UserEntry.insert(0,'<Usename>')
        #
        PassEntry=ttk.Entry(root,width=45,textvariable=PassVar)
        PassEntry.place(x=25,y=210)
        PassEntry.bind("<Button>",passText)
        PassEntry.insert(0,'<Password>')
        ########################################
        ttk.Button(text='Login',command=login).place(x=110,y=245)
        ErrorVar=StringVar()
        Label(textvariable=ErrorVar,fg='#f42626',font=('Calibri',10),bg='#000000').place(x=70,y=297)
        ##############################################################

if __name__ == '__main__':
    Gui=Tk()
    Gui.title('Login')
    #Gui.iconbitmap('Your-icon-File.ico')
    Add=OBJ(Gui)
    Gui.geometry('330x330')
    Gui.mainloop()