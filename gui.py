from tkinter import *
from PIL import Image,ImageTk
import speech_to_text
import text_to_speech
import action
import pyttsx3
import datetime
root=Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="pink")

#ask 
def ask():
    ask_data=speech_to_text.speech_to_text()
    if(ask_data==None):
        text.insert(END, "Assistant <----"+"Sorry Unable to catch it, Please ask again\n")
    else:
        assis_data =action.Action(ask_data)
        text.insert(END, "User ----> "+ask_data+"\n")
        if assis_data !=None:
            text.insert(END, "Assistant <----"+str(assis_data)+"\n")
        if assis_data =="Shutting down...":
            root.destroy()
def send():
    send=entry.get()
    assist=action.Action(send)
    text.insert(END, "User ----> "+send+"\n")
    if assist !=None:
        text.insert(END, "Assistant <----"+str(assist)+"\n")
    if assist =="Shutting down...":
        root.destroy()
    if assist=="Yes,I'm Quitting Now":
        text.insert(END, "Assistant <----"+"Yes,I'm Quitting Now!!!Thank You,Mam"+"\n")
        text_to_speech.text_to_speech("Yes,I'm Quitting Now!!!Thank You,Mam")
        exit()
def dele():
    text.delete("1.0" , "end")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!Bhargavi")
    elif hour>=12 and hour<18:
        speak("Good Afternoon,Bhargavi")
    else:
        speak("Good evening,Bhargavi")
    speak("Iam a Desktop Assistant,tell me how can i help you?")
frame=LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
frame.config(bg="pink")
frame.grid(row=0,column=1,padx=55,pady=10)
text_label=Label(frame,text="Desktop Assistant",font=('comic Sans ms',14,"bold"),bg='white')
text_label.grid(row=0,column=0,padx=20,pady=10)
#image label
image=ImageTk.PhotoImage(Image.open("C:/Users/Bhargavi Nagulapally/Downloads/Programs/py/Virtual_Assistant/ai.png"))
image_label=Label(frame,image=image )
image_label.grid(row=1,column=0,pady=20)
text= Text(root,font=('courier 10 bold'),bg="skyblue")
text.grid(row=2,column=0)
text.place(x=95,y=425,width=375 ,height=100)
#entry
entry=Entry(root,justify=CENTER)
entry.place(x=95,y=530,width=375,height=30)
#button
Button1=Button(root,text='ASK',bg="white",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=575)
Button2=Button(root,text='Send',bg="white",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=400,y=575)
Button3=Button(root,text='Delete',bg="white",pady=16,padx=40,borderwidth=3,relief=SOLID,command=dele)
Button3.place(x=225,y=575)
wishMe()
root.mainloop()
