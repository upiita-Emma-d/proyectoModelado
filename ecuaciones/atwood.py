import numpy as np 
from scipy.integrate import  odeint
def atwood():
    idm=0
    fdm=1.5
    dt=0.004
    t=np.arange(idm,fdm,dt)
    def mmr(y,t,m1,m2):
        x,v =y
        dxdy=[ v ,(m1-m2)/(m1+m2)*g]
        return dxdy
    g=9.81
    m1=1
    m2=2
    #k=.1
    y0=[3,0]
    sol=odeint(mmr,y0,t,args=(m1,m2))
    x=sol[:,0]
    velocidad=sol[:,1]
    yp=(x*100)+20
    atw=True
    return x,velocidad,np.full_like(yp,3),yp,t,atw 

