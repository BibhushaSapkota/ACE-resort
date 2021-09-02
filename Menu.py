from tkinter import *
from PIL import ImageTk,Image
import custom_burger
from tkinter import messagebox
import mysql.connector

class run:
    def __init__(self,master):

        self.root=master
        self.root.state('zoomed')
        self.img=ImageTk.PhotoImage(Image.open(f'menu_bg.png'),master=self.root)
        print(self.img)
        self.my_canvas=Canvas(self.root)
        self.my_canvas.pack(fill='both',expand=True)
        self.my_canvas.create_image(0,0,image=self.img,anchor='nw')

        title=Label(self.root,text='MENU',font=("times new roman",40,'bold'),bg='black',fg='grey').place(x=615,y=35)

        quantity = Label(self.root,text='Quantity', font=("times new roman", 15, 'bold'), bg='black',
                     fg='grey').place(x=490, y=133)
        #momo
        momo = Label(self.root,text='Momo', font=("times new roman", 18, 'bold'), bg='black',
                            fg='grey').place(x=220, y=135)

        #chicken momo
        chiken_momo = Label( self.root,text='Chicken Momo----------------------------', font=("times new roman", 12, 'bold'), bg='black',
                      fg='grey').place(x=220, y=160)
        cmomo_price= Label( self.root,text='190', font=("times new roman", 12, 'bold'), bg='black',
                      fg='grey').place(x=450, y=160)
        self.txt_chicken_momo = Entry( self.root,font=("times new roman", 12), bg='grey')
        self.txt_chicken_momo.place(x=500, y=160, width=40)

        #buff momo
        buff_momo = Label(self.root,text='Buff Momo------------------------------', font=("times new roman", 12, 'bold'),
                            bg='black', fg='grey').place(x=220, y=180)
        bmomo_price = Label(self.root,text='150', font=("times new roman", 12, 'bold'), bg='black',
                            fg='grey').place(x=450, y=180)
        self.txt_buff_momo = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_buff_momo.place(x=500, y=180, width=40)

        # veg momo
        vegg_momo = Label(self.root,text='Veg Momo------------------------------', font=("times new roman", 12, 'bold'),
                          bg='black',
                          fg='grey').place(x=220, y=200)
        vmomo_price = Label(self.root,text='120', font=("times new roman", 12, 'bold'), bg='black',
                            fg='grey').place(x=450, y=200)
        self.txt_vegg_momo = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_vegg_momo.place(x=500, y=200, width=40)

        #pizza
        pizza = Label(self.root,text='Pizza', font=("times new roman", 18, 'bold'), bg='black',
                     fg='grey').place(x=220, y=255)

        #pizza
        chicken_pizza = Label(self.root,text='Chicken Pizza---------------------------', font=("times new roman", 12, 'bold'),
                          bg='black',
                          fg='grey').place(x=220, y=280)
        cpizza_price = Label(self.root,text='450', font=("times new roman", 12, 'bold'), bg='black',
                            fg='grey').place(x=450, y=280)
        self.txt_chicken_pizza = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_chicken_pizza.place(x=500, y=280, width=40)

        #alfungi pizza
        alfungi_pizza = Label(self.root,text='Alfungi Pizza-----------------------------', font=("times new roman", 12, 'bold'),
                              bg='black',
                              fg='grey').place(x=220, y=300)
        apizza_price = Label(self.root,text='390', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=450, y=300)
        self.txt_alfungi_pizza = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_alfungi_pizza.place(x=500, y=300, width=40)

        # Cheese pizza
        cheese_pizza = Label(self.root,text='Cheese Pizza---------------------------', font=("times new roman", 12, 'bold'),
                              bg='black',
                              fg='grey').place(x=220, y=320)
        chpizza_price = Label(self.root,text='350', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=450, y=320)
        self.txt_cheese_pizza = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_cheese_pizza.place(x=500, y=320, width=40)

        # Burger
        burger = Label(self.root,text='Burger', font=("times new roman", 18, 'bold'), bg='black',
                      fg='grey').place(x=220, y=380)

        #ham Burger
        ham_burger = Label(self.root,text='Ham Burger-----------------------------', font=("times new roman", 12, 'bold'),
                             bg='black',
                             fg='grey').place(x=220, y=405)
        hburger_price = Label(self.root,text='250', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=450, y=405)
        self.txt_ham_burger = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_ham_burger.place(x=500, y=405, width=40)

        #chicken Burger
        chicken_burger = Label(self.root,text='Chicken Burger---------------------------', font=("times new roman", 12, 'bold'),
                           bg='black',
                           fg='grey').place(x=220, y=425)
        cburger_price = Label(self.root,text='290', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=450, y=425)
        self.txt_chicken_burger = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_chicken_burger.place(x=500, y=425, width=40)

        #mix Burger
        mix_burger = Label(self.root,text='Mix Burger------------------------------', font=("times new roman", 12, 'bold'),
                               bg='black',
                               fg='grey').place(x=220, y=445)
        mburger_price = Label(self.root,text='300', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=450, y=445)
        self.txt_mix_burger = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_mix_burger.place(x=500, y=445, width=40)

        #sizzler

        sizzlers = Label(self.root,text='Sizzler', font=("times new roman", 18, 'bold'), bg='black',
                       fg='grey').place(x=220, y=500)

        sizzler = Label(self.root,text='Special Sizzler----------------------------', font=("times new roman", 12, 'bold'),
                           bg='black',
                           fg='grey').place(x=220, y=525)
        sizzler_price = Label(self.root,text='300', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=450, y=525)
        self.txt_sizzler = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_sizzler.place(x=500, y=525, width=40)

        #newari khajaset
        # Newari cuisine
        newari = Label(self.root,text='Newari Cuisine', font=("times new roman", 18, 'bold'), bg='black',
                       fg='grey').place(x=730, y=135)
        #khajaset

        newari_khajaset = Label(self.root,text='Khaja Set ---------------------------------', font=("times new roman", 12, 'bold'),
                         bg='black',fg='grey').place(x=730, y=160)
        nkhaja_price = Label(self.root,text='350', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=960, y=160)
        self.txt_newari_khaja = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_newari_khaja.place(x=1000, y=160, width=40)

        #yomari
        yomari = Label(self.root,text='Yomari ------------------------------------',
                                font=("times new roman", 12, 'bold'),
                                bg='black',
                                fg='grey').place(x=730, y=180)
        yomari_price = Label(self.root,text='100', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=960, y=180)
        self.txt_yomari = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_yomari.place(x=1000, y=180, width=40)

        #choila
        choila= Label(self.root,text='Choila ------------------------------------',
                       font=("times new roman", 12, 'bold'),
                       bg='black',
                       fg='grey').place(x=730, y=200)
        choila_price = Label(self.root,text='200', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=960, y=200)
        self.txt_choila = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_choila.place(x=1000, y=200, width=40)

        #thakali set
        thakali_set = Label(self.root,text='Thakali Set', font=("times new roman", 18, 'bold'), bg='black',
                       fg='grey').place(x=730, y=255)

        Thakali_set = Label(self.root,text='Thakali Set ---------------------------------',
                       font=("times new roman", 12, 'bold'),
                       bg='black',
                       fg='grey').place(x=730, y=280)
        Thakali_set_price = Label(self.root,text='500', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=960, y=280)
        self.txt_Thakali_set= Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_Thakali_set.place(x=1000, y=280, width=40)

        #sekuwa
        sekuwa = Label(self.root,text='Sekuwa', font=("times new roman", 18, 'bold'), bg='black',
                            fg='grey').place(x=730, y=380)

        chicken_sekuwa = Label(self.root,text='Chicken Sekuwa -----------------------',
                            font=("times new roman", 12, 'bold'),
                            bg='black',
                            fg='grey').place(x=730, y=410)
        csekuwa_price = Label(self.root,text='600', font=("times new roman", 12, 'bold'), bg='black',
                                  fg='grey').place(x=960, y=410)
        self.txt_chicken_sekuwa = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_chicken_sekuwa.place(x=1000, y=410, width=40)

        pork_sekuwa = Label(self.root,text='Pork Sekuwa --------------------------',
                               font=("times new roman", 12, 'bold'),
                               bg='black',
                               fg='grey').place(x=730, y=430)
        psekuwa_price = Label(self.root,text='530', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=960, y=430)
        self.txt_pork_sekuwa = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_pork_sekuwa.place(x=1000, y=430, width=40)

        buff_sekuwa = Label(self.root,text='Pork Sekuwa --------------------------',
                            font=("times new roman", 12, 'bold'),
                            bg='black',
                            fg='grey').place(x=730, y=450)
        bsekuwa_price = Label(self.root,text='560', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=960, y=450)
        self.txt_buff_sekuwa = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_buff_sekuwa.place(x=1000, y=450, width=40)

        soft_drink = Label(self.root,text='Soft Drink', font=("times new roman", 18, 'bold'), bg='black',
                       fg='grey').place(x=730, y=495)

        coke = Label(self.root,text='Coke------------------------------------------',
                            font=("times new roman", 12, 'bold'),
                            bg='black',
                            fg='grey').place(x=730, y=520)
        coke_price = Label(self.root,text='100', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=960, y=520)
        self.txt_coke = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_coke.place(x=1000, y=520, width=40)

        dew = Label(self.root,text='Mountain Dew--------------------------',
                     font=("times new roman", 12, 'bold'),
                     bg='black',
                     fg='grey').place(x=730, y=540)
        Mdew_price = Label(self.root,text='100', font=("times new roman", 12, 'bold'), bg='black',
                           fg='grey').place(x=960, y=540)
        self.txt_dew = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_dew.place(x=1000, y=540, width=40)

        fanta = Label(self.root,text='Fanta---------------------------------------',
                    font=("times new roman", 12, 'bold'),
                    bg='black',
                    fg='grey').place(x=730, y=560)
        fanta_price = Label(self.root,text='100', font=("times new roman", 12, 'bold'), bg='black',
                           fg='grey').place(x=960, y=560)
        self.txt_fanta = Entry(self.root,font=("times new roman", 12), bg='grey')
        self.txt_fanta.place(x=1000, y=560, width=40)

        self.custom_menu=Button(self.root,text="Custom Burgar", font=("times new roman", 20, 'bold'), bg='black',
                           fg='grey',command=self.custom)
        self.custom_menu.place(x=650,y=620)

        self.register_btn = Button(self.root,text="  Submit  ",font=("times new roman",18,'bold'), bg='black',
                                   fg='grey',command=self.register_menu)
        self.register_btn.place(x=450, y=620)



        self.root.mainloop()

    def clear_data(self):
        self.txt_chicken_momo.delete(0, END)
        self.txt_buff_momo.delete(0, END)
        self.txt_vegg_momo.delete(0, END)
        self.txt_chicken_pizza.delete(0, END)
        self.txt_alfungi_pizza.delete(0, END)
        self.txt_cheese_pizza.delete(0, END)
        self.txt_ham_burger.delete(0, END)
        self.txt_chicken_burger.delete(0, END)
        self.txt_mix_burger.delete(0, END)
        self.txt_sizzler.delete(0,END)
        self.txt_newari_khaja.delete(0,END)
        self.txt_yomari.delete(0, END)
        self.txt_choila.delete(0, END)
        self.txt_Thakali_set.delete(0, END)
        self.txt_chicken_sekuwa.delete(0, END)
        self.txt_buff_sekuwa.delete(0, END)
        self.txt_pork_sekuwa.delete(0, END)
        self.txt_coke.delete(0, END)
        self.txt_dew.delete(0, END)
        self.txt_fanta.delete(0, END)

    def register_menu(self):

        try:
            con = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9869167415',
                port=3306,
                database='login_registration')
            cur = con.cursor()

            chicken_momo = self.txt_chicken_momo.get()
            buff_momo = self.txt_buff_momo.get()
            vegg_momo =self.txt_vegg_momo.get()
            chicken_pizza = self.txt_chicken_pizza.get()
            alfungi_pizza=self.txt_alfungi_pizza.get()
            cheese_pizza=self.txt_cheese_pizza.get()
            ham_burger=self.txt_ham_burger.get()
            chicken_burger=self.txt_chicken_burger.get()
            mix_burger=self.txt_mix_burger.get()
            sizzler=self.txt_sizzler.get()
            newari_khajaset=self.txt_newari_khaja.get()
            yomari=self.txt_yomari.get()
            choila=self.txt_choila.get()
            Thakali_set=self.txt_Thakali_set.get()
            chicken_sekuwa=self.txt_chicken_sekuwa.get()
            pork_sekuwa=self.txt_pork_sekuwa.get()
            buff_sekuwa=self.txt_buff_sekuwa.get()
            coke=self.txt_coke.get()
            dew=self.txt_dew.get()
            fanta=self.txt_fanta.get()

            sql = "insert into registration(fname,lname,contact_number,username,gender,age,password,security_question,answer) " \
                  "values('" + chicken_momo + "','" +buff_momo+ "'," + vegg_momo + "," \
                    "'" + chicken_pizza + "','" + alfungi_pizza + "'," + cheese_pizza+ ",'" + ham_burger + "'," \
                    "'" + chicken_burger + "','" + mix_burger + "','" + sizzler + "','" + newari_khajaset + "'," \
                    " '" +yomari+"','"+choila+"','"+Thakali_set+"','"+chicken_sekuwa+"','"+pork_sekuwa+"'," \
                    " '"+buff_sekuwa+"','"+coke+"','"+dew+"','"+fanta+"')"

            values = cur.execute(sql)

            con.commit()
            con.close()
            messagebox.showinfo("success", "You have been successfully registered", parent=self.root)
            self.clear_data()

        except:
            print('error')
            pass


    def custom(self):
        custom_burger.CustomBurger(Toplevel())