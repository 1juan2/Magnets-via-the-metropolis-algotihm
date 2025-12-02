### Libraries in used HERE

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import Functions as Fc

##Read data
EV_matr = np.loadtxt('StateEvol.txt')

Data_E_equil = np.loadtxt('AvrEnergy.txt')
time = Data_E_equil[:, 0]
E_equil = Data_E_equil[:, 1]


##Visualization of the material changing in time

fig1 = plt.figure(figsize = (15,5))
sns.heatmap(EV_matr, annot=False, cbar = False)
plt.xlabel('Time')
plt.ylabel('Num Particles')
#fig1.savefig('State_evolution.pdf')
plt.show()

##Graph equilibration check

fig2 = plt.figure(figsize = (5,5))
plt.plot(time, E_equil)
plt.xlabel('Time')
plt.ylabel('Avr. Energy')
plt.grid()
#fig2.savefig('Avr_Energy_equilCheck.pdf')
plt.show()


##graph analytic solution

n=Fc.Values["Num_particles"]
j=Fc.Values["J"]
k=Fc.Values["K"]
t=np.arange(0.1,5,0.1)
b=Fc.Values["B"]

def u_ana(n,j,k,t):
    return -n*j*np.tanh(j/(k*t))

#print(u_ana(n,j,k,t))

def cal_ana(n,j,k,t):
    return (j/(k*t))**2/(np.cosh(j/(k*t)))

#print(cal_ana(n,j,k,t))

def mag_ana(n,j,k,t,b):
    return n*np.exp(j/(k*t))*np.sinh(b/(k*t))/np.sqrt(np.exp(2*j/(k*t))*(np.sinh(b/(k*t)))**2 + np.exp(-2*j/(k*t)))

#print(mag_ana(n,j,k,t,b))

plt.figure()
plt.title('cálculo analítico de la energía')
plt.plot(t,u_ana(n,j,k,t))
plt.show()

plt.figure()
plt.title('cálculo analítico del calor específico')
plt.plot(t,cal_ana(n,j,k,t))
plt.show()

plt.figure()
plt.title('cálculo analítico de la magentización')
plt.plot(t,mag_ana(n,j,k,t,b))
plt.show()