### Libraries in used HERE

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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