import joblib
import pandas as pd
import cloudpickle as cp
import pickle
import sklearn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.simplefilter("ignore")
import os
import requests
import shutil
import urllib.request
l=['DTC.sav','gauusianb.sav','k-neigh.pkl','logistic.sav','random.sav','svc.sav']
for i in l:
    if not os.path.exists(i):
        url="https://github.com/ChandraKarthik07/Diabetes-prediction-with-custom-tkinter/blob/main/sav/{}?raw=true".format(i)
        filename, headers = urllib.request.urlretrieve(url, filename="./{}".format(i))
    print ("exists!")

DTC_model = joblib.load('DTC.sav')
gauusuianb_model = joblib.load('gauusianb.sav')
logistic_model = joblib.load('logistic.sav')
random_model = joblib.load('random.sav')
#with open('k-neigh.pkl' , 'rb') as f:
    #k_neigh = cp.load(f)
svc_model = joblib.load('svc.sav')
from tkinter import *
import tkinter.messagebox
import customtkinter
import sys
from PIL import Image, ImageTk# <- import PIL for the images
from tkinter.ttk import *
from urllib.request import urlopen
#from .customtkinter_theme_manager import CTkThemeManager
import numpy as np


customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("blue")# Themes: "blue" (standard), "green", "dark-blue"

top=customtkinter.CTk()


top.geometry("720x720")
top.title("Diabetes prediction")
 
def change_mode():
        if check_box_2.get() == 0:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

check_box_2 = customtkinter.CTkCheckBox(master=top,text="Toggle",command=change_mode)
check_box_2.grid(row=7, column=0, pady=10, padx=20, sticky="w")
URL = "https://raw.githubusercontent.com/ChandraKarthik07/Diabetes-prediction-with-custom-tkinter/main/accuracy.png"
URL1 = "https://raw.githubusercontent.com/ChandraKarthik07/Diabetes-prediction-with-custom-tkinter/main/clipart.png"
URL2="https://raw.githubusercontent.com/ChandraKarthik07/Diabetes-prediction-with-custom-tkinter/main/cr.jpg"
u = urlopen(URL)
raw_data = u.read()
u.close()
v = urlopen(URL1)
raw__data = v.read()
v.close()
w = urlopen(URL2)
raw___data = w.read()
w.close()
bg_image = ImageTk.PhotoImage(data=raw_data) # <-----
bg_image1= ImageTk.PhotoImage(data=raw__data)
bg_image3=ImageTk.PhotoImage(data=raw___data)
def do_something():
    tkinter.messagebox.showinfo("ERROR"," 0 levels that means you are not alive anymore " u" \u2620 " u" \u2620...")
def button1():
    top1=customtkinter.CTkToplevel()
    customtkinter.set_appearance_mode("dark")
    top1.geometry("1600x1080")
    top1.title("Diabetes report")
    X1=float(entry.get())
    Y1=float(entry1.get())
    ha=np.array([[X1,Y1]])
    pred1=DTC_model.predict(ha)
    pred2=gauusuianb_model.predict(ha)
    pred3=logistic_model.predict(ha)
    #pred4=k_neigh.predict(ha)
    pred5=svc_model.predict(ha)
    pred6=random_model.predict(ha)


    k1="👉According to the deccision tree classifier algorithm ,you have a chance of being {pro} ".format( pro="diabetic" if int(pred1)==2 else "prediabetic" if int(pred1)==1 else "normal")
    k2="👉According to the gaussain nb algorithm ,you have a chance of being {pro} ".format( pro="diabetic" if int(pred2)==2 else "prediabetic" if int(pred2)==1 else "normal")
    k3="👉According to the logistic classification algorithm ,you have a chance of being {pro} ".format( pro="diabetic" if int(pred3)==2 else "prediabetic" if int(pred3)==1 else "normal")
    #k4="👉According to the k-neighbors algorithm ,you have a chance of being {pro} ".format( pro="diabetic" if int(pred4)==2 else "prediabetic" if int(pred4)==1 else "normal")
    k5="👉According to the svm ,you have a chance of being {pro} ".format( pro="diabetic" if int(pred5)==2 else "prediabetic" if int(pred5)==1 else "normal")
    k6="👉According to the random tree classifier algorithm ,you have a chance of being {pro} ".format( pro="diabetic" if int(pred6)==2 else "prediabetic" if int(pred6)==1 else "normal")
    
        
    def change_mode1():
        if check_box_1.get() == 0:
            customtkinter.set_appearance_mode("light")
            
            
        else:
            customtkinter.set_appearance_mode("dark")
            
    image_label1 = tkinter.Label(master=top1, image=bg_image)
    image_label1.image=bg_image
    image_label1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    image_label3 = customtkinter.CTkLabel(master=top1,text="{}\n\n{}\n\n{}\n\n{}".format(k1,k2,k3,k5),width=550,height=250,corner_radius=8)
    image_label3.place(relx=0.6, rely=0.2, anchor=tkinter.CENTER)
    plot= tkinter.Label(master=top1, image=bg_image3)
    plot.image=bg_image3
    plot.place(relx=0.6, rely=0.7, anchor=tkinter.CENTER)
       
    check_box_1 = customtkinter.CTkCheckBox(master=top1,text="T",command=change_mode1)
    check_box_1.grid(row=7, column=5, pady=10, padx=20, sticky="w")
    #rep1="acording to the k-neighbours algoritm ,you are "
    
    
