from tkinter import *
from PIL import ImageTk, Image

class Roompage:
    def __init__(self ,master):
        self.root4 = master
        self.root4.title("Room")
        self.root4.state('zoomed')
        self.my_canvas = Canvas(self.root4)
        self.my_canvas.pack(fill="both", expand=True)

        self.background = ImageTk.PhotoImage(Image.open('background.png'),master=self.root4)
        self.my_canvas.create_image(0, 0, image=self.background, anchor="nw")
        self.ace_images()
        self.buttons()
        self.main_frame()

    def ace_images(self):
        # now set an image for moving
        self.img1 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace.png"), master=self.root4)
        # in you current folder that you are working with
        self.img2 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace1.png"), master=self.root4)
        self.img3 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace2.png"), master=self.root4)
        self.img4 = ImageTk.PhotoImage(Image.open(f"ace_logo/ace3.png"), master=self.root4)
        # Create a label
        self.l = Label(self.root4, font="bold")
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
        self.root4.after(1500, self.ace_move)

    def buttons(self):

        self.standardroom_img = ImageTk.PhotoImage(Image.open('button.png'), master=self.root4)
        self.roooom_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root4)


        self.standardroom_btn= Button(self.root4, text="Standard room", image=self.standardroom_img,
                                   font=("Rockwell nova", 20,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",fg="white",compound=CENTER,command=self.main_frame)
        self.standardroom_btn.place(x=30,y=150)

        self.deluxeroom_img = ImageTk.PhotoImage(Image.open('button.png'),master=self.root4)


        self.deluxeroom_btn= Button(self.root4, text="Deluxe room", fg="white",image=self.standardroom_img,
                                   font=("Rockwell nova", 20,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.fn_deluxeroom)
        self.deluxeroom_btn.place(x=30,y=250)


        self.villa_btn= Button(self.root4, text="Villa", fg="white",image=self.standardroom_img,
                                   font=("Rockwell nova", 20,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.fn_villa)
        self.villa_btn.place(x=30,y=350)

        self.hall_btn= Button(self.root4, text="SEMINAR HALL", fg="white",image=self.standardroom_img,
                                   font=("Rockwell nova", 20,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.fn_hall)
        self.hall_btn.place(x=30,y=450)

        self.lbl=Label(self.root4,text="choose room/villa/hall:",fg='#9a90e4',font=("Rockwell nova", 15,'bold'))
        self.lbl.place(x=30,y=550)
        self.txt=Entry(self.root4,bg='#9a90e4',font=("Rockwell nova", 15,'bold'))
        self.txt.place(x=30,y=600)
        self.book_btn= Button(self.root4, text="BOOK", fg="white",image=self.roooom_img,
                                   font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER)
        self.book_btn.place(x=50,y=650)

    def main_frame(self):
        self.standardroom_btn.config(fg='green')
        self.deluxeroom_btn.config(fg='white')
        self.villa_btn.config(fg='white')
        self.hall_btn.config(fg='white')

        self.frame_main = LabelFrame(self.root4, height=650, width=1040, borderwidth=10)
        self.frame_main.place(x=300, y=130)
        self.frame_main.pack_propagate(False)
        self.fn_standardroom()

    def fn_standardroom(self):
        self.room_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root4)
        self.frame_standardroom = LabelFrame(self.root4, height=650, width=1050, borderwidth=10)
        self.frame_standardroom.place(x=300, y=130)

        self.sroominfo=Button(self.frame_standardroom,text='STANDARD ROOM INFO', fg="white",image=self.room_img,font=("Rockwell nova", 7,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.sroom)
        self.sroominfo.place(x=0,y=30)
        self.room1=Button(self.frame_standardroom,text='ROOM 1', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm)
        self.room1.place(x=160,y=30)
        self.room2=Button(self.frame_standardroom,text='ROOM 2',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm1)
        self.room2.place(x=330,y=30)
        self.room3=Button(self.frame_standardroom,text='ROOM 3',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm2)
        self.room3.place(x=490,y=30)
        self.room4=Button(self.frame_standardroom,text='ROOM 4',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm3)
        self.room4.place(x=650,y=30)
        self.room5=Button(self.frame_standardroom,text='ROOM 5',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm4)
        self.room5.place(x=810,y=30)

        self.name_fn='Standard rooms'

    def fn_deluxeroom(self):
        self.standardroom_btn.config(fg='white')
        self.deluxeroom_btn.config(fg='green')
        self.villa_btn.config(fg='white')
        self.hall_btn.config(fg='white')
        self.room_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root4)
        self.frame_deluxeroom = LabelFrame(self.root4, height=650, width=1050, borderwidth=10)
        self.frame_deluxeroom.place(x=300, y=130)
        self.droominfo=Button(self.frame_deluxeroom,text='DELUXE ROOM INFO', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.droom)
        self.droominfo.place(x=0,y=30)
        self.room6=Button(self.frame_deluxeroom,text='ROOM 6', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm9)
        self.room6.place(x=160,y=30)
        self.room7=Button(self.frame_deluxeroom,text='ROOM 7',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm5)
        self.room7.place(x=330,y=30)
        self.room8=Button(self.frame_deluxeroom,text='ROOM 8',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm6)
        self.room8.place(x=490,y=30)
        self.room9=Button(self.frame_deluxeroom,text='ROOM 9',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm7)
        self.room9.place(x=650,y=30)
        self.room10=Button(self.frame_deluxeroom,text='ROOM 10',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.roomm8)
        self.room10.place(x=810,y=30)
        self.frame_main.pack_propagate(False)
        self.name_fn='deluxe room'
    def fn_villa(self):
        self.standardroom_btn.config(fg='white')
        self.deluxeroom_btn.config(fg='white')
        self.villa_btn.config(fg='green')
        self.hall_btn.config(fg='white')
        self.room_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root4)
        self.frame_villa = LabelFrame(self.root4, height=650, width=1050, borderwidth=10)
        self.frame_villa.place(x=300, y=130)

        self.villainfo=Button(self.frame_villa,text='VILLA INFO', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.villa_info)
        self.villainfo.place(x=0,y=30)
        self.villa101=Button(self.frame_villa,text='VILLA 11', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.villa1)
        self.villa101.place(x=160,y=30)
        self.villa102=Button(self.frame_villa,text='VILLA 12',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.villa2)
        self.villa102.place(x=330,y=30)
        self.villa103=Button(self.frame_villa,text='VILLA 13',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.villa3)
        self.villa103.place(x=490,y=30)
        self.villa104=Button(self.frame_villa,text='VILLA 14',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.villa4)
        self.villa104.place(x=650,y=30)
        self.villa105=Button(self.frame_villa,text='VILLA 15',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.villa5)
        self.villa105.place(x=810,y=30)
        self.frame_main.pack_propagate(False)
        self.name_fn='villa'
    def fn_hall(self):
        self.standardroom_btn.config(fg='white')
        self.deluxeroom_btn.config(fg='white')
        self.villa_btn.config(fg='white')
        self.hall_btn.config(fg='green')
        self.room_img = ImageTk.PhotoImage(Image.open('rb.png'), master=self.root4)
        self.frame_hall = LabelFrame(self.root4, height=650, width=1050, borderwidth=10)
        self.frame_hall.place(x=300, y=130)

        self.hall1=Button(self.frame_hall,text='HALL 16', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.hall16)
        self.hall1.place(x=50,y=30)
        self.hall2=Button(self.frame_hall,text='HALL 17', fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.hall17)
        self.hall2.place(x=300,y=30)
        self.hall3=Button(self.frame_hall,text='HALL 18',fg="white",image=self.room_img,font=("Rockwell nova", 10,'bold'),
                                   cursor="hand2",borderwidth=0,
                                   border='0', overrelief="sunken",compound=CENTER,command=self.hall18)
        self.hall3.place(x=550,y=30)
        self.frame_main.pack_propagate(False)
        self.name_fn='seminar hall'

    def sroom(self):
        self.frame_main.place_forget()
        self.sroominfo.config(image=self.room_img, fg='green')
        self.room1.config(image=self.room_img, fg='white')
        self.room2.config(image=self.room_img, fg='white')
        self.room3.config(image=self.room_img, fg='white')
        self.room4.config(image=self.room_img, fg='white')
        self.room5.config(image=self.room_img, fg='white')
        self.sroom_infoframe()

    def roomm(self):
        self.frame_main.place_forget()
        self.sroominfo.config(image=self.room_img, fg='white')
        self.room1.config(image=self.room_img, fg='green')
        self.room2.config(image=self.room_img, fg='white')
        self.room3.config(image=self.room_img, fg='white')
        self.room4.config(image=self.room_img, fg='white')
        self.room5.config(image=self.room_img, fg='white')
        self.room_frame()

    def roomm1(self):
        self.frame_main.place_forget()
        self.sroominfo.config(image=self.room_img, fg='white')
        self.room2.config(image=self.room_img, fg='green')
        self.room1.config(image=self.room_img, fg='white')
        self.room3.config(image=self.room_img, fg='white')
        self.room4.config(image=self.room_img, fg='white')
        self.room5.config(image=self.room_img, fg='white')
        self.room_frame()

    def roomm2(self):
        self.frame_main.place_forget()
        self.sroominfo.config(image=self.room_img, fg='white')
        self.room3.config(image=self.room_img, fg='green')
        self.room2.config(image=self.room_img, fg='white')
        self.room1.config(image=self.room_img, fg='white')
        self.room4.config(image=self.room_img, fg='white')
        self.room5.config(image=self.room_img, fg='white')
        self.room_frame()
    def roomm3(self):
        self.frame_main.place_forget()
        self.sroominfo.config(image=self.room_img, fg='white')
        self.room4.config(image=self.room_img, fg='green')
        self.room2.config(image=self.room_img, fg='white')
        self.room3.config(image=self.room_img, fg='white')
        self.room1.config(image=self.room_img, fg='white')
        self.room5.config(image=self.room_img, fg='white')
        self.room_frame()

    def roomm4(self):
        self.frame_main.place_forget()
        self.sroominfo.config(image=self.room_img, fg='white')
        self.room5.config(image=self.room_img, fg='green')
        self.room2.config(image=self.room_img, fg='white')
        self.room3.config(image=self.room_img, fg='white')
        self.room4.config(image=self.room_img, fg='white')
        self.room1.config(image=self.room_img, fg='white')
        self.room_frame()

    def droom(self):
        self.frame_main.place_forget()
        self.droominfo.config(image=self.room_img, fg='green')
        self.room7.config(image=self.room_img, fg='white')
        self.room6.config(image=self.room_img, fg='white')
        self.room8.config(image=self.room_img, fg='white')
        self.room9.config(image=self.room_img, fg='white')
        self.room10.config(image=self.room_img, fg='white')
        self.droom_infoframe()

    def roomm5(self):
        self.frame_main.place_forget()
        self.droominfo.config(image=self.room_img, fg='white')
        self.room7.config(image=self.room_img, fg='green')
        self.room6.config(image=self.room_img, fg='white')
        self.room8.config(image=self.room_img, fg='white')
        self.room9.config(image=self.room_img, fg='white')
        self.room10.config(image=self.room_img, fg='white')
        self.droom_frame()


    def roomm9(self):
        self.frame_main.place_forget()
        self.droominfo.config(image=self.room_img, fg='white')
        self.room6.config(image=self.room_img, fg='green')
        self.room7.config(image=self.room_img, fg='white')
        self.room8.config(image=self.room_img, fg='white')
        self.room9.config(image=self.room_img, fg='white')
        self.room10.config(image=self.room_img, fg='white')
        self.droom_frame()

    def roomm6(self):
        self.frame_main.place_forget()
        self.droominfo.config(image=self.room_img, fg='white')
        self.room8.config(image=self.room_img, fg='green')
        self.room6.config(image=self.room_img, fg='white')
        self.room7.config(image=self.room_img, fg='white')
        self.room9.config(image=self.room_img, fg='white')
        self.room10.config(image=self.room_img, fg='white')
        self.droom_frame()

    def roomm7(self):
        self.frame_main.place_forget()
        self.droominfo.config(image=self.room_img, fg='white')
        self.room9.config(image=self.room_img, fg='green')
        self.room6.config(image=self.room_img, fg='white')
        self.room7.config(image=self.room_img, fg='white')
        self.room8.config(image=self.room_img, fg='white')
        self.room10.config(image=self.room_img, fg='white')
        self.droom_frame()
    def roomm8(self):
        self.frame_main.place_forget()
        self.droominfo.config(image=self.room_img, fg='white')
        self.room10.config(image=self.room_img, fg='green')
        self.room6.config(image=self.room_img, fg='white')
        self.room7.config(image=self.room_img, fg='white')
        self.room8.config(image=self.room_img, fg='white')
        self.room9.config(image=self.room_img, fg='white')
        self.droom_frame()
    def villa1(self):
        self.villainfo.config(image=self.room_img,fg='white')
        self.villa101.config(image=self.room_img, fg='green')
        self.villa102.config(image=self.room_img, fg='white')
        self.villa103.config(image=self.room_img, fg='white')
        self.villa104.config(image=self.room_img, fg='white')
        self.villa105.config(image=self.room_img, fg='white')
        self.villa_frame()

    def villa2(self):
        self.villainfo.config(image=self.room_img,fg='white')
        self.villa102.config(image=self.room_img, fg='green')
        self.villa101.config(image=self.room_img, fg='white')
        self.villa103.config(image=self.room_img, fg='white')
        self.villa104.config(image=self.room_img, fg='white')
        self.villa105.config(image=self.room_img, fg='white')
        self.villa_frame()

    def villa3(self):
        self.villainfo.config(image=self.room_img,fg='white')
        self.villa103.config(image=self.room_img, fg='green')
        self.villa102.config(image=self.room_img, fg='white')
        self.villa101.config(image=self.room_img, fg='white')
        self.villa104.config(image=self.room_img, fg='white')
        self.villa105.config(image=self.room_img, fg='white')
        self.villa_frame()

    def villa4(self):
        self.villainfo.config(image=self.room_img,fg='white')
        self.villa104.config(image=self.room_img, fg='green')
        self.villa102.config(image=self.room_img, fg='white')
        self.villa103.config(image=self.room_img, fg='white')
        self.villa101.config(image=self.room_img, fg='white')
        self.villa105.config(image=self.room_img, fg='white')
        self.villa_frame()

    def villa5(self):
        self.villainfo.config(image=self.room_img,fg='white')
        self.villa105.config(image=self.room_img, fg='green')
        self.villa102.config(image=self.room_img, fg='white')
        self.villa103.config(image=self.room_img, fg='white')
        self.villa104.config(image=self.room_img, fg='white')
        self.villa101.config(image=self.room_img, fg='white')
        self.villa_frame()

    def villa_info(self):
        self.villainfo.config(image=self.room_img,fg='green')
        self.villa101.config(image=self.room_img, fg='white')
        self.villa102.config(image=self.room_img, fg='white')
        self.villa103.config(image=self.room_img, fg='white')
        self.villa104.config(image=self.room_img, fg='white')
        self.villa105.config(image=self.room_img, fg='white')
        self.villa_infoframe()
    def hall16(self):

        self.frame_main.place_forget()
        self.hall1.config(image=self.room_img, fg='green')
        self.hall2.config(image=self.room_img, fg='white')
        self.hall3.config(image=self.room_img, fg='white')
        self.frame_hall1=LabelFrame(self.frame_hall,height=500,width=950,borderwidth=5)
        self.frame_hall1.place(x=50,y=100)
        self.frame_hall1.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_hall1)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.vpicc=Image.open('vinfo.png')
        self.vg=ImageTk.PhotoImage(self.vpicc,master=self.root4)
        self.lblv=Label(self.frame_hall1,image=self.vg).place(x=0,y=0,width=937,height=490)

    def hall17(self):

        self.hall2.config(image=self.room_img, fg='green')
        self.hall1.config(image=self.room_img, fg='white')
        self.hall3.config(image=self.room_img, fg='white')
        self.frame_hall1=LabelFrame(self.frame_hall,height=500,width=950,borderwidth=5)
        self.frame_hall1.place(x=50,y=100)
        self.frame_hall1.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_hall1)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.vpicc=Image.open('vinfo.png')
        self.vg=ImageTk.PhotoImage(self.vpicc,master=self.root4)
        self.lblv=Label(self.frame_hall1,image=self.vg).place(x=0,y=0,width=937,height=490)
    def hall18(self):

        self.hall3.config(image=self.room_img, fg='green')
        self.hall2.config(image=self.room_img, fg='white')
        self.hall1.config(image=self.room_img, fg='white')
        self.frame_hall1=LabelFrame(self.frame_hall,height=500,width=950,borderwidth=5)
        self.frame_hall1.place(x=50,y=100)
        self.frame_hall1.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_hall1)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.vpicc=Image.open('vinfo.png')
        self.vg=ImageTk.PhotoImage(self.vpicc,master=self.root4)
        self.lblv=Label(self.frame_hall1,image=self.vg).place(x=0,y=0,width=937,height=490)
    def room_frame(self):
        self.frame_main.place_forget()
        self.frame_room123 =LabelFrame(self.frame_standardroom, height=500, width=950, borderwidth=5)
        self.frame_room123.place(x=50, y=100)
        self.frame_room123.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_room123)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.rpic=Image.open('Standard-room.jpg')
        self.lg=ImageTk.PhotoImage(self.rpic,master=self.root4)
        self.lbl1=Label(self.frame_room123,image=self.lg).place(x=0,y=0,width=937,height=485)

    def droom_frame(self):
        self.frame_main.place_forget()
        self.frame_room12 =LabelFrame(self.frame_deluxeroom, height=500, width=950, borderwidth=5)
        self.frame_room12.place(x=50, y=100)
        self.frame_room12.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_room12)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.rpic=Image.open('droom.jpg')
        self.lg=ImageTk.PhotoImage(self.rpic,master=self.root4)
        self.lbl1=Label(self.frame_room12,image=self.lg).place(x=0,y=0,width=937,height=490)

    def villa_frame(self):
        self.frame_main.place_forget()
        self.frame_villa12=LabelFrame(self.frame_villa,height=500,width=950,borderwidth=5)
        self.frame_villa12.place(x=50,y=100)
        self.frame_villa12.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_villa12)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.vpic=Image.open('villa.jpg')
        self.vg=ImageTk.PhotoImage(self.vpic,master=self.root4)
        self.lblv=Label(self.frame_villa12,image=self.vg).place(x=0,y=0,width=937,height=490)

    def villa_infoframe(self):
        self.frame_main.place_forget()
        self.frame_villa123=LabelFrame(self.frame_villa,height=500,width=950,borderwidth=5)
        self.frame_villa123.place(x=50,y=100)
        self.frame_villa123.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_villa123)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.vpicc=Image.open('vinfo.png')
        self.vg=ImageTk.PhotoImage(self.vpicc,master=self.root4)
        self.lblv=Label(self.frame_villa123,image=self.vg).place(x=0,y=0,width=937,height=490)


    def sroom_infoframe(self):
        self.frame_main.place_forget()
        self.frame_sroom123=LabelFrame(self.frame_standardroom,height=500,width=950,borderwidth=5)
        self.frame_sroom123.place(x=50,y=100)
        self.frame_sroom123.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_sroom123)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.vpicc=Image.open('sroom.png')
        self.vg=ImageTk.PhotoImage(self.vpicc,master=self.root4)
        self.lblv=Label(self.frame_sroom123,image=self.vg).place(x=0,y=0,width=937,height=490)

    def droom_infoframe(self):

        self.frame_main.place_forget()
        self.frame_droom123=LabelFrame(self.frame_deluxeroom,height=500,width=950,borderwidth=5)
        self.frame_droom123.place(x=50,y=100)
        self.frame_droom123.pack_propagate(False)
        self.my_canvas_room = Canvas(self.frame_droom123)
        self.my_canvas_room.pack(fill="both", expand=True)
        self.vpicc=Image.open('droom.png')
        self.vg=ImageTk.PhotoImage(self.vpicc,master=self.root4)
        self.lblv=Label(self.frame_droom123,image=self.vg).place(x=0,y=0,width=937,height=490)


