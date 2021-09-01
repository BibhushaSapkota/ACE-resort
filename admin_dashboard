from tkinter import *

from PIL import Image,ImageTk
from tkinter import ttk

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
                                     border='0', overrelief="sunken", compound=CENTER )
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

        self.frame_main = LabelFrame(self.root5, height=650, width=1040, borderwidth=10)
        self.frame_main.place(x=300, y=130)
        self.frame_main.pack_propagate(False)


root5=Tk()
obj=admin(root5)
root5.mainloop()
