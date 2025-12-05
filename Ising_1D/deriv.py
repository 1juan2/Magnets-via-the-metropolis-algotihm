import numpy as np
import matplotlib.pyplot as plt
import Functions as Fc
import Analytic as An


m=10000  ##Derivate step

X = np.linspace(Fc.Values["T"][0], Fc.Values["T"][-1],m)
fx=An.u_ana(Fc.Values["Num_particles"],Fc.Values["J"],Fc.Values["K"],X,Fc.Values["B"],Fc.Values["Miu"]) 
h=((Fc.Values["T"][-1] - Fc.Values["T"][0])/ (m-1))

Specif_heat = ((fx[2:])-(fx[:-2]))/(2*h*Fc.Values["Num_particles"]**2)


##Graph of the derivate (Specific Heat)

#plt.figure()
#plt.subplot(121)
#plt.grid(True)
#plt.plot(X,fx)
#plt.subplot(122)
#plt.grid(True)
#plt.plot(X[1:-1], Specif_heat)
#plt.show()
