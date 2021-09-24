from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector
from PIL import Image, ImageTk

class admin:
    def __init__(self, master):
        self.root5 = master
        self.root5.title("Room")
        self.root5.state('zoomed')
        self.my_canvas = Canvas(self.root5)
        self.my_canvas.pack(fill="both", expand=True)
        self.background = ImageTk.PhotoImage(Image.open('background.png'), master=self.root5)
        self.my_canvas.create_image(0, 0, image=self.background, anchor="nw")

        self.ace_images()
        self.buttons()
        self.main_frame()

        self.root5.mainloop()
    #
    def ace_images(self):
        # now set an image for moving
        self.img1 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace.png"), master=self.root5)
        # in you current folder that you are working with
        self.img2 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace1.png"), master=self.root5)
        self.img3 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace2.png"), master=self.root5)
        self.img4 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace3.png"), master=self.root5)
        # Create a label
        self.l = Label(self.root5, font="bold")
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
        self.root5.after(1500, self.ace_move)

    def buttons(self):

        self.btn_img = ImageTk.PhotoImage(Image.open('button.png'), master=self.root5)

        self.users_btn = Button(self.root5, text="Users Profile", image=self.btn_img,
                                font=("Rockwell nova", 20, 'bold'),
                                cursor="hand2", borderwidth=0,
                                border='0', overrelief="sunken", fg="white", compound=CENTER,
                                command=self.main_frame)
        self.users_btn.place(x=30, y=150)

        self.room_btn = Button(self.root5, text="Room Details", fg="white", image=self.btn_img,
                               font=("Rockwell nova", 20, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER, command=self.rooms)
        self.room_btn.place(x=30, y=250)

        self.orders_btn = Button(self.root5, text="Order Details", fg="white", image=self.btn_img,
                                 font=("Rockwell nova", 20, 'bold'),
                                 cursor="hand2", borderwidth=0,
                                 border='0', overrelief="sunken", compound=CENTER,command=self.orderdetails)
        self.orders_btn.place(x=30, y=350)

        self.cab_btn = Button(self.root5, text="Cab Details", fg="white", image=self.btn_img,
                              font=("Rockwell nova", 20, 'bold'),
                              cursor="hand2", borderwidth=0,
                              border='0', overrelief="sunken", compound=CENTER,command=self.cabdetails)
        self.cab_btn.place(x=30, y=450)



    def userdata(self):

        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Janakidevi24#',
                port=3306,
                database='login_registration')
            cur = con.cursor()
            cur.execute("select username,fname,lname,contact_number,gender from registration")
            result = cur.fetchall()
            if len(result) !=0:
                for row in result :
                    self.displayuserdata.insert('',END,values=row)

                con.close()

        except:
            print('error')
            pass
    def main_frame(self):
        self.users_btn.config(fg='green')
        self.room_btn.config(fg='white')
        self.orders_btn.config(fg='white')
        self.cab_btn.config(fg='white')

        self.frame_main = LabelFrame(self.root5, height=660, width=1080, borderwidth=10)
        self.frame_main.place(x=300, y=130)
        self.frame_main.pack_propagate(False)

        scrollu=Scrollbar(self.frame_main,orient=VERTICAL)
        self.displayuserdata=ttk.Treeview(self.frame_main,height=500,column=("username","fname","lname","contact_number","gender"),xscrollcommand=scrollu.set)
        scrollu.pack(side=RIGHT,fill=Y)
        scrollu.config(command=self.displayuserdata.yview)

        self.displayuserdata.heading("username",text="User name")
        self.displayuserdata.heading("fname",text="First name")
        self.displayuserdata.heading("lname", text="Last name")
        self.displayuserdata.heading("contact_number", text="Contact number")
        self.displayuserdata.heading("gender", text="Gender")
        self.displayuserdata['show']='headings'

        self.displayuserdata.column("username",width=100)
        self.displayuserdata.column("fname",width=100)
        self.displayuserdata.column("lname", width=100)
        self.displayuserdata.column("contact_number", width=200)
        self.displayuserdata.column("gender", width=100)


        self.displayuserdata.pack(fill=BOTH,expand=1)

        self.userdata()



    def fetchroom(self):

        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Janakidevi24#',
                port=3306,
                database='login_registration')
            cur = con.cursor()
            cur.execute("select room_no from room_book")
            row = cur.fetchall()
            for i in range(19):
                try:
                    if row[i] == ('Room:1',):
                        self.room1.config(bg="red")
                    if row[i] == ('Room:2',):
                        self.room2.config(bg="red")
                    if row[i] == ('Room:3',):
                        self.room3.config(bg="red")
                    if row[i] == ('Room:4',):
                        self.room4.config(bg="red")
                    if row[i] == ('Room:5',):
                        self.room5.config(bg="red")
                    if row[i] == ('Room:6',):
                        self.room6.config(bg="red")
                    if row[i] == ('Room:7',):
                        self.room7.config(bg="red")
                    if row[i] == ('Room:8',):
                        self.room8.config(bg="red")
                    if row[i] == ('Room:9',):
                        self.room9.config(bg="red")
                    if row[i] == ('Room:10',):
                        self.room10.config(bg="red")
                    if row[i] == ('Villa:11',):
                        self.villa101.config(bg="red")
                    if row[i] == ('Villa:12',):
                        self.villa102.config(bg="red")
                    if row[i] == ('Villa:13',):
                        self.villa103.config(bg="red")
                    if row[i] == ('Villa:14',):
                        self.villa104.config(bg="red")
                    if row[i] == ('Villa:15',):
                        self.villa105.config(bg="red")
                    if row[i] == ('Hall:16',):
                        self.hall1.config(bg="red")
                    if row[i] == ('Hall:17',):
                        self.hall2.config(bg="red")
                    if row[i] == ('Hall:18',):
                        self.hall3.config(bg="red")
                except:
                    pass

            con.close()

        except:
            print('error')
            pass


    def data(self):

        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='@!2002bisesh',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from room_book")
            result = cur.fetchall()
            if len(result) !=0:
                for row in result :
                    self.display.insert('',END,values=row)

                con.close()

        except:
            print('error')
            pass



    def rooms(self):
        self.users_btn.config(fg='white')
        self.room_btn.config(fg='green')
        self.orders_btn.config(fg='white')
        self.cab_btn.config(fg='white')

        self.frame_button = LabelFrame(self.root5, height=660, width=1080, borderwidth=10)
        self.frame_button.place(x=300, y=130)
        self.frame_button.pack_propagate(False)

        self.room_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root5)

        self.roominfobtn = Button(self.frame_button, text='Info', fg="white", image=self.room_img,
                                  font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER, command=self.moreinfo)
        self.roominfobtn.place(x=500, y=0)


        self.roomviewbtn = Button(self.frame_button, text='View rooms', fg="white", image=self.room_img,
                                  font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER, command=self.roomview)
        self.roomviewbtn.place(x=100, y=0)


        self.txt = ttk.Combobox(self.frame_button, font=("times new roman", 12), state='readonly', justify=CENTER)
        self.txt['values'] = ('Select', 'Room:1', 'Room:2', 'Room:3', 'Room:4', 'Room:5', 'Room:6'
                              , 'Room:7', 'Room:8', 'Room:9'
                              , 'Room:10', 'Villa:11', 'Villa:12', 'Villa:13', 'Villa:14', 'Villa:15'
                              , 'Hall:16', 'Hall:17', 'Hall:18')
        self.txt.place(x=600, y=5, width=250)
        self.txt.current(0)
        self.book_checkout = Button(self.frame_button, text="Check out", fg="white", image=self.room_img,
                                    font=("Rockwell nova", 10, 'bold'),
                                    cursor="hand2", borderwidth=0,
                                    border='0', overrelief="sunken", compound=CENTER, command=self.room_checkout)
        self.book_checkout.place(x=900, y=0)

        self.roomviewbtn.config(fg='green')
        self.roomview()
    def roomview(self):
        self.roomviewbtn.config(fg='green')
        self.roominfobtn.config(fg='white')
        self.users_btn.config(fg='white')
        self.room_btn.config(fg='green')
        self.orders_btn.config(fg='white')
        self.cab_btn.config(fg='white')



        self.frame_standardroom = LabelFrame(self.frame_button, height=550, width=1040, borderwidth=10)
        self.frame_standardroom.place(x=10, y=60)
        self.frame_standardroom.pack_propagate(False)
        self.my_canvas_room_in = Canvas(self.frame_standardroom)
        self.my_canvas_room_in.pack(fill="both", expand=True)

        self.room_bg_img = ImageTk.PhotoImage(Image.open("roombg.png"), master=self.root5)
        self.my_canvas_room_in.create_image(0, 0, image=self.room_bg_img, anchor="nw")

        self.room1 = Button(self.frame_standardroom, text='ROOM 1', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room1.place(x=10, y=30)
        self.room2 = Button(self.frame_standardroom, text='ROOM 2', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'),
                            cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room2.place(x=260, y=30)
        self.room3 = Button(self.frame_standardroom, text='ROOM 3', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'),
                            cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room3.place(x=510, y=30)
        self.room4 = Button(self.frame_standardroom, text='ROOM 4', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'),
                            cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room4.place(x=760, y=30)
        self.room5 = Button(self.frame_standardroom, text='ROOM 5', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'),
                            cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room5.place(x=10, y=130)
        self.room6 = Button(self.frame_standardroom, text='ROOM 6', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room6.place(x=260, y=130)
        self.room7 = Button(self.frame_standardroom, text='ROOM 7', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'),
                            cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room7.place(x=510, y=130)
        self.room8 = Button(self.frame_standardroom, text='ROOM 8', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'),
                            cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room8.place(x=760, y=130)
        self.room9 = Button(self.frame_standardroom, text='ROOM 9', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'),
                            cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.room9.place(x=10, y=230)
        self.room10 = Button(self.frame_standardroom, text='ROOM 10', fg="white", image=self.room_img,
                             font=("Rockwell nova", 10, 'bold'),
                             cursor="hand2", borderwidth=0,
                             border='0', overrelief="sunken", compound=CENTER)
        self.room10.place(x=260, y=230)
        self.villa101 = Button(self.frame_standardroom, text='VILLA 11', fg="white", image=self.room_img,
                               font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER)
        self.villa101.place(x=510, y=230)
        self.villa102 = Button(self.frame_standardroom, text='VILLA 12', fg="white", image=self.room_img,
                               font=("Rockwell nova", 10, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER)
        self.villa102.place(x=760, y=230)
        self.villa103 = Button(self.frame_standardroom, text='VILLA 13', fg="white", image=self.room_img,
                               font=("Rockwell nova", 10, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER)
        self.villa103.place(x=10, y=330)
        self.villa104 = Button(self.frame_standardroom, text='VILLA 14', fg="white", image=self.room_img,
                               font=("Rockwell nova", 10, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER)
        self.villa104.place(x=260, y=330)
        self.villa105 = Button(self.frame_standardroom, text='VILLA 15', fg="white", image=self.room_img,
                               font=("Rockwell nova", 10, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER)
        self.villa105.place(x=510, y=330)

        self.hall1 = Button(self.frame_standardroom, text='HALL 16', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.hall1.place(x=760, y=330)
        self.hall2 = Button(self.frame_standardroom, text='HALL 17', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.hall2.place(x=150, y=430)
        self.hall3 = Button(self.frame_standardroom, text='HALL 18', fg="white", image=self.room_img,
                            font=("Rockwell nova", 10, 'bold'),
                            cursor="hand2", borderwidth=0,
                            border='0', overrelief="sunken", compound=CENTER)
        self.hall3.place(x=550, y=430)

        self.fetchroom()


    def moreinfo(self):
        self.roominfobtn.config(fg='green')
        self.roomviewbtn.config(fg='white')
        self.users_btn.config(fg='white')
        self.room_btn.config(fg='green')
        self.orders_btn.config(fg='white')
        self.cab_btn.config(fg='white')
        self.frame_standardroom.destroy()

        self.frame_info = LabelFrame(self.frame_button, height=500, width=800, borderwidth=10)
        self.frame_info.place(x=100, y=100)
        self.frame_info.propagate(False)

        scroll=Scrollbar(self.frame_info,orient=VERTICAL)
        self.display=ttk.Treeview(self.frame_info,height=500,column=("username","room_no"),xscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.display.yview)
        self.display.heading("username",text="User name")
        self.display.heading("room_no",text="Room number")
        self.display['show']='headings'

        self.display.column("username",width=400)
        self.display.column("room_no",width=400)

        self.display.pack(fill=BOTH,expand=1)

        self.data()


    def pickupdata(self):
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='@!2002bisesh',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from pickup")
            result = cur.fetchall()
            if len(result) !=0:
                for row in result :
                    self.displaypickup.insert('',END,values=row)

                con.close()

        except:
            print('error')
            pass

    def dropoffdata(self):
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='@!2002bisesh',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from dropoff")
            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    self.displaydropoff.insert('', END, values=row)

                con.close()

        except:
            print('error')
            pass

    def cabdetails(self):
        self.users_btn.config(fg='white')
        self.room_btn.config(fg='white')
        self.orders_btn.config(fg='white')
        self.cab_btn.config(fg='green')

        self.framec_button = LabelFrame(self.root5, height=660, width=1080, borderwidth=10)
        self.framec_button.place(x=300, y=130)
        self.framec_button.pack_propagate(False)


        self.btnbg_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root5)

        self.pickupbtn = Button(self.framec_button, text='Pick Up', fg="white", image=self.btnbg_img,
                                  font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER, command=self.showpickup)
        self.pickupbtn.place(x=100, y=10)

        self.dropoffbtn = Button(self.framec_button, text='Drop Off', fg="white", image=self.btnbg_img,
                                  font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER,command=self.showdropoff)
        self.dropoffbtn.place(x=500, y=10)

        self.pickupbtn.config(fg='green')
        self.showpickup()

    def showpickup(self):
        self.pickupbtn.config(fg="green")
        self.dropoffbtn.config(fg="white")



        self.frame_pickup = LabelFrame(self.framec_button, height=400, width=800, borderwidth=10)
        self.frame_pickup.place(x=100, y=100)
        self.frame_pickup.propagate(False)

        scrollp = Scrollbar(self.frame_pickup, orient=VERTICAL)
        self.displaypickup = ttk.Treeview(self.frame_pickup, height=400, column=("username", "pickup_address","month","day","date"),
                                    xscrollcommand=scrollp.set)
        scrollp.pack(side=RIGHT, fill=Y)
        scrollp.config(command=self.displaypickup.yview)

        self.displaypickup.heading("username", text="User name")
        self.displaypickup.heading("pickup_address", text="Pickup Address")
        self.displaypickup.heading("month", text="Month")
        self.displaypickup.heading("day", text="Day")
        self.displaypickup.heading("date", text="Date")


        self.displaypickup['show'] = 'headings'

        self.displaypickup.column("username", width=100)
        self.displaypickup.column("pickup_address", width=400)
        self.displaypickup.column("month", width=100)
        self.displaypickup.column("day", width=100)
        self.displaypickup.column("date", width=100)

        self.displaypickup.pack(fill=BOTH, expand=1)

        self.pickupdata()

        self.frame_dropoff.destroy()



    def showdropoff(self):
        self.pickupbtn.config(fg="white")
        self.dropoffbtn.config(fg="green")


        self.frame_dropoff = LabelFrame(self.framec_button, height=400, width=800, borderwidth=10)
        self.frame_dropoff.place(x=100, y=100)
        self.frame_dropoff.propagate(False)

        scrolld = Scrollbar(self.frame_dropoff, orient=VERTICAL)
        self.displaydropoff = ttk.Treeview(self.frame_dropoff, height=400,
                                          column=("username", "dropoff_address", "month", "day", "date"),
                                          xscrollcommand=scrolld.set)
        scrolld.pack(side=RIGHT, fill=Y)
        scrolld.config(command=self.displaydropoff.yview)

        self.displaydropoff.heading("username", text="User name")
        self.displaydropoff.heading("dropoff_address", text="Dropoff Address")
        self.displaydropoff.heading("month", text="Month")
        self.displaydropoff.heading("day", text="Day")
        self.displaydropoff.heading("date", text="Date")

        self.displaydropoff['show'] = 'headings'

        self.displaydropoff.column("username", width=100)
        self.displaydropoff.column("dropoff_address", width=400)
        self.displaydropoff.column("month", width=100)
        self.displaydropoff.column("day", width=100)
        self.displaydropoff.column("date", width=100)

        self.displaydropoff.pack(fill=BOTH, expand=1)

        self.dropoffdata()
        self.frame_pickup.destroy()

    def customdata(self):
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='@!2002bisesh',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from burgar")
            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    self.displaycustom.insert('', END, values=row)

                con.close()

        except:
            print('error')
            pass

    def menu(self):
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='@!2002bisesh',
                port=3306,
                database='login_registration1')
            cur = con.cursor()
            cur.execute("select * from menu")
            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    self.displaymenu.insert('', END, values=row)

                con.close()

        except:
            print('error')
            pass


    def orderdetails(self):
        self.users_btn.config(fg='white')
        self.room_btn.config(fg='white')
        self.orders_btn.config(fg='green')
        self.cab_btn.config(fg='white')

        self.frameo_button = LabelFrame(self.root5, height=660, width=1080, borderwidth=10)
        self.frameo_button.place(x=300, y=130)
        self.frameo_button.pack_propagate(False)

        self.btnbg_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root5)

        self.custombtn = Button(self.frameo_button, text='Custom Menu', fg="white", image=self.btnbg_img,
                                  font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER, command=self.showcustom)
        self.custombtn.place(x=100, y=10)

        self.menubtn = Button(self.frameo_button, text='Menu', fg="white", image=self.btnbg_img,
                                  font=("Rockwell nova", 10, 'bold'), cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER,command=self.showmenu)
        self.menubtn.place(x=500, y=10)

        self.custombtn.config(fg="green")
        self.showcustom()


    def showmenu(self):
        self.custombtn.config(fg="white")
        self.menubtn.config(fg="green")

        self.frame_menu = LabelFrame(self.frameo_button, height=400, width=1000, borderwidth=10)
        self.frame_menu.place(x=10, y=100)
        self.frame_menu.propagate(False)

        scrollm = Scrollbar(self.frame_menu, orient=HORIZONTAL)
        self.displaymenu = ttk.Treeview(self.frame_menu, height=400, column=("username","chicken_momo","buff_momo","vegg_momo","chicken_pizza","alfungi_pizza","cheese_pizza","ham_burger","chicken_burger","mix_burger","sizzler","newari_khajaset","yomari","choila","Thakali_set","chicken_sekuwa","pork_sekuwa","buff_sekuwa","coke","dew","fanta"),
                                    xscrollcommand=scrollm.set)

        scrollm.pack(side=BOTTOM, fill=X)
        scrollm.config(command=self.displaymenu.xview)

        self.displaymenu.heading("username", text="User name")
        self.displaymenu.heading("chicken_momo", text="Chicken momo")
        self.displaymenu.heading("buff_momo", text="Buff momo")
        self.displaymenu.heading("vegg_momo", text="Veg momo")
        self.displaymenu.heading("chicken_pizza", text="Chicken pizza")
        self.displaymenu.heading("alfungi_pizza", text="Alfungi pizza")
        self.displaymenu.heading("cheese_pizza", text="Cheese pizza")
        self.displaymenu.heading("ham_burger", text="Ham burger")
        self.displaymenu.heading("chicken_burger", text="Chicken Burger")
        self.displaymenu.heading("mix_burger", text="Mix Burger")
        self.displaymenu.heading("sizzler", text="Sizzler")
        self.displaymenu.heading("newari_khajaset", text="Newari set")
        self.displaymenu.heading("yomari", text="Yomari")
        self.displaymenu.heading("choila", text="Choila")
        self.displaymenu.heading("Thakali_set", text="Thakali set")
        self.displaymenu.heading("chicken_sekuwa", text="Chicken sekuwa")
        self.displaymenu.heading("pork_sekuwa", text="Pork sekuwa")
        self.displaymenu.heading("buff_sekuwa", text="Buff Sekuwa")
        self.displaymenu.heading("coke", text="Coke")
        self.displaymenu.heading("dew", text="Dew")
        self.displaymenu.heading("fanta", text="Fanta")



        self.displaymenu['show'] = 'headings'

        self.displaymenu.column("username", width=100)
        self.displaymenu.column("chicken_momo", width=100)
        self.displaymenu.column("buff_momo",width=100)
        self.displaymenu.column("vegg_momo", width=100)
        self.displaymenu.column("chicken_pizza", width=100)
        self.displaymenu.column("alfungi_pizza", width=100)
        self.displaymenu.column("cheese_pizza", width=100)
        self.displaymenu.column("ham_burger", width=100)
        self.displaymenu.column("chicken_burger", width=100)
        self.displaymenu.column("mix_burger", width=100)
        self.displaymenu.column("sizzler",width=50 )
        self.displaymenu.column("newari_khajaset", width=100)
        self.displaymenu.column("yomari",width=50)
        self.displaymenu.column("choila", width=50)
        self.displaymenu.column("Thakali_set", width=100)
        self.displaymenu.column("chicken_sekuwa", width=100)
        self.displaymenu.column("pork_sekuwa", width=100)
        self.displaymenu.column("buff_sekuwa", width=100)
        self.displaymenu.column("coke",width=50)
        self.displaymenu.column("dew", width=50)
        self.displaymenu.column("fanta", width=50)

        self.displaymenu.pack(fill=BOTH, expand=1)


        self.menu()

    def showcustom(self):
        self.custombtn.config(fg="green")
        self.menubtn.config(fg="white")

        self.frame_custom = LabelFrame(self.frameo_button, height=400, width=1000, borderwidth=10)
        self.frame_custom.place(x=10, y=100)
        self.frame_custom.propagate(False)

        scrollc = Scrollbar(self.frame_custom, orient=VERTICAL)
        self.displaycustom = ttk.Treeview(self.frame_custom, height=400, column=("username", "spanich","tomato","pickel","cheese","fish","chicken","qty"),
                                    xscrollcommand=scrollc.set)
        scrollc.pack(side=RIGHT, fill=Y)
        scrollc.config(command=self.displaycustom.yview)

        self.displaycustom.heading("username", text="User name")
        self.displaycustom.heading("spanich", text="Spinach")
        self.displaycustom.heading("tomato", text="Tomato")
        self.displaycustom.heading("pickel", text="Pickel")
        self.displaycustom.heading("cheese", text="Cheese")
        self.displaycustom.heading("fish", text="Fish")
        self.displaycustom.heading("chicken", text="Chicken")
        self.displaycustom.heading("qty", text="Quantity")


        self.displaycustom['show'] = 'headings'



        self.displaycustom.column("username", width=100)
        self.displaycustom.column("spanich", width=100)
        self.displaycustom.column("tomato", width=100)
        self.displaycustom.column("pickel", width=100)
        self.displaycustom.column("cheese", width=100)
        self.displaycustom.column("fish", width=100)
        self.displaycustom.column("chicken", width=100)
        self.displaycustom.column("qty", width=100)

        self.displaycustom.pack(fill=BOTH, expand=1)

        self.customdata()

    def room_checkout(self):
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Janakidevi24#',
                port=3306,
                database='login_registration')
            cur = con.cursor()
            cur.execute("select * from room_book where room_no=%s", (self.txt.get(),))
            row = cur.fetchone()
            if row != None:
                cur.execute("delete from room_book where room_no=%s", (self.txt.get(),))
                messagebox.showinfo("success", "The room has been sucessfully checked out", parent=self.root5)

                con.commit()
                con.close()
            else:
                messagebox.showerror('sorry', 'The room no you have choosen has not been booked yet')



        finally:
            pass
        self.moreinfo()