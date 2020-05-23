import pygame
import numpy as np
from scipy.integrate import odeint
import time
import  pendulo_datos
altura_de_pantalla=600
ancho_de_pantalla=600
#colores
RF=131, 33, 97
MORA=61, 38, 69
SR=218, 65, 103
BLANCO=240, 239, 244
#intialize the pygame
pygame.init()
#creat the screen 
screen = pygame.display.set_mode((altura_de_pantalla,ancho_de_pantalla))
#title an icon
pygame.display.set_caption("Modelado y Simulacion ")
icon =pygame.image.load('img/upiita.jpg')
pygame.display.set_icon(icon)
#Bola
bolaImg=pygame.image.load('img/sport _1.png')
#pantalla
font =pygame.font.Font('font/Mate-Italic.ttf',32)

def show(x,y,velocidad,Magnitud):
    score = font.render( str(Magnitud)+":" +str(velocidad),True,MORA)
    screen.blit(score,(x,y))
def bola(x,y):
    cy=altura_de_pantalla/2
    cx=ancho_de_pantalla/2
    bolaX=x + cy
    bolaY=y + cx
    screen.blit(bolaImg,(bolaX,bolaY))
def linea(x,y):
    cy = (altura_de_pantalla/2)
    cx = (ancho_de_pantalla/2)
    lineaX=x+cy
    lineaY=y+cx
    pygame.draw.line(screen, BLANCO, [cy, cx], [lineaX, lineaY], 3)
anguloGra,velocidad,Xm,Ym,t = pendulo_datos.pendulosimple()
#Game Loop
i=0
running =True
while running:
    screen.fill((RF))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False 
    bola(Xm[i],Ym[i])
    linea(Xm[i],Ym[i])
    show(10,10,anguloGra[i],'Angulo')
    show(10,110,velocidad[i],'Velocidad')
    show(10,210,np.around(t[i],decimals=1),'tiempo')
    pygame.display.update()
    if i==(len(Xm)-1):
        i=0
    i=i+1
    #print(i)
    pygame.time.wait(25)
    timer_resolution = pygame.TIMER_RESOLUTION
    print (timer_resolution+25)