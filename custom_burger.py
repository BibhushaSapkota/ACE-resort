from tkinter import *
from time import sleep
from PIL import ImageTk, Image
import mysql.connector
import Login


class CustomBurger:
    def __init__(self,master):
        self.root=master
        self.root.config(bg="black")
        self.root.title("Custom Loader")
        self.root.state('zoomed')
        self.main_frame_fn()
        self.a=550
        self.b=230
        self.count=0
        self.count_pi=0
        self.count_fi=0
        self.count_ch=0
        self.count_ce=0
        self.count_to=0
        self.count_sp = 0
        self.total=0
        self.qty_total=0
        self._pice_1=0
        self.total_all=0
        self.before = 0
        self.after = 0
        self.before_qty = 0
        self.after_qty = 0
        self.root.update()
        self.root.mainloop()
    def main_frame_fn(self):
        self.frame_main = LabelFrame(self.root, height= self.root.winfo_screenheight(), width=self.root.winfo_screenwidth())
        self.frame_main.place(x=0, y=0)
        self.frame_main.pack_propagate(False)
        self.my_canvas = Canvas(self.frame_main)
        self.my_canvas.pack(fill="both", expand=True)
        self.back1 = ImageTk.PhotoImage(Image.open(f'burger_background.jpg'),master=self.root)
        self.my_canvas.create_image(0, 0, image=self.back1, anchor="nw")
        self.btn_img = ImageTk.PhotoImage(Image.open(f'btn_img.png'),master=self.root)
        self.btn_img_small = ImageTk.PhotoImage(Image.open(f'btn_img_small.png'),master=self.root)
        self.img_box =Image.open('burgar_box.png')
        self.img_box = self.img_box.resize((600,80), Image.ANTIALIAS)
        self.box_img = ImageTk.PhotoImage(self.img_box,master=self.root)

        self.my_canvas.create_image(720, 180, image=self.box_img, anchor="nw")
        self.my_canvas.create_text(1000, 225, text="CUSTOM PIZZA", font=("Algerian", 30, 'bold'), fill="black")

        self.my_canvas.create_image(60, 180, image=self.box_img, anchor="nw")
        self.my_canvas.create_text(340, 225, text="CUSTOM BURGER", font=("Algerian", 30, 'bold'), fill="black")

        self.my_canvas.create_image(400, 70, image=self.box_img, anchor="nw")
        self.my_canvas.create_text(680, 110, text="CUSTOM MENU", font=("Algerian", 40, 'bold'), fill="black")

        # setting background image in canvas.
        self.btn_fire = ImageTk.PhotoImage(Image.open(f'fire.png'),master=self.root)
        self.btn_top_p=Button(self.frame_main,text="\n \n \nStart making",cursor="hand2",
                           font=("Algerian", 40, 'bold'),compound=CENTER,fg="white",image=self.btn_fire,borderwidth=10,command=self.burger_buttom)
        self.btn_top_p.place(x=100,y=300)
        self.btn_fire_pizza = ImageTk.PhotoImage(Image.open(f'firepizza.png'),master=self.root)
        self.btn_pizza = Button(self.frame_main, text="\n \n \nStart making", cursor="hand2",
                                font=("Algerian", 40, 'bold'), compound=CENTER, fg="white", image=self.btn_fire_pizza,
                                borderwidth=10, command=self.burger_buttom)
        self.btn_pizza.place(x=770, y=300)

    def reset(self):
        self.a = 550
        self.b = 230
        self.btn_top.config(state=NORMAL)
        self.btn_chees.config(state=NORMAL)
        self.btn_tomato.config(state=NORMAL)
        self.btn_chicken.config(state=NORMAL)
        self.btn_pickle.config(state=NORMAL)
        self.btn_spinach.config(state=NORMAL)
        self.btn_fish.config(state=NORMAL)
        self.qty_inc.config(state=DISABLED)
        self.qty_dec.config(state=DISABLED)
        self.count = 0
        self.count_pi = 0
        self.count_fi = 0
        self.count_ch = 0
        self.count_ce = 0
        self.count_to = 0
        self.count_sp = 0
        self.total = 0
        self.qty_total = 0
        self._pice_1 = 0
        self.total_all = 0
        self.before = 0
        self.after=0
        self.before_qty=0
        self.after_qty=0
        self.tot_qty.config(text=self.qty_total)
        self.login2 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login2, anchor="nw")
        self.login3 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login3, anchor="nw")
        self.login4 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login4, anchor="nw")
        self.login5 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login5, anchor="nw")
        self.login = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login, anchor="nw")
        self.login6 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login6, anchor="nw")
        self.login7 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login7, anchor="nw")
        self.btn_tomato.config(text="Tomato:No", bg="black",fg="red4")
        self.btn_chicken.config(text="Chicken:No", bg="black",fg="red4")
        self.btn_chees.config(text="Cheese:No", bg="black",fg="red4")
        self.btn_pickle.config(text="Pickle:No", bg="black",fg="red4")
        self.btn_fish.config(text="Fish:No", bg="black",fg="red4")
        self.btn_spinach.config(text="Spinach:No", bg="black", fg="red4")
        self.total_cost.config(text=self.total)
    def burger_buttom(self):
        self.frame_main.place_forget()
        self.frame_burger = LabelFrame(self.root, height=self.root.winfo_screenheight(),
                                     width=self.root.winfo_screenwidth())
        self.frame_burger.place(x=0, y=0)
        self.frame_burger.pack_propagate(False)
        self.my_canvas_bur = Canvas(self.frame_burger)
        self.my_canvas_bur.pack(fill="both", expand=True)

        self.back2 = ImageTk.PhotoImage(Image.open(f'burger_background.jpg'),master=self.root)
        self.my_canvas_bur.create_image(0, 0, image=self.back2, anchor="nw")

        self.my_canvas_bur.create_image(380, 50, image=self.box_img, anchor="nw")
        self.my_canvas_bur.create_text(650, 95, text="CUSTOM BURGER", font=("Algerian", 30, 'bold'), fill="black")

        self.my_canvas_bur.create_line(1020, 140, 1020, 440, width=5, fill="black")
        self.my_canvas_bur.create_rectangle(730, 140, 1300, 440, width=5)
        self.my_canvas_bur.create_text(840, 170, text="Veg", font=("Algerian", 30, 'bold'), fill="black")
        self.my_canvas_bur.create_text(1130, 170, text="Non-veg", font=("Algerian", 30, 'bold'), fill="black")
        self.my_canvas_bur.create_text(980, 170, text="(Price)", font=("Areal", 15, 'bold'), fill="black")
        self.my_canvas_bur.create_text(1265, 170, text="(Price)", font=("Areal", 15, 'bold'), fill="black")

        self.my_canvas_bur.create_text(960, 585, text="Total : Rs", font=("Areal", 21, 'bold'), fill="black")
        self.my_canvas_bur.create_text(930, 530, text="Quantity : ", font=("Areal", 21, 'bold'), fill="black")

        self.my_canvas_bur.create_text(980, 220, text="Rs 15", font=("Areal", 15, 'bold'), fill="black")
        self.my_canvas_bur.create_text(980, 280, text="Rs 10", font=("Areal", 15, 'bold'), fill="black")
        self.my_canvas_bur.create_text(980, 340, text="Rs 20", font=("Areal", 15, 'bold'), fill="black")
        self.my_canvas_bur.create_text(980, 400, text="Rs 50", font=("Areal", 15, 'bold'), fill="black")

        self.my_canvas_bur.create_text(1265, 250, text="Rs 80", font=("Areal", 15, 'bold'), fill="black")
        self.my_canvas_bur.create_text(1265, 350, text="Rs 70", font=("Areal", 15, 'bold'), fill="black")


        self.btn_tomato = Button(self.frame_burger, text="Tomato:No", image=self.btn_img_small,
                                 compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                 command=self.burger_tomato)
        self.btn_tomato.place(x=740, y=250)


        self.btn_pickle = Button(self.frame_burger, text="Pickle:No", image=self.btn_img_small,
                                 compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                 command=self.burger_pickel)
        self.btn_pickle.place(x=740, y=310)
        self.btn_chees = Button(self.frame_burger, text="Cheese:No", image=self.btn_img_small,
                                compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                command=self.burger_chees)
        self.btn_chees.place(x=740, y=370)
        self.btn_chicken = Button(self.frame_burger, text="Chicken:No", image=self.btn_img_small,
                                  compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                  command=self.burger_chicken)
        self.btn_chicken.place(x=1030, y=320)
        self.btn_fish = Button(self.frame_burger, text="Fish:No", image=self.btn_img_small,
                                  compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                                  command=self.burger_fish)
        self.btn_fish.place(x=1030, y=220)
        self.btn_spinach = Button(self.frame_burger, text="Spinach:No", image=self.btn_img_small,
                               compound=CENTER, font=("Algerian", 20, 'bold'), fg="red4",
                               command=self.burger_spinach)
        self.btn_spinach.place(x=740, y=190)
        self.btn_reset = Button(self.frame_burger, text="Reset",width=8,
                                compound=CENTER, command=self.reset,font=("Algerian", 20, 'bold'))
        self.btn_reset.place(x=1140, y=450)
        self.btn_top= Button(self.frame_burger, text="Finish",width=8,
                                 compound=CENTER, font=("Algerian", 20, 'bold'),
                                 command=self.burger_top)
        self.btn_top.place(x=760, y=450)
        self.btn_add = Button(self.frame_burger, text="Add New",width=8,command=self.add_new,
                              compound=CENTER, font=("Algerian", 20, 'bold'),state=DISABLED)
        self.btn_add.place(x=950, y=450)
        self.qty_inc = Button(self.frame_burger, text="+1",state=DISABLED,width=2,
                              compound=CENTER, font=("Areal", 15, 'bold'),command=self.qty_increase)
        self.qty_inc.place(x=1000, y=510)
        self.qty_dec = Button(self.frame_burger, text="-1",state=DISABLED,width=2,
                              compound=CENTER, font=("Areal", 15, 'bold'),command=self.qty_decrease)
        self.qty_dec.place(x=1050, y=510)
        self.giv_ord = Button(self.frame_burger, text="Give Order",width=10,bg="green",
                              compound=CENTER, font=("Areal", 17, 'bold'),state=DISABLED,command=self.give_order)
        self.giv_ord.place(x=850, y=610)
        self.go_bac = Button(self.frame_burger, text="Go Back", width=10,bg="red",
                              compound=CENTER, font=("Areal", 17, 'bold'), command=self.go_back)
        self.go_bac.place(x=1050, y=610)

        self.total=self.total+0

        self.total_cost=Label(self.frame_burger,text="0",font=("areal", 20, 'bold'),width=4)
        self.total_cost.place(x=1040,y=565)
        self.tot_qty = Label(self.frame_burger, text="0", font=("areal", 20, 'bold'), width=4)
        self.tot_qty.place(x=1100, y=515)
        self.total_cost.config(text=self.total)
        for i in range(1, 7):
            self.login1 = ImageTk.PhotoImage(Image.open(f'bunbutton_img/{i}.png'),master=self.root)
            self.my_canvas_bur.create_image(self.b, self.a, image=self.login1, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()
    def qty_increase(self):
        self.qty_total=self.qty_total+1
        self.tot_qty.config(text=self.qty_total)
        if self.btn_add.cget('text')=='Add New ':
            self.total = self.total + self.after
            self.total_cost.config(text=self.total)
        else:
            self.total = self.total + self._pice_1
            self.total_cost.config(text=self.total)
        self.total_all=self.total


    def qty_decrease(self):
        if self.qty_total <= 1:
            self.qty_total=1
            self.tot_qty.config(text=self.qty_total)
        elif self.btn_add.cget('text') == 'Add New ':
            print(self.qty_total)
            if self.qty_total-self.before_qty==0:
                self.qty_total=self.qty_total
                self.tot_qty.config(text=self.qty_total)
            else:
                self.qty_total = self.qty_total - 1
                self.tot_qty.config(text=self.qty_total)
                self.total = self.total - self.after
                self.total_cost.config(text=self.total)
        else:
            self.total = self.total - self._pice_1
            self.qty_total = self.qty_total - 1
            self.tot_qty.config(text=self.qty_total)
            self.total_cost.config(text=self.total)
    def give_order(self):
        self.qty = Entry(self.root, text=self.qty_total-self.before_qty)
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Janakidevi24#',
                port=3306,
                database='login_registration')
            cur = con.cursor()
            print(cur)

            sql = "insert into burgar(qty )" \
                  "values ( " + self.qty['text'] + ")"
            values = cur.execute(sql)

            con.commit()
            con.close()
        except:
            print('error')
            pass
    def go_back(self):
        self.qty = Entry(self.root, text='0')
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Janakidevi24#',
                port=3306,
                database='login_registration')
            cur = con.cursor()
            print(cur)

            sql = "insert into burgar(qty )" \
                  "values ( " + self.qty['text']+ ")"
            values = cur.execute(sql)

            con.commit()
            con.close()
        except:
            print('error')
            pass
        self.a = 550
        self.b = 230
        self.count = 0
        self.count_pi = 0
        self.count_fi = 0
        self.count_ch = 0
        self.count_ce = 0
        self.count_to = 0
        self.count_sp = 0
        self.total = 0
        self.qty_total = 0
        self._pice_1 = 0
        self.total_all = 0
        self.before = 0
        self.after = 0
        self.before_qty = 0
        self.after_qty = 0
        self.frame_burger.place_forget()
        self.main_frame_fn()

    def burger_top(self):
        self.pi = Entry(self.root, text=self.count_pi)
        self.fi = Entry(self.root, text=self.count_fi)
        self.ch = Entry(self.root, text=self.count_ch)
        self.ce = Entry(self.root, text=self.count_ce)
        self.to = Entry(self.root, text=self.count_to)
        self.sp = Entry(self.root, text=self.count_sp)

        print(self.sp['text'])
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Janakidevi24#',
                port=3306,
                database='login_registration')
            cur = con.cursor()
            print(cur)

            sql = "insert into burgar(username,spanich,tomato,pickel,cheese,fish,chicken)" \
                  "values ('"+Login.gett()+"'," + self.sp['text'] + "," + self.to['text'] + "," + self.pi['text'] + "," + self.ce[
                      'text'] + "," + self.fi['text'] + "," + self.ch['text'] + ")"
            values = cur.execute(sql)

            con.commit()
            con.close()
        except:
            print('error')
            pass

        self.total = self.total + 20
        self.total_cost.config(text=self.total)
        self.btn_top.config(state=DISABLED)
        self.qty_total = self.qty_total+1
        self.tot_qty.config(text=self.qty_total)
        self.btn_add.config(state=NORMAL)
        self._pice_1=self.total
        self.btn_chees.config(state=DISABLED)
        self.btn_tomato.config(state=DISABLED)
        self.btn_chicken.config(state=DISABLED)
        self.btn_pickle.config(state=DISABLED)
        self.btn_spinach.config(state=DISABLED)
        self.btn_fish.config(state=DISABLED)
        self.qty_inc.config(state=NORMAL)
        self.qty_dec.config(state=NORMAL)
        self.giv_ord.config(state=NORMAL)
        self.after = 0
        self.after = self.total - self.before
        for i in range(1, 7):
            self.login = ImageTk.PhotoImage(Image.open(f'buntop_img/{i}.png'),master=self.root)
            self.my_canvas_bur.create_image(self.b,self.a-50, image=self.login, anchor="nw")
            sleep(0.1)
            self.root.update_idletasks()
    def add_new(self):
        self.qty = Entry(self.root, text=self.qty_total-self.before_qty)
        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Janakidevi24#',
                port=3306,
                database='login_registration')
            cur = con.cursor()
            print(cur)

            sql = "insert into burgar(qty )" \
                  "values ( " + self.qty['text'] + ")"
            values = cur.execute(sql)

            con.commit()
            con.close()
        except:
            print('error')
            pass
        self.giv_ord.config(state=DISABLED)
        self.a = 550
        self.b = 230
        self.count_pi = 0
        self.count_fi = 0
        self.count_ch = 0
        self.count_ce = 0
        self.count_to = 0
        self.count_sp = 0
        self.btn_add.config(state=DISABLED)
        self.btn_top.config(state=NORMAL)
        self.btn_chees.config(state=NORMAL)
        self.btn_tomato.config(state=NORMAL)
        self.btn_chicken.config(state=NORMAL)
        self.btn_pickle.config(state=NORMAL)
        self.btn_spinach.config(state=NORMAL)
        self.btn_fish.config(state=NORMAL)
        self.qty_inc.config(state=DISABLED)
        self.qty_dec.config(state=DISABLED)
        self.btn_add.config(text="Add New ")
        self.login2 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login2, anchor="nw")
        self.login3 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login3, anchor="nw")
        self.login4 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login4, anchor="nw")
        self.login5 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login5, anchor="nw")
        self.login = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login, anchor="nw")
        self.login6 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login6, anchor="nw")
        self.login7 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
        self.my_canvas.create_image(self.b, self.a, image=self.login7, anchor="nw")
        self.btn_tomato.config(text="Tomato:No", bg="black", fg="red4")
        self.btn_chicken.config(text="Chicken:No", bg="black", fg="red4")
        self.btn_chees.config(text="Cheese:No", bg="black", fg="red4")
        self.btn_pickle.config(text="Pickle:No", bg="black", fg="red4")
        self.btn_fish.config(text="Fish:No", bg="black", fg="red4")
        self.btn_spinach.config(text="Spinach:No", bg="black", fg="red4")
        self.before_qty=self.qty_total
        self.before=self.total
    def burger_tomato(self):
        if self.btn_tomato.cget('text') == 'Tomato:No':
            self.total = self.total + 10
            self.total_cost.config(text=self.total)
            self.a = self.a - 50
            self.pos_to=self.a
            self.btn_tomato.config(text="Tomato:Yes", bg="black",fg="green")
            self.count=self.count+1
            self.count_to=self.count
            print("to"+str(self.count))
            print("to" + str(self.count_to))
            for i in range(1, 7):
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/{i}.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.a, image=self.login2, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            self.total = self.total - 10
            self.total_cost.config(text=self.total)

            if self.count_to <= self.count_pi:
                self.count_pi=self.count_pi-1
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_to < self.count_ch:
                self.count_ch=self.count_ch-1
                print(self.a)
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")
            if self.count_to < self.count_ce:
                self.count_ce = self.count_ce - 1
                print("ce")
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")
            if self.count_to < self.count_fi:
                self.count_fi = self.count_fi - 1
                print("ce")
                print(self.a)
                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            if self.count_to < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")

            self.a = self.a +50
            self.count = self.count - 1
            self.count_to = 0
            print("tor" + str(self.count))
            print("tor" + str(self.count_to))
            self.btn_tomato.config(text="Tomato:No", bg="black",fg="red4")
            self.login2 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas_bur.create_image(self.b, self.a, image=self.login2, anchor="nw")

    def burger_pickel(self):

        if self.btn_pickle.cget('text') == 'Pickle:No':
            self.total = self.total + 20
            self.total_cost.config(text=self.total)
            self.a = self.a - 50
            self.pos_pi = self.a
            self.btn_pickle.config(text="Pickle:Yes", bg="black",fg="green")
            self.count=self.count+1
            self.count_pi = self.count
            print("pi" + str(self.count))
            print("pi" + str(self.count_pi))
            for i in range(1, 7):
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/{i}.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.a, image=self.login3, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            self.total = self.total - 20
            self.total_cost.config(text=self.total)
            if self.count_pi <= self.count_to:
                self.count_to = self.count_to - 1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_pi, image=self.login2, anchor="nw")
            if self.count_pi < self.count_ch:
                self.count_ch = self.count_ch - 1
                print(self.a)
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")

            if self.count_pi < self.count_ce:
                self.count_ce = self.count_ce - 1
                print("ce")
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")
            if self.count_pi < self.count_fi:
                self.count_fi = self.count_fi - 1
                print("ce")
                print(self.a)
                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            if self.count_pi < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")


            self.a = self.a +50
            self.count = self.count - 1
            self.count_pi = 0
            print("tor" + str(self.count))
            print("tor" + str(self.count_to))
            self.btn_pickle.config(text="Pickle:No", bg="black",fg="red4")
            self.login3 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas_bur.create_image(self.b, self.a, image=self.login3, anchor="nw")



    def burger_chees(self):
        if self.btn_chees.cget('text') == 'Cheese:No':
            self.total = self.total + 50
            self.total_cost.config(text=self.total)
            self.a = self.a - 50
            self.pos_ce = self.a
            self.btn_chees.config(text="Cheese:Yes", bg="black",fg="green")
            self.count = self.count + 1
            self.count_ce = self.count
            print("ce" + str(self.count))
            print("ce" + str(self.count_ce))
            for i in range(1, 7):
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/{i}.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.a, image=self.login4, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            self.total = self.total - 50
            self.total_cost.config(text=self.total)
            if self.count_ce <= self.count_to:
                self.count_to = self.count_to - 1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_to, image=self.login2, anchor="nw")
            if self.count_ce < self.count_ch:
                self.count_ch = self.count_ch - 1
                print(self.a)
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")

            if self.count_ce < self.count_pi:
                self.count_pi = self.count_pi - 1
                print("ce")
                print(self.a)
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_ce < self.count_fi:
                self.count_fi = self.count_fi - 1
                print("ce")
                print(self.a)
                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            if self.count_ce < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")

            self.a = self.a +50
            self.count = self.count - 1
            self.count_ce = 0
            self.btn_chees.config(text="Cheese:No", bg="black",fg="red4")
            self.login4 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas_bur.create_image(self.b, self.a, image=self.login4, anchor="nw")

    def burger_chicken(self):
        if self.btn_chicken.cget('text') == 'Chicken:No':
            self.total = self.total + 70
            self.total_cost.config(text=self.total)
            self.a = self.a - 50
            self.pos_ch = self.a
            self.btn_chicken.config(text="Chicken:Yes", bg="black",fg="green")
            self.count = self.count + 1
            self.count_ch = self.count
            for i in range(1, 7):
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/{i}.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.a, image=self.login5, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            self.total = self.total - 70
            self.total_cost.config(text=self.total)
            if self.count_ch <= self.count_to:
                self.count_to=self.count_to-1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_to, image=self.login2, anchor="nw")
            if self.count_ch < self.count_ce:
                self.count_ce=self.count_ce-1
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")

            if self.count_ch < self.count_pi:
                self.count_pi = self.count_pi - 1
                print("ce")
                print(self.a)
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_ch < self.count_fi:
                self.count_fi = self.count_fi - 1
                print("ce")
                print(self.a)
                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            if self.count_ch < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")

            self.a = self.a +50

            self.count = self.count - 1
            self.count_ch = 0
            self.btn_chicken.config(text="Chicken:No", bg="black",fg="red4")
            self.login5 = ImageTk.PhotoImage(Image.open(f'remove.png'))
            self.my_canvas_bur.create_image(self.b, self.a, image=self.login5, anchor="nw")

    def burger_fish(self):

        if self.btn_fish.cget('text') == 'Fish:No':
            self.total = self.total + 80
            self.total_cost.config(text=self.total)
            self.a = self.a - 50
            self.pos_fi = self.a
            self.btn_fish.config(text="Fish:Yes", bg="black",fg="green")
            self.count = self.count + 1
            self.count_fi = self.count
            for i in range(1, 7):
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/{i}.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.a, image=self.login6, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            self.total = self.total - 80
            self.total_cost.config(text=self.total)
            if self.count_fi <= self.count_ch:
                self.count_ch=self.count_ch-1
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")
            if self.count_fi <= self.count_to:
                self.count_to=self.count_to-1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_to, image=self.login2, anchor="nw")
            if self.count_fi < self.count_ce:
                self.count_ce=self.count_ce-1
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")

            if self.count_fi < self.count_pi:
                self.count_pi = self.count_pi - 1
                print("ce")
                print(self.a)
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")
            if self.count_fi < self.count_sp:
                self.count_sp = self.count_sp - 1
                print("ce")
                print(self.a)
                self.pos_sp = self.pos_sp + 50
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_sp, image=self.login7, anchor="nw")

            self.a = self.a +50

            self.count = self.count - 1
            self.count_fi = 0
            self.btn_fish.config(text="Fish:No", bg="black",fg="red4")
            self.login6 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
            self.my_canvas_bur.create_image(self.b, self.a, image=self.login6, anchor="nw")

    def burger_spinach(self):
        if self.btn_spinach.cget('text') == 'Spinach:No':
            self.total = self.total + 15
            self.total_cost.config(text=self.total)
            self.a = self.a - 50
            self.pos_sp = self.a
            self.btn_spinach.config(text="Spinach:Yes", bg="black",fg="green")
            self.count = self.count + 1
            self.count_sp = self.count
            for i in range(1, 7):
                self.login7 = ImageTk.PhotoImage(Image.open(f'spinach_img/{i}.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.a, image=self.login7, anchor="nw")
                sleep(0.1)
                self.root.update_idletasks()
        else:
            self.total = self.total - 15
            self.total_cost.config(text=self.total)
            if self.count_sp <= self.count_ch:
                self.count_ch=self.count_ch-1
                self.pos_ch = self.pos_ch + 50
                self.login5 = ImageTk.PhotoImage(Image.open(f'chicken_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ch, image=self.login5, anchor="nw")
            if self.count_sp <= self.count_to:
                self.count_to=self.count_to-1
                self.pos_to = self.pos_to + 50
                self.login2 = ImageTk.PhotoImage(Image.open(f'tomato_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_to, image=self.login2, anchor="nw")

            if self.count_sp < self.count_ce:
                self.count_ce=self.count_ce-1
                print(self.a)
                self.pos_ce = self.pos_ce + 50
                self.login4 = ImageTk.PhotoImage(Image.open(f'cheese_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_ce, image=self.login4, anchor="nw")

            if self.count_sp < self.count_pi:
                self.count_pi = self.count_pi - 1
                print("ce")
                print(self.a)
                self.pos_pi = self.pos_pi + 50
                self.login3 = ImageTk.PhotoImage(Image.open(f'pickle_img/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_pi, image=self.login3, anchor="nw")


            if self.count_sp < self.count_fi:
                self.count_fi = self.count_fi - 1

                self.pos_fi = self.pos_fi + 50
                self.login6 = ImageTk.PhotoImage(Image.open(f'fish/6.png'),master=self.root)
                self.my_canvas_bur.create_image(self.b, self.pos_fi, image=self.login6, anchor="nw")
            self.a = self.a +50
            self.count = self.count - 1
            self.count_sp = 0
            self.btn_spinach.config(text="Spinach:No", bg="black",fg="red4")
            self.login7 = ImageTk.PhotoImage(Image.open(f'remove.png'),master=self.root)
            self.my_canvas_bur.create_image(self.b, self.a, image=self.login7, anchor="nw")


