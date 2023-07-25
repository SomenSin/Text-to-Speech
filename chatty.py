from tkinter.ttk import Progressbar
from gtts import gTTS
import time
import os
from tkinter import *
root = Tk()
root.configure(bg="cyan")
root.geometry("500x500")
root.resizable(0,0)
Progress_Bar=Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
root.title("Chatty")
def Take_input():
    """ This function gets the statement from the text box, converts it to speech using Google TTS,
    saves the speech as an MP3 file, and plays the MP3 file back using the OS command.  """
    INPUT = inputtxt.get("1.0", "end-1c")
    language = 'hi'
    myobj=gTTS(text=INPUT, lang=language)
    myobj.save("C:\Clip\play.mp3")
    Progress_Bar['value']=10
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=20
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=30
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=40
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=50
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=60
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=70
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=80        
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=90
    root.update_idletasks()
    time.sleep(0.5)
    Progress_Bar['value']=100        
    root.update_idletasks()
    time.sleep(0.5)
    os.system("C:\Clip\play.mp3")
l=Label(text = "Enter the Statement",fg="silver",bg="blue",font=('Times', 25))
inputtxt = Text(root,height=14.49,width=40,bg="orange",fg="black",font=('Times',15))
Display=Button(root, height = 4,width = 15,text ="send" ,command = lambda:Take_input())
l.place(x=130,y=9)
Display.place(x=190,y=420)
inputtxt.place(x=50,y=60)
Progress_Bar.place(x=100,y=382)
mainloop()
