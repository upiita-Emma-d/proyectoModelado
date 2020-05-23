import pygame
import numpy as np
from scipy.integrate import odeint
import time
from ecuaciones import  pendulo_datos, resorte , atwood

altura_de_pantalla=600
ancho_de_pantalla=600
#colores
RF=131, 33, 97
MORA=61, 38, 69
SR=218, 65, 103
BLANCO=240, 254, 254
AZUL=18,10,143
#intialize the pygame
pygame.init()
#creat the pantalla 
pantalla = pygame.display.set_mode((altura_de_pantalla,ancho_de_pantalla))
#title an icon
pygame.display.set_caption("Modelado y Simulacion ")
icon =pygame.image.load('img/upiita.jpg')
pygame.display.set_icon(icon)
#Bola
bolaImg=pygame.image.load('img/sport _1.png')
bolaImg2=pygame.image.load('img/soccer-ball.png')
#polea
polea=pygame.image.load('img/polea.png')
#Disco M R
disco=pygame.image.load('img/disco_150.jpg')
riel=pygame.image.load('img/riel.png')
res=pygame.image.load('img/r.jpg')
#pantalla
font =pygame.font.Font('font/Mate-Italic.ttf',32)
#awwood
atw=False

def show(x,y,velocidad,Magnitud):
    score = font.render( str(Magnitud)+":" +str(velocidad),True,MORA)
    pantalla.blit(score,(x,y))
def bola(x,y,b):
    cy=altura_de_pantalla/2
    cx=ancho_de_pantalla/2
    bolaX=x + cy
    bolaY=y + cx
    if b==0:
        pantalla.blit(bolaImg,(bolaX,bolaY))
    if b==1:
        pantalla.blit(bolaImg2,(bolaX,bolaY))
def linea(x,y):
    cy = (altura_de_pantalla/2)
    cx = (ancho_de_pantalla/2)
    lineaX=x+cy
    lineaY=y+cx
    pygame.draw.line(pantalla, AZUL, [cy, cx], [lineaX, lineaY], 3)
def bolaa(x,y,b):
    cx=50
    cy=ancho_de_pantalla/2
    bolaX=x + cy
    bolaY=y + cx
    if b==0:
        pantalla.blit(bolaImg,(bolaX,bolaY))
    if b==1:
        pantalla.blit(bolaImg2,(bolaX,bolaY))

def lineaa(x,y):
    cx = (50)
    cy = (ancho_de_pantalla/2)
    lineaX=x+cy
    lineaY=y+cx
    pygame.draw.line(pantalla, MORA, [cy, cx], [lineaX, lineaY], 3)

def animaciones(opcion):
    print(opcion)
    atw=False
    if opcion==0:
        anguloGra,velocidad,Xm,Ym,t = pendulo_datos.pendulosimple()
    elif opcion==1:
        anguloGra,velocidad,Xm,Ym,t = resorte.resorte()
    elif opcion==2:
        anguloGra,velocidad,Xm,Ym,t,atw= atwood.atwood()
        ele=4*100

    
    i=0
    running =True
    while running:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False 
        if opcion==0:
            pantalla.fill((RF))
            bola(Xm[i],Ym[i],0)
            linea(Xm[i],Ym[i])
            show(10,10,anguloGra[i],'Angulo')
            show(10,110,velocidad[i],'Velocidad')
            show(10,210,np.around(t[i],decimals=1),'tiempo')
        elif opcion==1:
            pantalla.fill((BLANCO))
            show(10,10,anguloGra[i],'Posicion X')
            show(10,110,velocidad[i],'Velocidad')
            show(10,210,np.around(t[i],decimals=1),'tiempo')
            pantalla.blit(riel, [42,100])
            pantalla.blit(disco, [Xm[i]+(ancho_de_pantalla/2) , Ym[i] + (altura_de_pantalla/2)-50])
            dif=int(Xm[i])
            resort = pygame.transform.scale(res, (dif ,60) )
            pantalla.blit(resort, [ancho_de_pantalla/2 , altura_de_pantalla/2 - 40])
   
        elif opcion==2:
            
            pantalla.fill((BLANCO))
            pantalla.blit(polea,[(ancho_de_pantalla/2)-30,50])
            ele=4*100
            dos=200
            bolaa(Xm[i]+15,Ym[i],0)
            lineaa(Xm[i]+20,Ym[i])
            bolaa( Xm[i]-30 ,ele-Ym[i],1)
            lineaa(Xm[i]-20,ele-Ym[i])
            
            show(10,10,np.around(anguloGra[i],decimals=1),'Posicion Y')
            show(10,110,np.around(velocidad[i],decimals=2),'Velocidad')
            show(10,210,np.around(t[i],decimals=1),'tiempo')
            if Ym[i]<=0:
                i=0
        pygame.display.update()
        if i==(len(Xm)-1):
            i=0
        i=i+1
        #print(i)
        pygame.time.wait(25)
        #timer_resolution = pygame.TIMER_RESOLUTION
        #print (timer_resolution+25)

