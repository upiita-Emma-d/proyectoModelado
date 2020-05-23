import numpy as np 
from scipy.integrate import  odeint
def resorte():
    idm=0
    fdm=50
    dt=0.1
    t=np.arange(idm,fdm,dt)
    def mmr(y,t,m,k):
        x,v =y
        dxdy=[ v ,(-k/m) * x]
        return dxdy

    m=5
    k=.1
    y0=[1,0]
    sol=odeint(mmr,y0,t,args=(m,k))
    x=sol[:,0]
    velocidad=sol[:,1]
    
    x=abs(x)
    velocidad=abs(velocidad )
    xp=x*100

    return x,velocidad,xp,np.zeros_like(xp),t 
resorte()

