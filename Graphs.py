### Libraries in used HERE

import matplotlib.pyplot as plt
import seaborn as sns


##Visualization of the material changing in time


plt.figure(figsize = (8,5))
sns.heatmap(Evol_Matr, annot=False, cbar = False)
plt.xlabel('Time')
plt.ylabel('Num Particles')
plt.show()

##Graph equilibration check

plt.figure(figsize = (5,5))
plt.plot(time, E_equil_verf)
plt.xlabel('Time')
plt.ylabel('Avr. Energy')
plt.grid()
plt.show()