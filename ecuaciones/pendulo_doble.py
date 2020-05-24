import numpy as np
from scipy.integrate import  odeint
import matplotlib.pyplot as plt

l1=1
l2=1 
m1=1
m2=1
g=9.81
def penduloDoble():

    def fun(iniciales,t):
   
        #iniciales=[1,0,1,0]
        tetha1=iniciales[0]
        w1=iniciales[1]
        tetha2=iniciales[2]
        w2=iniciales[3]
        dA=tetha1-tetha2
        #data = np.array([[1, 2], [3, 4]])
        D = np.array( [[ (m1+m2) * l1**2 , m2*l1*l2*np.cos(dA) ] , [m2 * l1 * l2 * np.cos(dA) , m2*l2*l2 ]])
        C=np.array([[ m2 * l1 * l2 * np.sin(dA) * (w2 * w2) ],[-m2 * l1 * l2 * np.sin(dA) * (w1**2)]])
        G=np.array( [ [ (m1+m2) * g * l1 * np.sin(tetha1)] , [m2 * g * l2 * np.sin(tetha2) ] ] )
        T=np.array([[0],[0]]) 
        
        aceleraciones=-(np.linalg.inv(D)) @ C - (np.linalg.inv(D)) @ G #+ (np.linalg.inv(D)) @ T
        #pru= (np.linalg.inv(D)) 
        aceleraciones = np.array(aceleraciones, dtype=float)
        derivadas=(w1,aceleraciones[0],w2,aceleraciones[1])
        
        return derivadas

    tetha1 = 120.0
    w1 = 0.0
    tetha2 = -10.0
    w2 = 0.0

    #estados iniciales
    iniciales = np.radians([tetha1, w1, tetha2, w2])

    dt = 0.025
    t = np.arange(0, 20, dt)
    sol = odeint(fun, iniciales, t )
    #fun(iniciales,t,L1,L2)

    #print(sol)

    #sol = odeint(fun, iniciales, t ,args=(L1,L2))
     #cachando las soluciones
    angulo1=sol[:,0]
    velocidad1=sol[:,1]
    angulo2=sol[:,2]
    velocidad2=sol[:,3]
    ####################
    X1=l1*100*np.sin(angulo1)
    Y1=l1*100*np.cos(angulo1)
    X2=l1*100*np.sin(angulo1)+l2*100*np.sin(angulo2)
    Y2=l1*100*np.cos(angulo1)+l2*100*np.cos(angulo2)
    anguloGra1=np.degrees(angulo1)
    anguloGra1=np.around(anguloGra1,decimals=1)
    velocidad1=np.around(velocidad1,decimals=1)
    return anguloGra1,velocidad1,X1,Y1,X2,Y2,t  


#penduloDoble()






