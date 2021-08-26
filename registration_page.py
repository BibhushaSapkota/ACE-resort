from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import Login

class Register:
    def __init__(self,master):
        self.root2=master
        self.root2.title("registration form")
        self.root2.state('zoomed')

        self.load=Image.open('registration.png') #background picture
        self.bg=ImageTk.PhotoImage(self.load,master=self.root2)
        self.lbl=Label(self.root2,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.left=Image.open('sd.png')
        self.lg=ImageTk.PhotoImage(self.left,master=self.root2)
        self.lbl1=Label(self.root2,image=self.lg).place(x=200,y=150,width=425,height=600)

        frame1= Frame(self.root2,bg='white')
        frame1.place(x=625,y=150,width=700,height=600)

        title=Label(frame1,text='REGISTER HERE',font=("times new roman",30,'bold'),bg='white',fg='#65178a').place(x=50,y=30)

        #entry fields

        fname= Label(frame1, text='First Name', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_fname.place(x=50,y=130,width=250)

        lname= Label(frame1, text='Last Name', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_lname.place(x=370,y=130,width=250)

        contact= Label(frame1, text='Contact Number', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=160)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_contact.place(x=50,y=190,width=250)

        email= Label(frame1, text='Username', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=160)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_email.place(x=370,y=190,width=250)

        gender=Label(frame1, text='Gender', font=("times new roman", 15, 'bold'), bg='white',
              fg='#51375d').place(x=50, y=220)
        self.gender = ttk.Combobox(frame1, font=("times new roman", 12), state='readonly', justify=CENTER)
        self.gender['values'] = ('Select', 'Male', 'Female','non_binary')
        self.gender.place(x=50, y=250, width=250)
        self.gender.current(0)

        age= Label(frame1, text='Age', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=220)
        self.txt_age=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_age.place(x=370,y=250,width=250)

        password= Label(frame1, text='Password', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=280)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg='#bcb5c0',show="*")
        self.txt_password.place(x=50,y=310,width=250)
        confirm_password= Label(frame1, text='Confirm password', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=280)
        self.txt_confirm_password=Entry(frame1,font=("times new roman",15),bg='#bcb5c0',show='*')
        self.txt_confirm_password.place(x=370,y=310,width=250)

        question= Label(frame1, text='Security Question', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=340)
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",12),state='readonly',justify=CENTER)
        self.cmb_question['values']=('Select','In what city were you born?','What is your bestfriends name?',
                                'What was your favorite food as a child?')
        self.cmb_question.place(x=50,y=370,width=250)
        self.cmb_question.current(0)

        answer= Label(frame1, text='Answer', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=340)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_answer.place(x=370,y=370,width=250)

        self.terms_chk=IntVar()
        terms=Checkbutton(frame1,text='I Agree To The Terms and Conditions',variable=self.terms_chk,onvalue=1,offvalue=0,bg='white').place(x=50, y=420)


        register_btn=Button(frame1,text="  Register  ",bg='#9a90e4',command=self.register_data).place(x=50,y=500,width=250)
        login_btn=Button(frame1,text="   Login  ",bg='#9a90e4',command=self.login_window).place(x=370,y=500,width=250)
        self.root2.mainloop()
   

    def login_window(self):
        self.root2.destroy()
        Login.Login(Toplevel())



