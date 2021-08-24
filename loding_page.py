from time import sleep
from tkinter import *
from PIL import ImageTk, Image
import time
import threading
from playsound import playsound
import login_page
class Loading:
    def __init__(self):
        self.root=Tk()
        self.root.config(bg="black")
        self.root.state('zoomed')
        self.root.update()
        self.play_animation()
        self.root.mainloop()
    def play_animation(self):
        for i in range(1):
            for j in range(1, 27):
                loading = ImageTk.PhotoImage(Image.open(f'loading_img/{j}.jpg'))
                loading_img = Label(self.root, image=loading).place(x=45, y=25)
                sleep(0.14)
                self.root.update_idletasks()
        else:
            self.root.destroy()
            login_page.Login(Tk())

def startmusic():
    time.sleep(0.5)
    playsound('coffee1.mp3')
def startthreads():
    thread1=threading.Thread(target=startmusic)
    thread1.start()
startthreads()
Loading()
