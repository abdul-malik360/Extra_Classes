import multiprocessing
from playsound import playsound
from tkinter import *

window = Tk()
window.title("Play Sound")
window.geometry("300x200")

p = multiprocessing.Process(target=playsound, args=(""))



def play_sound():
    p.start()


def stop_sound():
    p.terminate()
    window.destroy()


play_btn = Button(window, text="PLAY", command=play_sound)
play_btn.place(x=20, y=50)

stop_btn = Button(window, text="STOP", command=stop_sound)
stop_btn.place(x=20, y=100)

window.mainloop()
