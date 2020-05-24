import pygame
import numpy as np
from scipy.integrate import odeint
import time
from ecuaciones import  pendulo_datos, resorte , atwood,pen_doble,pendulo_doble,pendulo_inv_carp

altura_de_pantalla=600
ancho_de_pantalla=600

#colores
RF=131, 33, 97
MORA=61, 38, 69
SR=218, 65, 103
BLANCO=240, 254, 254
AZUL=18,10,143
BLACK=0,0,0
#fondo Resbaloso
fondoM=pygame.image.load('img/fondoResbaloso.png')
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
rayo=pygame.image.load('img/rayom.png')
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
    bolaX=int(x + cy)
    bolaY=int(y + cx)
    if b==0:
        pantalla.blit(bolaImg,(bolaX,bolaY))
    if b==1:
        pantalla.blit(bolaImg2,(bolaX,bolaY))
def linea(x,y):
    cy = (altura_de_pantalla/2)
    cx = (ancho_de_pantalla/2)
    lineaX=x+cy
    lineaY=y+cx
    pygame.draw.line(pantalla, AZUL, [cy, cx], [lineaX, lineaY], 4)
def linea_dos_p(xi,yi,xf,yf):
    cy = (altura_de_pantalla/2)
    cx = (ancho_de_pantalla/2)
    xi=xi+cy
    yi=yi+cx
    xf=xf+cy
    yf=yf+cx
    pygame.draw.line(pantalla, BLACK, [xi,yi], [xf, yf], 4)  

def linea_dos_pf(xi,yi,xf,yf):
    cy = (altura_de_pantalla/2)
    cx = (ancho_de_pantalla/2)
    xi=xi+cy
    yi=yi+cx
    xf=xf+cy
    yf=yf+cx
    pygame.draw.line(pantalla, BLACK, [xi,yi], [xf, yf], 4)  

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
    pygame.draw.line(pantalla, MORA, [cy, cx], [lineaX, lineaY], 4)

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
    elif opcion==3:
        anguloGra,velocidad,Xm,Ym,X2,Y2,t =pendulo_doble.penduloDoble() #pen_doble.pd()
        ele=4*100
    elif opcion==4:
        x,v,tetha,w,Pmx,Pmy,PMx,PMy,t =pendulo_inv_carp.pendulocarp()     #pen_doble.pd()
        Xm=x
    
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

        elif opcion==3:
            
            pantalla.fill((RF))
            bola(Xm[i]-5,Ym[i],0)
            linea(Xm[i],Ym[i])
            bola(X2[i],Y2[i],1)
            linea_dos_p(Xm[i],Ym[i],X2[i],Y2[i])
            #linea(Xm[i],Ym[i])
            show(10,10,anguloGra[i],'Angulo UNO')
            show(10,110,velocidad[i],'Velocidad UNO')
            show(230,500,np.around(t[i],decimals=1),'tiempo')
            show(350,10,anguloGra[i],'Angulo DOS')
            show(350,110,velocidad[i],'Velocidad DOS')
        
        elif opcion==4:
            #x,v,tetha,w,Pmx,Pmy,PMx,PMy,t
            pantalla.fill((255,255,255))
            pantalla.blit(fondoM,[0,0])
            pantalla.blit(rayo, [ -PMx[i] +(ancho_de_pantalla/2) -170, -PMy[i] + (altura_de_pantalla/2)-50])
            #pantalla.blit(polea,[-PMx[i] +(ancho_de_pantalla/2) , -PMy[i] + (altura_de_pantalla/2)+25])
            #pantalla.blit(fondoM,[0,0])
            bola(-Pmx[i],-Pmy[i],0)
            linea_dos_p(-Pmx[i],-Pmy[i], -PMx[i] ,-PMy[i] )
            #linea(Xm[i],Ym[i])
            #bola(PMx[i],PMy[i],1)
            
            #pantalla.blit(rayo, [ -PMx[i] +(ancho_de_pantalla/2) , -PMy[i] + (altura_de_pantalla/2)-50])
            
            #linea_dos_p(Xm[i],Ym[i],X2[i],Y2[i])
            show(10,400,np.around(Pmx[i],decimals=1),'Bola en X')
            show(10,450,np.around(Pmy[i],decimals=1),'Bola en Y')
            show(10,500,np.around(PMy[i],decimals=1),'Auto en X')
            show(530,530,np.around(t[i],decimals=1),'t')
            show(10,550,np.around(v[i],decimals=1),'Velocidad auto')
            #show(350,110,velocidad[i],'Velocidad DOS')
            


        pygame.display.update()
        if i==(len(Xm)-1):
            i=0
        i=i+1
        #print(i)
        pygame.time.wait(100)
        #timer_resolution = pygame.TIMER_RESOLUTION
        #print (timer_resolution+25)
