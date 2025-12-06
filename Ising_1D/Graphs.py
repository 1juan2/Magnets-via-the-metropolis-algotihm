### Libraries in used HERE

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import Functions as Fc
import Analytic as An
import deriv as Dr


##Read data
EV_matr = np.loadtxt('StateEvol/StateEvol1.txt')

Data_E_equil = np.loadtxt('AvrEnergy/AvrEnergy1.txt')
time = Data_E_equil[:, 0]
E_equil = Data_E_equil[:, 1]

Data_termo_quant = np.loadtxt('Termo_values.txt', skiprows=1)
Magnetiz = Data_termo_quant[:, 0]
Internal_energy = Data_termo_quant[:, 1]
Speci_heat = Data_termo_quant[:, 2]
Temp = np.array(Fc.Values["T"])


n=Fc.Values["Num_particles"]
j=Fc.Values["J"]
k=Fc.Values["K"]
t=np.arange(0.1, Fc.Values["T"][-1], 0.1)
miu=Fc.Values["Miu"]
b=Fc.Values["B"]

##########################################################################


##Visualization of the material changing in time

fig1 = plt.figure(figsize = (15,5))
plt.title('Evolución del estado inicial del modelo de Ising')
sns.heatmap(EV_matr, annot=False, cbar = False)
plt.xlabel('Time')
plt.ylabel('Num Particles')
#fig1.savefig('State_evolution.pdf')
plt.show()


##Graph equilibration check

fig2 = plt.figure(figsize = (5,5))
plt.title('Verif. del equil. promediando la energia del sistema')
plt.plot(time, E_equil)
plt.xlabel('Time')
plt.ylabel('Avr. Energy')
plt.grid()
#fig2.savefig('Avr_Energy_equilCheck.pdf')
plt.show()



#Graphs Analytic vs Termodinamic quantitis

##Magnetization

fig3 = plt.figure(figsize = (5,5))
plt.title('Cálculo analítico de la magentización vs resultado numerico')
plt.plot(t,An.mag_ana(n,j,k,t,b,miu))
plt.plot(Temp, Magnetiz)
plt.xlabel('Temp')
plt.ylabel('Magnetization')
plt.grid()
#fig3.savefig('Magnetizacion.pdf')
plt.show()


##Internal_Energy

fig4 = plt.figure(figsize = (5,5))
plt.title('Cálculo analítico de la energía vs resultado numerico')
plt.plot(t, An.u_ana(n,j,k,t,b,miu))
plt.plot(Temp, Internal_energy)
plt.xlabel('Temp')
plt.ylabel('Internal_Energy')
plt.grid()
#fig4.savefig('Energia_Interna.pdf')
plt.show()


##Speci_heat

fig5 = plt.figure(figsize = (5,5))
plt.title('Cálculo analítico del calor específico vs resultado numerico')
plt.plot(Dr.X[1:-1], Dr.Specif_heat)
plt.plot(Temp, Speci_heat)
plt.xlabel('Temp')
plt.ylabel('Specific heat')
plt.grid()
#fig5.savefig('Calor_especifico.pdf')
plt.show()