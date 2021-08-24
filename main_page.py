from tkinter import *
from PIL import ImageTk, Image
from time import sleep
import  custom_burger
import room
class MainPage:
    def __init__(self,master):
        self.root3 = master
        self.root3.title("Main")
        self.root3.state('zoomed')
        self.my_canvas = Canvas(self.root3)
        self.my_canvas.pack(fill="both", expand=True)
        self.background = ImageTk.PhotoImage(Image.open('background.png'),master=self.root3)
        self.my_canvas.create_image(0, 0, image=self.background, anchor="nw")
        self.ace_images()
        self.buttons()
        self.menu_main_frame()
        self.root3.update()
        self.root3.mainloop()
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
        self.details_img= ImageTk.PhotoImage(Image.open('details.png'),master=self.root3)
        self.details_change_img = ImageTk.PhotoImage(Image.open('details_change.png'),master=self.root3)
        self.about_img = ImageTk.PhotoImage(Image.open('information.png'),master=self.root3)
        self.about_change_img = ImageTk.PhotoImage(Image.open('information_change.png'),master=self.root3)
        self.profile_img = ImageTk.PhotoImage(Image.open('profile.png'),master=self.root3)
        self.profile_change_img = ImageTk.PhotoImage(Image.open('profile_change.png'),master=self.root3)
        self.setting_img = ImageTk.PhotoImage(Image.open('setting.png'),master=self.root3)
        self.setting_change_img = ImageTk.PhotoImage(Image.open('setting_change.png'),master=self.root3)


        self.menu_btn= Button(self.root3, text="      MENU", fg="white",image=self.menu_change_img,
                                   font=("Rockwell nova", 20,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.menu_main_frame)
        self.menu_btn.place(x=30,y=150)
        self.details_btn = Button(self.root3, text="   DETAILS", fg="white", image=self.details_img,
                               font=("Rockwell nova", 20, 'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER, command=self.fn_details)
        self.details_btn.place(x=30, y=250)


        self.about_btn = Button(self.root3, text="ABOUT US", fg="white", image=self.about_img,
                               font=("Rockwell nova", 20,'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER,command=lambda:self.fn_about())
        self.about_btn.place(x=30, y=350)

        self.profile_btn = Button(self.root3, text="PROFILE", fg="white", image=self.profile_img,
                                  font=("Rockwell nova", 20,'bold'),
                                  cursor="hand2", borderwidth=0,
                                  border='0', overrelief="sunken", compound=CENTER,command=lambda:self.fn_profile())
        self.profile_btn.place(x=30, y=450)

        self.setting_btn = Button(self.root3, text="   SETTING", fg="white", image=self.setting_img,
                               font=("Rockwell nova", 20,'bold'),
                               cursor="hand2", borderwidth=0,
                               border='0', overrelief="sunken", compound=CENTER,command=lambda:self.fn_setting())
        self.setting_btn.place(x=30, y=550)


    def menu_main_frame(self):
        self.menu_btn.config(image=self.menu_change_img, fg='green')
        self.details_btn.config(image=self.details_img, fg='white')
        self.about_btn.config(image=self.about_img, fg='white')
        self.profile_btn.config(image=self.profile_img, fg='white')
        self.setting_btn.config(image=self.setting_img, fg='white')

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
                              font=("Rockwell nova", 25, 'bold'), command=self.burgar)
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
    def burgar(self):
        custom_burger.CustomBurger()


    def fn_details(self):
        self.frame_details = LabelFrame(self.root3, height=550, width=1050, borderwidth=10)
        self.frame_details.place(x=300, y=130)
        self.topic=Label(self.frame_details,text='DETAILS',font=("Rockwell nova", 30,'bold'))
        self.topic.place(x=420,y=30)
        self.frame_main.pack_propagate(False)
        self.name_fn='details'
        self.frame_main.place_forget()

        self.img_change()
    def fn_about(self):
        self.frame_about = LabelFrame(self.root3, height=550, width=1050, borderwidth=10)
        self.frame_about.place(x=300, y=130)
        self.topic = Label(self.frame_about, text='ABOUT US', font=("Rockwell nova", 30, 'bold'))
        self.topic.place(x=420, y=30)
        self.name_fn='about'

        self.img_change()
    def fn_profile(self):
        self.frame_profile = LabelFrame(self.root3, height=550, width=1050, borderwidth=10)
        self.frame_profile.place(x=300, y=130)
        self.topic = Label(self.frame_profile, text='YOUR PROFILE', font=("Rockwell nova", 30, 'bold'))
        self.topic.place(x=420, y=30)
        self.name_fn='profile'
        self.img_change()
    def fn_setting(self):
        self.frame_setting = LabelFrame(self.root3, height=550, width=1050, borderwidth=10)
        self.frame_setting.place(x=300, y=130)
        self.topic = Label(self.frame_setting, text='SETTING', font=("Rockwell nova", 30, 'bold'))
        self.topic.place(x=420, y=30)
        self.name_fn = 'setting'
        self.img_change()

    def img_change(self):
        if self.name_fn=='menu':
            self.menu_btn.config(image=self.menu_change_img, fg='green')
            self.details_btn.config(image=self.details_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_img, fg='white')


        elif self.name_fn=='details':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_change_img,fg='green')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_img, fg='white')


        elif self.name_fn=='about':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_img,fg='white')
            self.about_btn.config(image=self.about_change_img, fg='green')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_img, fg='white')

            self.frame_main.place_forget()
        elif self.name_fn=='profile':
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_img,fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_change_img, fg='green')
            self.setting_btn.config(image=self.setting_img, fg='white')

            self.frame_main.place_forget()
        else:
            self.menu_btn.config(image=self.menu_img, fg='white')
            self.details_btn.config(image=self.details_img, fg='white')
            self.about_btn.config(image=self.about_img, fg='white')
            self.profile_btn.config(image=self.profile_img, fg='white')
            self.setting_btn.config(image=self.setting_change_img, fg='green')

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
        self.cab_bg_img=ImageTk.PhotoImage(Image.open(f'cab_bg.png'),master=self.root3)
        self.my_canvas_cab_in.create_image(0, 0, image=self.cab_bg_img, anchor="nw")
        self.my_canvas_cab_in.create_text(450,80,text="BOOK A TAXI", font=("Algerian", 45),fill="white")
        self.my_canvas_cab_in.create_text(230, 150, text="Pick up address:", font=("Times new roman", 20), fill="white")
        self.my_canvas_cab_in.create_text(230, 250, text="Drop off  address:", font=("Times new roman", 20), fill="white")
        self.my_canvas_cab_in.create_text(250, 200, text="Pick up Date:", font=("Times new roman", 20), fill="white")
        self.my_canvas_cab_in.create_text(250, 300, text="Drop off Date:",font=("Times new roman", 20), fill="white")

        self.pick_ent=Entry(self.frame_cab_in,bg="#05035b",fg="white",font=("Times new roman", 20),width=15)
        self.pick_ent.place(x=350,y=130)
        self.pick_dat = Entry(self.frame_cab_in,bg="#05035b",fg="white", font=("Times new roman", 20), width=15)
        self.pick_dat.place(x=350, y=180)
        self.pick_btn = Button(self.frame_cab_in,text="Book",bg="green",fg="white", font=("Times new roman", 18,'bold'))
        self.pick_btn.place(x=580, y=160)


        self.drop_ent = Entry(self.frame_cab_in,bg="#05035b",fg="white", font=("Times new roman", 20), width=15)
        self.drop_ent.place(x=350, y=230)
        self.drop_dat = Entry(self.frame_cab_in,bg="#05035b",fg="white", font=("Times new roman", 20), width=15)
        self.drop_dat.place(x=350, y=280)
        self.drop_btn = Button(self.frame_cab_in, text="Book", bg="green", fg="white", font=("Times new roman", 18,'bold'))
        self.drop_btn.place(x=580, y=255)