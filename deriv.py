import numpy as np
import matplotlib.pyplot as plt
import Functions as Fc

def funcion(n,j,k,t,b,miu):

    a = (miu*b)/(k*t)
    c = (j)/(k*t)
    delt = np.sqrt(np.sinh(a)**2 + np.exp(-4*c))

    u = -n*j - (n/(np.cosh(a) + delt))*((miu*b*np.sinh(a)) + ((miu*b*np.sinh(a)*np.cosh(a) - 2*j*np.exp(-4*c))/delt))
    return u

m=10000

X=np.linspace(0.1,5,m)
fx=funcion(Fc.Values["Num_particles"],Fc.Values["J"],Fc.Values["K"],X,Fc.Values["B"],Fc.Values["Miu"]) 
h=(( 5 -0.)/ (m-1))

cen_d=((fx[2:])-(fx[:-2]))/(2*h)/Fc.Values["Num_particles"]**2

plt.figure()
plt.subplot(121)
plt.grid(True)
plt.plot(X,fx)
plt.subplot(122)
plt.grid(True)
plt.plot(X[1:-1],cen_d)
plt.show()
