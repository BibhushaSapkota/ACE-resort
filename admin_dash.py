from tkinter import *

import mysql.connector
from PIL import Image,ImageTk


class admin:
    def __init__(self,master):
        self.root5 = master
        self.root5.title("Room")
        self.root5.state('zoomed')
        self.my_canvas = Canvas(self.root5)
        self.my_canvas.pack(fill="both", expand=True)
        self.background = ImageTk.PhotoImage(Image.open('background.png'),master=self.root5)
        self.my_canvas.create_image(0, 0, image=self.background, anchor="nw")

        self.ace_images()
        self.buttons()
        self.main_frame()

        self.root5.mainloop()


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
                                     border='0', overrelief="sunken", compound=CENTER ,command=self.rooms)
        self.room_btn.place(x=30, y=250)

        self.orders_btn = Button(self.root5, text="Order Details", fg="white", image=self.btn_img,
                                font=("Rockwell nova", 20, 'bold'),
                                cursor="hand2", borderwidth=0,
                                border='0', overrelief="sunken", compound=CENTER)
        self.orders_btn.place(x=30, y=350)

        self.cab_btn = Button(self.root5, text="Cab Details", fg="white", image=self.btn_img,
                               font=("Rockwell nova", 20, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER)
        self.cab_btn.place(x=30, y=450)




    def main_frame(self):
        self.users_btn.config(fg='green')
        self.room_btn.config(fg='white')
        self.orders_btn.config(fg='white')
        self.cab_btn.config(fg='white')

        self.frame_main = LabelFrame(self.root5, height=690, width=1080, borderwidth=10)
        self.frame_main.place(x=300, y=130)
        self.frame_main.pack_propagate(False)





    def fetchroom(self):

        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='@!2002bisesh',
                port=3306,
                database='login_registration1')
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
    def rooms(self):
        self.users_btn.config(fg='white')
        self.room_btn.config(fg='green')
        self.orders_btn.config(fg='white')
        self.cab_btn.config(fg='white')



        self.frame_standardroom = LabelFrame(self.frame_main, height=670, width=1060, borderwidth=10)
        self.frame_standardroom.place(x=0, y=0)
        self.frame_standardroom.pack_propagate(False)
        self.my_canvas_room_in = Canvas(self.frame_standardroom)
        self.my_canvas_room_in.pack(fill="both", expand=True)
        self.room_bg_img = ImageTk.PhotoImage(Image.open("roombg.png"), master=self.root5)
        self.my_canvas_room_in.create_image(0, 0, image=self.room_bg_img, anchor="nw")

        self.room_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root5)
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

        self.hall1=Button(self.frame_standardroom,text='HALL 16', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER)
        self.hall1.place(x=760,y=330)
        self.hall2=Button(self.frame_standardroom,text='HALL 17', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER)
        self.hall2.place(x=150,y=430)
        self.hall3=Button(self.frame_standardroom,text='HALL 18',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER)
        self.hall3.place(x=550,y=430)

        self.fetchroom()