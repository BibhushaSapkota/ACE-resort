from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
from time import sleep
import room
import Login
import Menu
class MainPage:
    def __init__(self,master):
        self.root3 = master
        self.root3.title("Main")
        self.root3.geometry("%dx%d+0+0" % (self.root3.winfo_screenwidth(), self.root3.winfo_screenheight()))
        self.my_canvas = Canvas(self.root3)
        self.my_canvas.pack(fill="both", expand=True)
        self.background = ImageTk.PhotoImage(Image.open('background.png'),master=self.root3)
        self.male = ImageTk.PhotoImage(Image.open('male.png'), master=self.root3)
        self.female = ImageTk.PhotoImage(Image.open('female.png'), master=self.root3)
        self.my_canvas.create_image(0, 0, image=self.background, anchor="nw")
        self.ace_images()
        self.buttons()
        self.menu_main_frame()
        self.gender_part()
        self.result=self.convertTuple(self.row1)
        print(self.result)
        self.user_name=Label(self.root3,text=self.us_name,font=("Rockwell nova", 40,'bold'),fg="Green")
        self.user_name.place(x=1100, y=10)
        if self.result=='Male':
            self.Mr = Label(self.root3, text='Mr', font=("Rockwell nova", 40, 'bold'), fg="Green")
            self.Mr.place(x=980, y=10)
            self.my_canvas.create_image(900, 10, image=self.male, anchor="nw")
        else:
            self.Mrs = Label(self.root3, text='Miss', font=("Rockwell nova", 40, 'bold'), fg="Green")
            self.Mrs.place(x=980, y=10)
            self.my_canvas.create_image(900, 10, image=self.female, anchor="nw")
        self.root3.update()
        self.root3.mainloop()

    def convertTuple(self,tup):
        str = ''.join(tup)
        return str
    def gender_part(self):
        self.us_name=Login.gett()
        query = "select gender from registration where username=%s"
        try:
            con1 = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')

            cur1 = con1.cursor()
            cur1.execute(query, (self.us_name,))
            self.row1 = cur1.fetchone()
            con1.close()
        except:
            print('error')
            pass

    def ace_images(self):
        # now set an image for moving
        self.img1 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace.png"),master=self.root3)  # make sure that you have a photo
        # in you current folder that you are working with
        self.img2 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace1.png"),master=self.root3)
        self.img3 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace2.png"),master=self.root3)
        self.img4 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace3.png"),master=self.root3)
        # Create a label
        self.l = Label(self.root3, font="bold")
        self.l.place(x=20, y=0)
        # take a variable
        self.x = 1
        self.ace_move()


    def ace_move(self):
        if self.x == 5:
            self.x = 1
        if self.x == 1:
            self.l.config(image=self.img1)  # by writing this line first picture will appear
        elif self.x == 2:
            self.l.config(image=self.img2)
        elif self.x == 3:
            self.l.config(image=self.img3)
        elif self.x == 4:
            self.l.config(image=self.img4)
        # you can do it for thousands of images
        # now increase the count by one
        self.x += 1
        # set images to work automatically by "after" feature in tkinter
        self.root3.after(1500, self.ace_move)



    def buttons(self):
        self.menu_img = ImageTk.PhotoImage(Image.open('menu.png'),master=self.root3)
        self.menu_change_img = ImageTk.PhotoImage(Image.open('menu_change.png'),master=self.root3)
        self.bill_img= ImageTk.PhotoImage(Image.open('bill.png'),master=self.root3)
        self.bill_change_img = ImageTk.PhotoImage(Image.open('bill_change.png'),master=self.root3)
        self.about_img = ImageTk.PhotoImage(Image.open('information.png'),master=self.root3)
        self.about_change_img = ImageTk.PhotoImage(Image.open('information_change.png'),master=self.root3)
        self.profile_img = ImageTk.PhotoImage(Image.open('profile.png'),master=self.root3)
        self.profile_change_img = ImageTk.PhotoImage(Image.open('profile_change.png'),master=self.root3)
        self.review_img = ImageTk.PhotoImage(Image.open('review.png'),master=self.root3)
        self.review_change_img = ImageTk.PhotoImage(Image.open('review_change.png'),master=self.root3)

        self.menu_btn= Button(self.root3, text="      MENU", fg="white",image=self.menu_change_img,
                                   font=("Rockwell nova", 20,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.menu_main_frame)
        self.menu_btn.place(x=30,y=150)
        self.bill_btn = Button(self.root3, text="   BILL", fg="white", image=self.bill_img,
                               font=("Rockwell nova", 20, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER, command=self.fn_bill)
        self.bill_btn.place(x=30, y=240)


        self.about_btn = Button(self.root3, text="ABOUT US", fg="white", image=self.about_img,
                               font=("Rockwell nova", 20,'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER,command=lambda:self.fn_about())
        self.about_btn.place(x=30, y=330)

        self.profile_btn = Button(self.root3, text="PROFILE", fg="white", image=self.profile_img,
                                  font=("Rockwell nova", 20,'bold'),
                                  cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER,command=lambda:self.fn_profile())
        self.profile_btn.place(x=30, y=420)

        self.review_btn = Button(self.root3, text="      REVIEW", fg="white", image=self.review_img,
                               font=("Rockwell nova", 20,'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER,command=self.fn_review)
        self.review_btn.place(x=30, y=510)
        self.standardroom_img = ImageTk.PhotoImage(Image.open('button.png'), master=self.root3)
        self.logout = Button(self.root3,fg="red", text="LOGOUT", image=self.standardroom_img,
                               font=("Rockwell nova", 20,'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER,
                             command=self.logout_fn)
        self.logout.place(x=30, y=600)

    def logout_fn(self):
        MsgBox = messagebox.askquestion('Logout', 'Are you sure you want to logout',
                                        icon='warning')
        if MsgBox == 'yes':
            self.root3.withdraw()
            Login.Login(Toplevel())
        else:
            pass
    def menu_main_frame(self):
        self.menu_btn.config(image=self.menu_change_img, fg='green')
        self.bill_btn.config(image=self.bill_img, fg='white')
        self.about_btn.config(image=self.about_img, fg='white')
        self.profile_btn.config(image=self.profile_img, fg='white')
        self.review_btn.config(image=self.review_img, fg='white')

        self.frame_main = LabelFrame(self.root3, height=550, width=1040, borderwidth=10)
        self.frame_main.place(x=300, y=130)
        self.frame_main.pack_propagate(False)


        self.frame_room = LabelFrame(self.frame_main, height=530, width=340, borderwidth=10)
        self.frame_room.place(x=0, y=0)
        self.frame_room.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_room)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.room_close = ImageTk.PhotoImage(Image.open(f'room/room1.png'),master=self.root3)
        self.my_canvas_room.create_image(60, 300, image=self.room_close, anchor="nw")
        self.frame_room.bind("<Enter>", self.change_room)
        self.frame_room.bind("<Leave>", self.change_back_room)
        self.topic_room = Label(self.frame_room, text='ROOM', font=("Algerian", 40, 'bold'))
        self.topic_room.place(x=90, y=50)
        self.point_img2 = ImageTk.PhotoImage(Image.open(f'point.png'), master=self.root3)
        self.my_canvas_room.create_image(130, 140, image=self.point_img2, anchor="nw")

        self.room_btn = Button(self.frame_room, text="BOOK HERE", bg="green", fg="white", cursor="hand2",
                              font=("Rockwell nova", 25, 'bold'), command=self.room_fn)
        self.room_btn.place(x=50, y=210)



        self.frame_food = LabelFrame(self.frame_main, height=530, width=340, borderwidth=10)
        self.frame_food.place(x=340, y=0)
        self.frame_food.pack_propagate(False)
        self.my_canvas_food = Canvas(self.frame_food)
        self.my_canvas_food.pack(fill="both", expand=True)
        self.food_close = ImageTk.PhotoImage(Image.open(f'food/food1.png'),master=self.root3)
        self.my_canvas_food.create_image(75, 320, image=self.food_close, anchor="nw")
        self.frame_food.bind("<Enter>", self.change_food)
        self.frame_food.bind("<Leave>", self.change_back_food)
        self.topic_food = Label(self.frame_food, text='FOOD', font=("Algerian", 40, 'bold'))
        self.topic_food.place(x=90, y=50)
        self.point_img1 = ImageTk.PhotoImage(Image.open(f'point.png'), master=self.root3)
        self.my_canvas_food.create_image(130, 140, image=self.point_img1, anchor="nw")
        self.food_btn = Button(self.frame_food, text="ORDER HERE", bg="green", fg="white", cursor="hand2",
                              font=("Rockwell nova", 25, 'bold'), command=self.menu)
        self.food_btn.place(x=50, y=210)



        self.frame_cab = LabelFrame(self.frame_main, height=530, width=340, borderwidth=10)
        self.frame_cab.place(x=680, y=0)
        self.frame_cab.pack_propagate(False)
        self.my_canvas_cab = Canvas(self.frame_cab)
        self.my_canvas_cab.pack(fill="both", expand=True)



        self.cab_close = ImageTk.PhotoImage(Image.open(f'cab/cab1.png'),master=self.root3)
        self.my_canvas_cab.create_image(75, 320, image=self.cab_close, anchor="nw")
        self.frame_cab.bind("<Enter>", self.change_cab)
        self.frame_cab.bind("<Leave>", self.change_back_cab)
        self.topic_cab = Label(self.frame_cab, text='CAB \nSERVICE', font=("Algerian", 40, 'bold'))
        self.topic_cab.place(x=50, y=5)
        self.point_img = ImageTk.PhotoImage(Image.open(f'point.png'), master=self.root3)
        self.my_canvas_cab.create_image(130, 140, image=self.point_img, anchor="nw")
        self.cab_btn=Button(self.frame_cab,text="BOOK HERE",bg="green",fg="white",cursor="hand2",font=("Rockwell nova", 25,'bold'),command=self.cab_fn)
        self.cab_btn.place(x=50,y=210)



    def change_room(self,e):
        self.animation('room','room',60,300,self.my_canvas_room)
    def change_back_room(self,e):
        self.room_close = ImageTk.PhotoImage(Image.open(f'room/room1.png'),master=self.root3)
        self.my_canvas_room.create_image(60, 300, image=self.room_close, anchor="nw")
    def change_food(self,f):
        self.animation('food','food',75,320,self.my_canvas_food)
    def change_back_food(self,f):
        self.food_close = ImageTk.PhotoImage(Image.open(f'food/food1.png'),master=self.root3)
        self.my_canvas_food.create_image(75, 320, image=self.food_close, anchor="nw")
    def change_cab(self,g):
        self.animation('cab','cab',75,320,self.my_canvas_cab)
    def change_back_cab(self,g):
        self.cab_close = ImageTk.PhotoImage(Image.open(f'cab/cab1.png'),master=self.root3)
        self.my_canvas_cab.create_image(75, 320, image=self.cab_close, anchor="nw")
    def room_fn(self):
        room.Roompage(Toplevel())

    def menu(self):
        Menu.run(Toplevel())


    def fn_bill(self):
        self.frame_bill = LabelFrame(self.root3, height=550, width=1050, borderwidth=10)
        self.frame_bill.place(x=300, y=130)

        self.frame_bill.pack_propagate(False)
        self.my_canvas_bill = Canvas(self.frame_bill)
        self.my_canvas_bill.pack(fill="both", expand=True)
        self.bill_bg_img = ImageTk.PhotoImage(Image.open(f'profile_bg.png'), master=self.root3)
        self.my_canvas_bill.create_image(0, 0, image=self.bill_bg_img, anchor="nw")
        self.name_fn = 'bill'
        self.img_change()

        self.my_canvas_bill.create_text(500, 100, text="Billing", font=("Algerian", 40),
                                           fill="white")

        self.my_canvas_bill.create_text(200, 200, text="Room Total Price :", font=("Arial", 18),
                                        fill="white")

        self.my_canvas_bill.create_text(450, 200, text="Food Total Price :", font=("Arial", 18),
                                        fill="white")

        self.my_canvas_bill.create_text(750, 200, text="Custom Burger Total Price :", font=("Arial", 18),
                                        fill="white")

        self.frame_main.place_forget()


        self.room_total=0
        self.display=Label(self.frame_bill,text="",font=("times new roman", 15, 'bold'))
        self.display.place(x=120,y=250)
        self.display_menu=Label(self.frame_bill,text="",font=("times new roman", 15, 'bold'))
        self.display_menu.place(x=380,y=250)
        self.display_burgar = Label(self.frame_bill, text="", font=("times new roman", 15, 'bold'))
        self.display_burgar.place(x=640, y=250)
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from room_book where username=%s", (self.us_name,))
            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    if row[1]=="Room:1":
                        self.room_total = 5000+self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:2":
                        self.room_total = 5000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:3":
                        self.room_total = 5000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:4":
                        self.room_total = 5000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:5":
                        self.room_total = 5000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:6":
                        self.room_total = 7000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:7":
                        self.room_total = 7000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:8":
                        self.room_total = 7000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:9":
                        self.room_total = 7000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Room:10":
                        self.room_total = 7000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Villa:11":
                        self.room_total = 15000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Villa:12":
                        self.room_total = 15000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Villa:13":
                        self.room_total = 15000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Villa:14":
                        self.room_total = 15000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Villa:15":
                        self.room_total = 15000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Hall:16":
                        self.room_total = 50000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Hall:17":
                        self.room_total = 70000 + self.room_total
                        self.display.config(text=self.room_total)
                    if row[1]=="Hall:18":
                        self.room_total = 100000 + self.room_total
                        self.display.config(text=self.room_total)
                con.close()
        except:
            print("sjkjfsd")
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from menu where username=%s", (self.us_name,))
            result1 = cur.fetchall()
            print("abc")
            print(result1)
            self.food_total=0
            if len(result1) != 0:
                for row in result1:
                    print(row[0])
                    if row[1] != "0":
                        self.food_total = 190 * int(row[1]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[2] != "0":
                        self.food_total = 150 * int(row[2]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[3] != "0":
                        self.food_total = 120 * int(row[3]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[4] != "0":
                        self.food_total = 450 * int(row[4]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[5] != "0":
                        self.food_total = 390 * int(row[5]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[6] != "0":
                        self.food_total = 350 * int(row[6]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[7] != "0":
                        self.food_total = 250 * int(row[7]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[8] != "0":
                        self.food_total = 290 * int(row[8]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[9] != "0":
                        self.food_total = 300 * int(row[9]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[10] != "0":
                        self.food_total = 300 * int(row[10]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[11] != "0":
                        self.food_total = 350 * int(row[11]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[12] != "0":
                        self.food_total = 100 * int(row[12]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[13] != "0":
                        self.food_total = 200 * int(row[13]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[14] != "0":
                        self.food_total = 500 * int(row[14]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[15] != "0":
                        self.food_total = 600 * int(row[15]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[16] != "0":
                        self.food_total = 530 * int(row[16]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[17] != "0":
                        self.food_total = 200 * int(row[7]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[18] != "0":
                        self.food_total = 500 * int(row[18]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[19] != "0":
                        self.food_total = 600 * int(row[19]) + self.food_total
                        self.display_menu.config(text=self.food_total)
                    if row[20] != "0":
                        self.food_total = 530 * int(row[20]) + self.food_total
                        self.display_menu.config(text=self.food_total)

        except:
            print("kau")
            print('error')
            pass

        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from burgar where username=%s", (self.us_name,))
            result2 = cur.fetchall()
            print(result2)

            self.burgar_total = 0
            if len(result2) != 0:
                for row in result2:
                    print(row[8])
                    if row[8] != None:
                        self.burgar_total = int(row[8]) + self.burgar_total
                        self.display_burgar.config(text=self.burgar_total)
        except:
            print('error')
            pass
        self.pay = Button(self.frame_bill,bg="green",fg="white", text="PAY",command=self.pay_fn, font=("times new roman", 20, 'bold'))
        self.pay.place(x=450, y=350)
        self.img_change()

    def pay_fn(self):
        MsgBox = messagebox.askquestion('Pay', 'Are you sure you want to pay',
                                        icon='warning')
        if MsgBox == 'yes':
            self.display.config(text="0")
            self.display_menu.config(text="0")
            self.display_burgar.config(text="0")
        else:
            pass

    def fn_about(self):
        self.frame_about_in = LabelFrame(self.root3, height=550, width=1040, borderwidth=0)
        self.frame_about_in.place(x=300, y=130)
        self.frame_about_in.pack_propagate(False)
        self.my_canvas_about_in = Canvas(self.frame_about_in)
        self.my_canvas_about_in.pack(fill="both", expand=True)
        self.about_bg_img = ImageTk.PhotoImage(Image.open(f'about_bg.png'), master=self.root3)
        self.my_canvas_about_in.create_image(0, 0, image=self.about_bg_img, anchor="nw")
        self.name_fn = 'about'
        self.img_change()

        # image
        self.about_feature_img = ImageTk.PhotoImage(Image.open(f'about_feature.png'), master=self.root3)
        self.my_canvas_about_in.create_image(75, 230, image=self.about_feature_img, anchor="nw")

        # Text
        self.my_canvas_about_in.create_text(450, 40, text="ABOUT US", font=("Algerian", 45), fill="white")
        self.my_canvas_about_in.create_text(530, 120, text="Located in the Pokhara, Ace Resort is a perfect weekend getaway for families looking for  a place \n to relax away from the hustle and bustle  of the cities. The place provides a refreshing break from the\n crowd of the city giving you a place to relax and spend some quality time with your family.", font=("Times new roman", 17),
                                            fill="white")
        self.my_canvas_about_in.create_text(500, 210, text="SPECIAL FEATURES", font=("Algerian", 40, 'bold'),
                                            fill="gold")

    def fn_profile(self):
        self.frame_profile = LabelFrame(self.root3, height=550, width=1050, borderwidth=10)
        self.frame_profile.place(x=300, y=130)

        self.frame_profile.pack_propagate(False)
        self.my_canvas_profile = Canvas(self.frame_profile)
        self.my_canvas_profile.pack(fill="both", expand=True)
        self.profile_bg_img = ImageTk.PhotoImage(Image.open(f'profile_bg.png'), master=self.root3)
        self.my_canvas_profile.create_image(0, 0, image=self.profile_bg_img, anchor="nw")
        self.name_fn = 'profile'
        self.img_change()

        self.my_canvas_profile.create_text(480, 100, text="Personal and Account Settings", font=("Arial", 35),
                                           fill="white")

        self.my_canvas_profile.create_text(285, 150, text="First Name", font=("times new roman", 15), fill="white")

        self.txt_fname = Entry(self.frame_profile, font=("times new roman", 15), bg='#bcb5c0')
        self.txt_fname.place(x=220, y=170, width=250)

        self.my_canvas_profile.create_text(580, 150, text="Last Name", font=("times new roman", 15), fill="white")

        self.txt_lname = Entry(self.frame_profile, font=("times new roman", 15), bg='#bcb5c0')
        self.txt_lname.place(x=550, y=170, width=250)

        self.my_canvas_profile.create_text(270, 230, text="Contact Number", font=("times new roman", 15),
                                           fill="white")

        self.txt_contact = Entry(self.frame_profile, font=("times new roman", 15), bg='#bcb5c0')
        self.txt_contact.place(x=220, y=250, width=250)

        self.my_canvas_profile.create_text(250, 310, text="Gender", font=("times new roman", 15), fill='white')

        self.gender = ttk.Combobox(self.frame_profile, font=("times new roman", 12), state='readonly',
                                   justify=CENTER)
        self.gender['values'] = ('Select', 'Male', 'Female')
        self.gender.place(x=220, y=330, width=250)
        self.gender.current(0)

        self.my_canvas_profile.create_text(560, 230, text="Age", font=("times new roman", 15), fill="white")

        self.txt_age = Entry(self.frame_profile, font=("times new roman", 15), bg='#bcb5c0')
        self.txt_age.place(x=550, y=250, width=250)

        self.my_canvas_profile.create_text(580, 310, text="Password", font=("times new roman", 15), fill="white")

        self.txt_password = Entry(self.frame_profile, font=("times new roman", 15), bg='#bcb5c0', show="*")
        self.txt_password.place(x=550, y=330, width=250)


        self.update_profile = Button(self.frame_profile, text=" Update ", command=self.update, bg="#BA7AD1",
                                     fg="#350345",
                                     font=("Times new roman", 20, 'bold'))
        self.update_profile.place(x=400, y=380, width=200)
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from registration where username=%s", (self.us_name,))
            row = cur.fetchone()
            self.txt_fname.insert(0, row[0])
            self.txt_lname.insert(0, row[1])
            self.txt_contact.insert(0, row[2])
            self.gender.set(row[4])
            self.txt_age.insert(0, row[5])
            self.txt_password.insert(0, row[6])
        except:
            print("error")
            pass

    def update(self):
        try:
            con5 = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')
            cursor = con5.cursor()
            print(cursor)
            sql_update = "update registration set fname=%s,lname=%s,contact_number=%s,gender=%s,age=%s,password=%s where username=%s"
            val = (
            self.txt_fname.get(), self.txt_lname.get(), self.txt_contact.get(), self.gender.get(), self.txt_age.get(),
            self.txt_password.get(), self.us_name,)
            cursor.execute(sql_update, val)
            con5.commit()
        except:
            pass
    def fn_review(self):
        self.frame_review = LabelFrame(self.root3, height=550, width=1050, borderwidth=10)
        self.frame_review.place(x=300, y=130)

        self.frame_review.pack_propagate(False)
        self.my_canvas_review = Canvas(self.frame_review)
        self.my_canvas_review.pack(fill="both", expand=True)
        self.review_bg_img = ImageTk.PhotoImage(Image.open(f'review_bg.png'), master=self.root3)
        self.my_canvas_review.create_image(0, 0, image=self.review_bg_img, anchor="nw")
        self.my_canvas_review.create_text(430, 25, text="WRITE A REVIEW", font=("Algerian", 50),
                                           fill="black")
        self.name_fn = 'review'
        self.img_change()

        self.review_entry1 = Text(self.frame_review, height=11, width=51, font=("Times new roman", 12, 'bold'), border=5)
        self.review_entry1.place(x=165, y=70)
        self.submit_btn = Button(self.frame_review, text="  Submit  ", bg="#BA7AD1", fg="#350345",
                               font=("Times new roman", 14, 'bold'), command=self.review)
        self.submit_btn.place(x=325, y=294)



    def img_change(self):

        if self.name_fn=='menu':
            self.menu_btn.config(image=self.menu_change_img, fg='green')
            self.bill_btn.config(image=self.bill_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.review_btn.config(image=self.review_img, fg='white')


        elif self.name_fn=='bill':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.bill_btn.config(image=self.bill_change_img,fg='green')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.review_btn.config(image=self.review_img, fg='white')


        elif self.name_fn=='about':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.bill_btn.config(image=self.bill_img,fg='white')
            self.about_btn.config(image=self.about_change_img, fg='green')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.review_btn.config(image=self.review_img, fg='white')

            self.frame_main.place_forget()
        elif self.name_fn=='profile':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.bill_btn.config(image=self.bill_img,fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_change_img, fg='green')
            self.review_btn.config(image=self.review_img, fg='white')

            self.frame_main.place_forget()
        else:
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.bill_btn.config(image=self.bill_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.review_btn.config(image=self.review_change_img, fg='green')

            self.frame_main.place_forget()

    def animation(self,name,type,x,y,any):
        for i in range(1, 5):
            self.room_img = ImageTk.PhotoImage(Image.open(f'{name}/{type}{i}.png'),master=self.root3)
            any.create_image(x, y, image=self.room_img, anchor="nw")
            sleep(0.1)
            self.root3.update_idletasks()

    def cab_fn(self):
        self.frame_main.place_forget()
        self.frame_cab_in = LabelFrame(self.root3, height=550, width=1040, borderwidth=0)
        self.frame_cab_in.place(x=300, y=130)
        self.frame_cab_in.pack_propagate(False)
        self.my_canvas_cab_in = Canvas(self.frame_cab_in)
        self.my_canvas_cab_in.pack(fill="both", expand=True)
        self.cab_bg_img = ImageTk.PhotoImage(Image.open(f'cab_bg.png'), master=self.root3)
        self.my_canvas_cab_in.create_image(0, 0, image=self.cab_bg_img, anchor="nw")

        self.my_canvas_cab_in.create_text(450, 80, text="BOOK A TAXI", font=("Algerian", 45), fill="white")
        self.my_canvas_cab_in.create_text(240, 150, text="Pick up address:", font=("Times new roman", 20),
                                          fill="white")
        self.my_canvas_cab_in.create_text(230, 300, text="Drop off  address:", font=("Times new roman", 20),
                                          fill="white")
        self.my_canvas_cab_in.create_text(250, 200, text="Pick up Date:", font=("Times new roman", 20),
                                          fill="white")
        self.my_canvas_cab_in.create_text(250, 350, text="Drop off Date:", font=("Times new roman", 20),
                                          fill="white")

        self.pick_ent = Entry(self.frame_cab_in, bg="#05035b", fg="white", font=("Times new roman", 20), width=20)
        self.pick_ent.place(x=350, y=130)
        self.pick_btn = Button(self.frame_cab_in, text=" Book pick up ", bg="#BA7AD1", fg="#350345",
                               font=("Times new roman", 16, 'bold'),command=self.pickup)
        self.pick_btn.place(x=300, y=230)

        self.drop_ent = Entry(self.frame_cab_in, bg="#05035b", fg="white", font=("Times new roman", 20), width=20)
        self.drop_ent.place(x=350, y=280)
        self.drop_btn = Button(self.frame_cab_in, text=" Book drop off ", bg="#BA7AD1", fg="#350345",
                               font=("Times new roman", 16, 'bold'),command=self.dropoff)
        self.drop_btn.place(x=300, y=380)

        # dropdowns
        self.options = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ]
        self.clicked = StringVar()
        self.clicked.set("Sunday")

        self.drop = OptionMenu(self.frame_cab_in, self.clicked, *self.options)
        self.drop.place(x=450, y=190)

        self.options2 = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20", "21", "22", "23", "24", "25",
            "26", "27", "28", "29", "30", "31", "32"
        ]
        self.clickeddate = StringVar()
        self.clickeddate.set("1")

        self.dropdate = OptionMenu(self.frame_cab_in, self.clickeddate, *self.options2)
        self.dropdate.place(x=555, y=190)

        self.options3 = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        self.clickedmonth = StringVar()
        self.clickedmonth.set("January")

        self.dropmonth = OptionMenu(self.frame_cab_in, self.clickedmonth, *self.options3)
        self.dropmonth.place(x=350, y=190)

        # dropdown for drop off
        self.optionsd1 = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ]
        self.clickedd1 = StringVar()
        self.clickedd1.set("Sunday")

        self.dropd1 = OptionMenu(self.frame_cab_in, self.clickedd1, *self.optionsd1)
        self.dropd1.place(x=450, y=340)

        self.optionsd2 = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20", "21", "22", "23", "24", "25",
            "26", "27", "28", "29", "30", "31", "32"
        ]
        self.clickeddated2 = StringVar()
        self.clickeddated2.set("1")

        self.dropdated2 = OptionMenu(self.frame_cab_in, self.clickeddated2, *self.optionsd2)
        self.dropdated2.place(x=555, y=340)

        self.optionsd3 = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        self.clickedmonthd3 = StringVar()
        self.clickedmonthd3.set("January")

        self.dropmonthd3 = OptionMenu(self.frame_cab_in, self.clickedmonthd3, *self.optionsd3)
        self.dropmonthd3.place(x=350, y=340)

    def clearpickup(self):
        self.pick_ent.delete(0,END)
        self.drop_ent.delete(0,END)
        self.clickeddated2.set("1")
        self.clickedd1.set("Sunday")
        self.clickedmonthd3.set("January")
        self.clickedmonth.set("January")
        self.clickeddate.set("1")
        self.clicked.set("Sunday")

    def pickup(self):
        self.us_name = Login.gett()
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')
            cur = con.cursor()


            username= self.us_name
            pickup_address= self.pick_ent.get()
            month=self.clickedmonth.get()
            day=self.clicked.get()
            date=self.clickeddate.get()
            sql = "insert into pickup(username,pickup_address,month,day,date)" "values ('" + username + "','" +pickup_address+ "','" +month+ "','" +day+ "','" +date+"')"
            values = cur.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo("success", "Your cab has been  booked", parent=self.root3)
            self.clearpickup()

        except:
            print("error")

    def dropoff(self):
        self.us_name = Login.gett()
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')
            cur = con.cursor()


            username= self.us_name
            dropoff_address= self.drop_ent.get()
            month= self.clickedmonthd3.get()
            day=self.clickedd1.get()
            date=self.clickeddated2 .get()

            sql = "insert into dropoff(username,dropoff_address,month,day,date)" "values ('" + username + "','" +dropoff_address+ "','" +month+ "','" +day+ "','" +date+"')"
            values = cur.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo("success", "Your cab has been  booked", parent=self.root3)
            self.clearpickup()

        except:
            print("error")


    def review(self):
        self.us_name = Login.gett()
        try:

            username = self.us_name
            review1 = self.review_entry1.get("1.0","end-1c")

            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            print("a")
            cur.execute("insert into review(username,review)" "values ('" + username + "','" + review1 + "')")
            con.commit()
            con.close()
            messagebox.showinfo("success", "Your review has been submitted", parent=self.root3)
            self.review_entry1.delete("1.0","end-1c")

        except:
            print("error")

