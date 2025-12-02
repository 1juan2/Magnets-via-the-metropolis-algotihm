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

Data_termo_quant = np.loadtxt('Termo_values.txt', skiprows=1)
Magnetiz = Data_termo_quant[:, 0]
Internal_energy = Data_termo_quant[:, 1]
Speci_heat = Data_termo_quant[:, 2]
Temp = np.array(Fc.Values["T"])

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


#Graphs Termodinamic quantitis

##Magnetization

fig3 = plt.figure(figsize = (5,5))
plt.plot(Temp, Magnetiz)
plt.xlabel('Temp')
plt.ylabel('Magnetization')
plt.grid()
#fig2.savefig('Avr_Energy_equilCheck.pdf')
plt.show()


##Internal_Energy

fig4 = plt.figure(figsize = (5,5))
plt.plot(Temp, Internal_energy)
plt.xlabel('Temp')
plt.ylabel('Internal_Energy')
plt.grid()
#fig2.savefig('Avr_Energy_equilCheck.pdf')
plt.show()


##Speci_heat

fig5 = plt.figure(figsize = (5,5))
plt.plot(Temp, Speci_heat)
plt.xlabel('Temp')
plt.ylabel('Specific heat')
plt.grid()
#fig2.savefig('Avr_Energy_equilCheck.pdf')
plt.show()