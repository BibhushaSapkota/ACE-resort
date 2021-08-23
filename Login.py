from tkinter import *
from tkinter.tix import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import main_page
import registration_page


class Login:
    def __init__(self,master):
        self.root1 = master
        self.root1.title("Login")
        self.root1.state('zoomed')
        self.my_canvas = Canvas(self.root1)
        self.my_canvas.pack(fill="both", expand=True)
        self.login1 = ImageTk.PhotoImage(Image.open(f'login.png'),master=self.root1)
        self.img=Image.open('user.png')
        self.img=self.img.resize((55,45),Image.ANTIALIAS)
        self.user_img=ImageTk.PhotoImage(self.img,master=self.root1)
        self.login_btn_img = PhotoImage(file='in.png',master=self.root1)
        self.imgpass = Image.open('padlock.png')
        self.imgpass = self.imgpass.resize((55, 45), Image.ANTIALIAS)
        self.user_pass_img = ImageTk.PhotoImage(self.imgpass,master=self.root1)
        self.my_canvas.create_image(0, 0, image=self.login1, anchor="nw")
        self.my_canvas.create_image(610, 345, image=self.user_img, anchor="nw")
        self.my_canvas.create_image(610, 417, image=self.user_pass_img, anchor="nw")
        self.my_canvas.create_rectangle(1070, 600, 600, 90,outline = '#05035b',width=10)
        self.my_canvas.create_line(600, 225, 1070, 225,width=10,fill="#05035b")
        self.my_canvas.create_text(835, 130, text="REGISTER HERE", font=("Algerian", 40, 'bold'), fill="gold")
        self.register_btn = Button(self.root1, text="New user registration", bg="green", fg="white",
                                   font=("Rockwell nova", 18),
                                   cursor="hand2",
                                   border='0', overrelief="sunken",command=self.register_window)
        self.register_btn.place(x=720, y=160)
        self.my_canvas.create_text(850, 270, text="LOGIN HERE", font=("Algerian", 40, 'bold'), fill="gold")
        self.var123=IntVar()
        self.var123.set(1)
        Radiobutton(self.root1, text="USER", font=('times new roman', 16,'bold'),width=5, bg="royalblue2", variable=self.var123, value=1).place(x=750,y=300)
        Radiobutton(self.root1, text="ADMIN", font=('times new roman', 16,'bold'), bg="royalblue2", variable=self.var123,value=2).place(x=850, y=300)

        self.username_entry = Entry(self.root1, width=24, font=("Times New roman", 22, "bold"),justify='center', borderwidth=0,
                                    bg="snow3", fg="#05035b")
        self.username_entry.place(x=680, y=355)

        self.password_entry = Entry(self.root1, width=24,justify='center', font=("Times New roman", 22, "bold"), borderwidth=0,
                                    bg="snow3", fg="#05035b")
        self.my_canvas.create_window(680, 420, anchor="nw", window=self.password_entry)
        self.forget_btn = Button(self.root1, text="Forgot password",bg="red",fg="white",font=("Rockwell nova", 15), cursor="hand2",
                               border='0',overrelief="sunken")
        self.forget_btn.place(x=770, y=480)


        self.login_btn=Button(self.root1,text="",font=("Rockwell nova", 25),image=self.login_btn_img,command=self.login,cursor="hand2",borderwidth=0)
        self.login_btn.place(x=750,y=530)
        self.rounded_rect(self.my_canvas, 675, 350, 370, 42, 10)
        self.rounded_rect(self.my_canvas, 675, 415, 370, 42, 10)
        self.login_btn.bind("<Enter>",self.change)
        self.login_btn.bind("<Leave>", self.change_back)
        self.username_entry.bind("<FocusIn>",self.on_enter)
        self.username_entry.bind("<FocusOut>", self.on_leave)
        self.username_entry.insert(0,"Enter Username Here")
        self.password_entry.bind("<FocusIn>", self.on_enter1)
        self.password_entry.bind("<FocusOut>", self.on_leave1)
        self.password_entry.insert(0, "Enter Password Here")
        self.root1.mainloop()
    def register_window(self):
        self.root1.withdraw()
        registration_page.Register(Toplevel())


    def login(self):
        if self.username_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root1)
        else:
            try:
                con = mysql.connector.connect(
                    host='127.0.0.1',
                    user='root',
                    password='1235',
                    port=3306,
                    database='login_registration')
                cur = con.cursor()
                cur.execute("select * from registration where email=%s and password=%s", (self.username_entry.get(),self.password_entry.get()))
                row = cur.fetchone()
                if self.username_entry.get()=='admin' and self.password_entry.get()=='admin' and self.var123.get()==2:
                    messagebox.showinfo("Success", "Successful login", parent=self.root1)
                    self.root1.withdraw()
                    main_page.MainPage(Tk())
                elif self.username_entry.get()=='admin' and self.password_entry.get()=='admin' and self.var123.get()==1:
                    print(self.var123.get())
                    messagebox.showerror("Error", "Select currect authority", parent=self.root1)
                elif row==None:
                    messagebox.showerror("Error","Invalid username and password",parent=self.root1)
                elif row!=None and self.var123.get()==1:
                    messagebox.showinfo("Success","Successful login",parent=self.root1)
                    self.root1.withdraw()
                    main_page.MainPage(Toplevel())
                elif row!=None and self.var123.get()==2:
                    messagebox.showerror("Error", "Select currect authority", parent=self.root1)
                con.close()

            except:
                pass

    def on_enter(self,c):
        if self.username_entry.get() == "Enter Username Here":
            self.username_entry.delete(0,'end')

    def on_leave(self,c):
        if self.username_entry.get()=="":
            self.username_entry.insert(0,"Enter Username Here")
    def on_enter1(self,d):
        if self.password_entry.get() == "Enter Password Here":
            self.password_entry.delete(0,'end')
            self.password_entry.config(show="*")
    def on_leave1(self,d):
        if self.password_entry.get()=="":
            self.password_entry.config(show="")
            self.password_entry.insert(0,"Enter Password Here")


    def change(self,e):
        self.login_btn_img1=PhotoImage(file='out.png',master=self.root1)
        self.login_btn.config(image=self.login_btn_img1,borderwidth=0)
        self.login_btn.image=self.login_btn_img1
    def change_back(self,e):
        self.login_btn_img1=PhotoImage(file='in.png',master=self.root1)
        self.login_btn.config(image=self.login_btn_img1,borderwidth=0)
        self.login_btn.image=self.login_btn_img1

    def rounded_rect(self, my_canvas, x, y, w, h, c):
        self.my_canvas.create_arc(x, y, x + 2 * c, y + 2 * c, start=90, extent=90, style="arc", width=10)
        self.my_canvas.create_arc(x + w - 2 * c, y + h - 2 * c, x + w, y + h, start=270, extent=90, style="arc",
                                  width=10)
        self.my_canvas.create_arc(x + w - 2 * c, y, x + w, y + 2 * c, start=0, extent=90, style="arc", width=10)
        self.my_canvas.create_arc(x, y + h - 2 * c, x + 2 * c, y + h, start=180, extent=90, style="arc", width=10)
        self.my_canvas.create_line(x + c, y, x + w - c, y, fill="black", width=10)
        self.my_canvas.create_line(x + c, y + h, x + w - c, y + h, fill="black", width=10)
        self.my_canvas.create_line(x, y + c, x, y + h - c, fill="black", width=10)
        self.my_canvas.create_line(x + w, y + c, x + w, y + h - c, fill="black", width=10)