def button():
    if entry.get()==str(0) or entry1.get() == str(0):
        do_something()
    elif  len(entry.get())==0:
        tkinter.messagebox.showinfo("ERROR","PLEASE ENTER THE VALUES "u"\U0001F643 "u"\U0001F643")

    else:
        X1=float(entry.get())
        Y1=float(entry1.get())
        ha=np.array([[X1,Y1]])
        pred1=DTC_model.predict(ha)
        pred2=gauusuianb_model.predict(ha)
        pred3=logistic_model.predict(ha)
        #pred4=k_neigh.predict(ha)
        pred5=svc_model.predict(ha)
        pred6=random_model.predict(ha)
        l=[pred1,pred2]
        A=np.array([int(pred1),int(pred2),int(pred3),int(pred5)])
        C=A[A!=0]
        res=(len(C)/4)*100

        print("results",entry.get(),entry1.get())
        if res<=45:
            color="#5EA880"
        elif(45<res<=75):
            color="#FF7F50"
        else:
            color="#FF0000"
            
        outputLabel=customtkinter.CTkLabel(master=top,text="you have {} percent of chance of being diabetic".format(res),width=350,height=30,corner_radius=10,fg_color=("white", "gray20"),text_color=color)
        outputLabel.place(relx=0.5, rely=0.65,anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=top,width=320,height=720,corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

frame1 = customtkinter.CTkFrame(master=top,width=1080,height=300,corner_radius=10)
frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=top,text="1.GLUCOSE",width=100,height=25,corner_radius=5)

label.place(relx=0.35, rely=0.34, anchor=tkinter.CENTER)
entry = customtkinter.CTkEntry(master=top,placeholder_text="Let me know your glucose values",width=250,height=25,corner_radius=10)
entry.place(relx=0.45, rely=0.39, anchor=tkinter.CENTER)
text1 = entry.get()


label1 = customtkinter.CTkLabel(master=top,text="2.INSULIN",width=100,height=25,corner_radius=5)

label1.place(relx=0.35, rely=0.48, anchor=tkinter.CENTER)
entry1 = customtkinter.CTkEntry(master=top,placeholder_text="Let me know your insulin values",width=250,height=25,corner_radius=10)
entry1.place(relx=0.45, rely=0.53, anchor=tkinter.CENTER)
text2 = entry1.get()
button=customtkinter.CTkButton(top,text="CHECK",image=bg_image1,compound=("right"),command=button,fg_color=( "lightgray","gray"),hover_color= "#458577",border_width=2,corner_radius=6)
button.place(relx=0.5, rely=0.75,anchor=tkinter.CENTER)

button1=customtkinter.CTkButton(top,text="👇Click me for more details of 👇\n ml models/report",hover_color= "#458577",command=button1,border_width=2,corner_radius=5)
button1.place(relx=0.5, rely=0.85,anchor=tkinter.CENTER)
progressbar = customtkinter.CTkProgressBar(master=top,width=160,height=20,border_width=5)
progressbar.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
progressbar.set(True)


top.mainloop()
