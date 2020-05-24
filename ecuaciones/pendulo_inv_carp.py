import numpy as np
from scipy.integrate import  odeint
import matplotlib.pyplot as plt

l=1 
M=1
m=1
g=9.81
def pendulocarp():

    def fun(iniciales,t):
   
        #iniciales=[1,0,1,0]
        x=iniciales[0]
        xdot=iniciales[1]
        tetha=iniciales[2]
        w=iniciales[3]
        
        #data = np.array([[1, 2], [3, 4]])
        D = np.array( [ [ (M+m) , -m * l * np.cos(tetha) ] , [ - np.cos(tetha) , l ] ])
        C=np.array( [ [ m * l * (w**2) * np.sin(tetha) ] , [ 0 ] ] )
        G=np.array( [ [ 0 ] , [ -g*np.sin(tetha) ] ] )
        T=np.array([[0],[0]]) 
        
        aceleraciones=-(np.linalg.inv(D)) @ C - (np.linalg.inv(D)) @ G #+ (np.linalg.inv(D)) @ T
        pru= (np.linalg.inv(D)) 
        aceleraciones = np.array(aceleraciones, dtype=float)
        derivadas=(xdot,aceleraciones[0],w,aceleraciones[1])
        
        return derivadas

    x = 0
    xdot = 0.0
    tetha = 45
    w = 0.0

    #estados iniciales
    iniciales = np.radians([ 0 , 0 , tetha , 0 ])
    iniciales[0] = x
    iniciales[1] = xdot
    iniciales[2] = tetha

    dt = 0.025
    t = np.arange(0, 2, dt)
    sol = odeint(fun, iniciales, t )
    #fun(iniciales,t,L1,L2)

    #print(sol)
    
    sol = odeint(fun, iniciales, t )
     #cachando las soluciones
    x=sol[:,0]
    v=sol[:,1]
    tetha=sol[:,2]
    w=sol[:,3]
    ####################
    Pmx = (x-l*np.sin(tetha)) * 100
    Pmy = l * 100 * np.cos(tetha)
    PMx = 100 * x 
    PMy = np.zeros_like(PMx)
    return x,v,tetha,w,Pmx,Pmy,PMx,PMy,t  
    

#penduloDoble()





