import numpy as np
from scipy.integrate import  odeint
import matplotlib.pyplot as plt

def penduloDoble():

    def fun(iniciales,t,l1,l2):
   
        iniciales=[1,0,1,0]
        l1=1
        l2=1 
        m1=1
        m2=2
        tetha1=iniciales[0]
        w1=iniciales[1]
        tetha2=iniciales[2]
        w2=iniciales[3]
        dA=iniciales[0]-iniciales[3]
        #data = np.array([[1, 2], [3, 4]])
        D = np.array( [[ (m1+m2) * l1**2 , m2*l1*l2*np.cos(dA) ] , [m2*l1*l2*np.cos(dA) , m2*l2*l2 ]])
        C=np.array([[m2*l1*l2*np.sin(dA) * w2**2 ],[-m2*l1*l2*np.sin(dA) * w1**2]])
        G=np.array( [ [m2*l1*l2*np.sin(dA) * w2**2 ] , [-m2 * l1 * l2 * np.sin(dA) * w1**2] ] )
        T=np.array([[1],[1]]) 
        aceleraciones=-(np.linalg.inv(D)) @ C - (np.linalg.inv(D)) @ G #+ (np.linalg.inv(D)) @ T
        aceleraciones = np.array(aceleraciones, dtype=float)
        derivadas=(aceleraciones[0].astype(float),w1,aceleraciones[1].astype(float),w2)
        
        return derivadas

    iniciales=np.array([np.pi*.5-.7,0,np.pi*.5,0])
    dt=.04
    t = np.arange(0,15,dt)
    L1=1
    L2=2
    fun(iniciales,t,L1,L2)



    sol = odeint(fun, iniciales, t ,args=(L1,L2))
    angulo1=sol[:,0]
    velocidad1=sol[:,1]
    print(sol)
    angulo2=sol[:,2]
    velocidad2=sol[:,3]
    X1=L1*100*np.sin(angulo1)
    Y1=L1*100*np.cos(angulo1)
    X2=L1*100*np.sin(angulo1)+L2*np.sin(angulo2)
    Y2=L1*100*np.cos(angulo1)+L2*np.cos(angulo2)
    anguloGra1=np.degrees(angulo1)
    anguloGra1=np.around(anguloGra1,decimals=1)
    velocidad1=np.around(velocidad1,decimals=1)
    #print(angulo1)
    return anguloGra1,velocidad1,X1,Y1,X2,Y2,t 


penduloDoble()






