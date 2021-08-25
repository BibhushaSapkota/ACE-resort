from tkinter import *
from PIL import ImageTk,Image

class run:
    def __init__(self):
        self.root=Tk()
        self.root.state('zoomed')
        self.img=ImageTk.PhotoImage(Image.open(f'menu_bg.png'))
        print(self.img)
        self.my_canvas=Canvas(self.root)
        self.my_canvas.pack(fill='both',expand=True)
        self.my_canvas.create_image(0,0,image=self.img,anchor='nw')




        title=Label(text='MENU',font=("times new roman",40,'bold'),bg='black',fg='grey').place(x=590,y=100)

        quantity = Label(text='Quantity', font=("times new roman", 15, 'bold'), bg='black',
                     fg='grey').place(x=480, y=200)
        #momo
        momo = Label(text='Momo', font=("times new roman", 18, 'bold'), bg='black',
                            fg='grey').place(x=220, y=200)

        #chicken momo
        chiken_momo = Label( text='Chicken Momo----------------------------', font=("times new roman", 12, 'bold'), bg='black',
                      fg='grey').place(x=220, y=230)
        cmomo_price= Label( text='190', font=("times new roman", 12, 'bold'), bg='black',
                      fg='grey').place(x=450, y=230)
        self.txt_chicken_momo = Entry( font=("times new roman", 12), bg='grey')
        self.txt_chicken_momo.place(x=500, y=230, width=40)

        #buff momo
        buff_momo = Label(text='Buff Momo------------------------------', font=("times new roman", 12, 'bold'),
                            bg='black', fg='grey').place(x=220, y=250)
        bmomo_price = Label(text='150', font=("times new roman", 12, 'bold'), bg='black',
                            fg='grey').place(x=450, y=250)
        self.txt_buff_momo = Entry(font=("times new roman", 12), bg='grey')
        self.txt_buff_momo.place(x=500, y=250, width=40)

        # veg momo
        vegg_momo = Label(text='Veg Momo------------------------------', font=("times new roman", 12, 'bold'),
                          bg='black',
                          fg='grey').place(x=220, y=270)
        vmomo_price = Label(text='120', font=("times new roman", 12, 'bold'), bg='black',
                            fg='grey').place(x=450, y=270)
        self.txt_chicken_momo = Entry(font=("times new roman", 12), bg='grey')
        self.txt_chicken_momo.place(x=500, y=270, width=40)

        #pizza
        pizza = Label(text='Pizza', font=("times new roman", 18, 'bold'), bg='black',
                     fg='grey').place(x=220, y=320)

        #pizza
        chicken_pizza = Label(text='Chicken Pizza---------------------------', font=("times new roman", 12, 'bold'),
                          bg='black',
                          fg='grey').place(x=220, y=350)
        cpizza_price = Label(text='450', font=("times new roman", 12, 'bold'), bg='black',
                            fg='grey').place(x=450, y=350)
        self.txt_chicken_pizza = Entry(font=("times new roman", 12), bg='grey')
        self.txt_chicken_pizza.place(x=500, y=350, width=40)

        #alfungi pizza
        alfungi_pizza = Label(text='Alfungi Pizza-----------------------------', font=("times new roman", 12, 'bold'),
                              bg='black',
                              fg='grey').place(x=220, y=370)
        apizza_price = Label(text='390', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=450, y=370)
        self.txt_alfungi_pizza = Entry(font=("times new roman", 12), bg='grey')
        self.txt_alfungi_pizza.place(x=500, y=370, width=40)

        # Cheese pizza
        cheese_pizza = Label(text='Cheese Pizza---------------------------', font=("times new roman", 12, 'bold'),
                              bg='black',
                              fg='grey').place(x=220, y=390)
        chpizza_price = Label(text='350', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=450, y=390)
        self.txt_cheese_pizza = Entry(font=("times new roman", 12), bg='grey')
        self.txt_cheese_pizza.place(x=500, y=390, width=40)

        # Burger
        burger = Label(text='Burger', font=("times new roman", 18, 'bold'), bg='black',
                      fg='grey').place(x=220, y=445)

        #ham Burger
        ham_burger = Label(text='Ham Burger-----------------------------', font=("times new roman", 12, 'bold'),
                             bg='black',
                             fg='grey').place(x=220, y=480)
        hburger_price = Label(text='250', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=450, y=480)
        self.txt_ham_burger = Entry(font=("times new roman", 12), bg='grey')
        self.txt_ham_burger.place(x=500, y=480, width=40)

        #chicken Burger
        chicken_burger = Label(text='Chicken Burger---------------------------', font=("times new roman", 12, 'bold'),
                           bg='black',
                           fg='grey').place(x=220, y=500)
        cburger_price = Label(text='290', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=450, y=500)
        self.txt_chicken_burger = Entry(font=("times new roman", 12), bg='grey')
        self.txt_chicken_burger.place(x=500, y=500, width=40)

        #mix Burger
        mix_burger = Label(text='Mix Burger------------------------------', font=("times new roman", 12, 'bold'),
                               bg='black',
                               fg='grey').place(x=220, y=520)
        mburger_price = Label(text='300', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=450, y=520)
        self.txt_mix_burger = Entry(font=("times new roman", 12), bg='grey')
        self.txt_mix_burger.place(x=500, y=520, width=40)

        #s

        special_ = Label(text='Special Sizzler----------------------------', font=("times new roman", 12, 'bold'),
                           bg='black',
                           fg='grey').place(x=220, y=600)
        mburger_price = Label(text='300', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=450, y=600)
        self.txt_mix_burger = Entry(font=("times new roman", 12), bg='grey')
        self.txt_mix_burger.place(x=500, y=600, width=40)

        #newari khajaset
        # Newari cuisine
        newari = Label(text='Newari Cuisine', font=("times new roman", 18, 'bold'), bg='black',
                       fg='grey').place(x=730, y=205)
        #khajaset

        newari_khajaset = Label(text='Khaja Set ---------------------------------', font=("times new roman", 12, 'bold'),
                         bg='black',
                         fg='grey').place(x=730, y=230)
        nkhaja_price = Label(text='350', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=960, y=230)
        self.txt_newari_khaja = Entry(font=("times new roman", 12), bg='grey')
        self.txt_newari_khaja.place(x=1000, y=230, width=40)

        #yomari
        yomari = Label(text='Yomari ------------------------------------',
                                font=("times new roman", 12, 'bold'),
                                bg='black',
                                fg='grey').place(x=730, y=250)
        yomari_price = Label(text='100', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=960, y=250)
        self.txt_yomari = Entry(font=("times new roman", 12), bg='grey')
        self.txt_yomari.place(x=1000, y=250, width=40)

        #choila
        choila= Label(text='Choila ------------------------------------',
                       font=("times new roman", 12, 'bold'),
                       bg='black',
                       fg='grey').place(x=730, y=270)
        choila_price = Label(text='200', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=960, y=270)
        self.txt_choila = Entry(font=("times new roman", 12), bg='grey')
        self.txt_choila.place(x=1000, y=270, width=40)

        #thakali set
        thakali_set = Label(text='Thakali Set', font=("times new roman", 18, 'bold'), bg='black',
                       fg='grey').place(x=730, y=330)

        Thakali_set = Label(text='Thakali Set ---------------------------------',
                       font=("times new roman", 12, 'bold'),
                       bg='black',
                       fg='grey').place(x=730, y=360)
        Thakali_set_price = Label(text='500', font=("times new roman", 12, 'bold'), bg='black',
                             fg='grey').place(x=960, y=360)
        self.txt_Thakali_set= Entry(font=("times new roman", 12), bg='grey')
        self.txt_Thakali_set.place(x=1000, y=360, width=40)

        #sekuwa
        sekuwa = Label(text='Sekuwa', font=("times new roman", 18, 'bold'), bg='black',
                            fg='grey').place(x=730, y=450)

        chicken_sekuwa = Label(text='Chicken Sekuwa -----------------------',
                            font=("times new roman", 12, 'bold'),
                            bg='black',
                            fg='grey').place(x=730, y=480)
        csekuwa_price = Label(text='600', font=("times new roman", 12, 'bold'), bg='black',
                                  fg='grey').place(x=960, y=480)
        self.txt_chicken_sekuwa = Entry(font=("times new roman", 12), bg='grey')
        self.txt_chicken_sekuwa.place(x=1000, y=480, width=40)

        pork_sekuwa = Label(text='Pork Sekuwa --------------------------',
                               font=("times new roman", 12, 'bold'),
                               bg='black',
                               fg='grey').place(x=730, y=500)
        psekuwa_price = Label(text='530', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=960, y=500)
        self.txt_pork_sekuwa = Entry(font=("times new roman", 12), bg='grey')
        self.txt_pork_sekuwa.place(x=1000, y=500, width=40)

        buff_sekuwa = Label(text='Pork Sekuwa --------------------------',
                            font=("times new roman", 12, 'bold'),
                            bg='black',
                            fg='grey').place(x=730, y=520)
        bsekuwa_price = Label(text='560', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=960, y=520)
        self.txt_buff_sekuwa = Entry(font=("times new roman", 12), bg='grey')
        self.txt_buff_sekuwa.place(x=1000, y=520, width=40)

        soft_drink = Label(text='Soft Drink', font=("times new roman", 18, 'bold'), bg='black',
                       fg='grey').place(x=730, y=565)

        coke = Label(text='Coke------------------------------------------',
                            font=("times new roman", 12, 'bold'),
                            bg='black',
                            fg='grey').place(x=730, y=590)
        coke_price = Label(text='100', font=("times new roman", 12, 'bold'), bg='black',
                              fg='grey').place(x=960, y=590)
        self.txt_coke = Entry(font=("times new roman", 12), bg='grey')
        self.txt_coke.place(x=1000, y=590, width=40)

        dew = Label(text='Mountain Dew--------------------------',
                     font=("times new roman", 12, 'bold'),
                     bg='black',
                     fg='grey').place(x=730, y=610)
        Mdew_price = Label(text='100', font=("times new roman", 12, 'bold'), bg='black',
                           fg='grey').place(x=960, y=610)
        self.txt_dew = Entry(font=("times new roman", 12), bg='grey')
        self.txt_dew.place(x=1000, y=610, width=40)

        fanta = Label(text='Fanta---------------------------------------',
                    font=("times new roman", 12, 'bold'),
                    bg='black',
                    fg='grey').place(x=730, y=630)
        fanta_price = Label(text='100', font=("times new roman", 12, 'bold'), bg='black',
                           fg='grey').place(x=960, y=630)
        self.txt_fanta = Entry(font=("times new roman", 12), bg='grey')
        self.txt_fanta.place(x=1000, y=630, width=40)

        self.root.mainloop()


run()