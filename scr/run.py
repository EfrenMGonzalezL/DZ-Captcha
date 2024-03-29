#!/usr/bin/env python
# coding: utf-8

# # Creacion de Captcha para imagenes
# 
# 
# ##  Programa obtiene un arreglo de imagenes guardadas en una capeta, y escribe en ellas el codigo generado por el programa de generacion de Captcha
# ### Codigo creado por  Efren Mario Gonzalez Lopez 17/07/2019
# #### Github: https://github.com/DarknessZ3R0/Captcha_Create
# version: 5.0 
# release date: 21/08/2019
from tkinter import *
from tkinter import filedialog
from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import random
import cv2
import glob
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import *
import os


font_path = "..\\fonts\Minecrafter_Reg.ttf"

number_list = ['0','1','2','3','4','5','6','7','8','9']

#alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def create_random_captcha_text(captcha_string_size=4):

    captcha_string_list = []
    base_char =  alphabet_uppercase + number_list
    #base_char = alphabet_lowercase + alphabet_uppercase + number_list

    for i in range(captcha_string_size):

       
        char = random.choice(base_char)

       
        captcha_string_list.append(char)

    captcha_string = ''

    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

#Inicio, creacion de captcha y creacion de la imagen con captcha y guardado con su nombre
def img_captcha_creation(img_path,destiny_path):
  
    TEXT_COLOR =(255,255,255)#(238,238,238) #Color
    SHADOW_COLOR=(238,238,238)#(195,38,226) #Sombra
    SHADOW_FONT_COLOR=(0,0,0) #Negro
    X_data = []
    
    files=glob.glob(img_path) #solo funciona con jpg,"Probar con PNG y JPEG"
    print("Path de imagenes:",files)
    for myFile in files:
       
         # Crear Captcha 
        captcha_text = create_random_captcha_text()
        print("Captcha Original:")
        print(captcha_text) #visualizacion del captcha

        #reacomodo del captcha para la imagen
        i=0
        j=0
        img_captcha=''
        for i in range(len(captcha_text)):
            temp=captcha_text[i]
            img_captcha+=str(temp)
            j=j+1
            img_captcha+=str(' ')#Espacio
            j=j+1
        #fin del acomodo, y se guarda en otra variable para poder ser usada despues
        print("Captcha Reacomodado:")
        print(img_captcha)#visualizacion del captcha reacomodado
        #Selecion de tipo de letra, si quieres una en especial, descargar el TTF o OTF y modificar la ultima parte
        print("Localizacion de la imagen")
        print(myFile) #Localiza la imagen en una carpeta
        image = cv2.imread (myFile)  
        img = Image.open(myFile)
        img =img.resize((1500,500))
        draw = ImageDraw.Draw(img)
        #draw2 = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(font_path,250)
        width, height = img.size 
         #Posiciones, "texto a dibujar en la imagen" ,Tipo de letra,color
        x=width/7
        y=height/3
        tam=10
        #thin border
        draw.text((x-tam,y), img_captcha,font=fnt,fill=(SHADOW_FONT_COLOR))
        draw.text((x+tam,y), img_captcha,font=fnt,fill=(SHADOW_FONT_COLOR))
        draw.text((x,y-tam), img_captcha,font=fnt,fill=(SHADOW_FONT_COLOR))
        draw.text((x,y+tam), img_captcha,font=fnt,fill=(SHADOW_FONT_COLOR))
        ##thicker border
        draw.text((x-tam,y-tam), img_captcha,font=fnt,fill=(SHADOW_FONT_COLOR))
        draw.text((x+tam,y-tam), img_captcha,font=fnt,fill=(SHADOW_FONT_COLOR))
        draw.text((x-tam,y+tam), img_captcha,font=fnt,fill=(SHADOW_FONT_COLOR))
        draw.text((x+tam,y+tam), img_captcha,font=fnt,fill=(SHADOW_FONT_COLOR))
        
        draw.text((x,y), img_captcha,font=fnt,fill=(TEXT_COLOR))#Color base
        img.save(destiny_path+captcha_text + '.png') #Guarda el archivo generado con el nombre del captcha generado original

    


    # In[ ]:
    print("\n------------------------- Todo salio perfecto!! -------------------------------")
    
#folder_image_path=""
#folder_output_path=""
def crearCaptcha():
    global image_path 
    global destiny_path
    global done
    image_path=folder_image_path+"/*.png"
    destiny_path=folder_output_path+"/"
    print(image_path)
    img_captcha_creation(image_path,destiny_path)
    done.set("------------------TODO SALIO PERFECTO----------------------")
    

def browse_button_input():
    global folder_image_path
    global path_1
    filename = filedialog.askdirectory()
    folder_image_path=filename
    path_1.set(filename)
    

def browse_button_output():
    global folder_output_path
    global path_2
    filename = filedialog.askdirectory()
    folder_output_path=filename
    path_2.set(filename)
    

window =Tk()
window.title("Captcha Create")
window.geometry("300x400")
window.configure(background='grey25')
path_1= StringVar()
path_2= StringVar()
done = StringVar()
path_1.set("____________________________")
path_2.set("Default : ..\img_output/    ")
done.set("---------------------------------------------------------------------")
folder_image_path= ""
folder_output_path= "..\img_output/"



b1=Button(window,text="Buscar Folder",command=browse_button_input)
b1.place(x=5,y=100)
lbl=Label(master=window,textvariable=path_1)
lbl.place(x=0,y=130)

b2=Button(window,text="Folder donde guardar",command=browse_button_output)
b2.place(x=5,y=160)
lbl2=Label(master=window,textvariable=path_2)
lbl2.place(x=0,y=190)


b3=Button(window,text="Crear Captcha",command = crearCaptcha)
b3.place(x=5,y=220)
lbl3=Label(master=window,textvariable=done)
lbl3.place(x=0,y=260)
window.mainloop()
