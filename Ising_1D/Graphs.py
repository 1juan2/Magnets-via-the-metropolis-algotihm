### Libraries in used HERE

import matplotlib.pyplot as plt
import matplotlib.colors as clt
import numpy as np
import seaborn as sns
import Functions as Fc
import Analytic as An
import deriv as Dr


##Read data
EV_matr0 = np.loadtxt('StateEvol/StateEvol0.7.txt')
EV_matr1 = np.loadtxt('StateEvol/StateEvol1.7.txt')
EV_matr2 = np.loadtxt('StateEvol/StateEvol2.7.txt')
EV_matr3 = np.loadtxt('StateEvol/StateEvol3.7.txt')
EV_matr4 = np.loadtxt('StateEvol/StateEvol4.7.txt')

Data_E_equil = np.loadtxt('AvrEnergy/AvrEnergy2.7.txt')
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

colors = ["black", "gray"]
cmap = clt.ListedColormap(colors)
bounds = [-1, 0, 1]
norm = clt.BoundaryNorm(bounds, cmap.N)

fig1, ax = plt.subplots(2, 1, figsize = (15,15), sharex=True, sharey=True)
fig1.suptitle('Evolución del estado inicial del modelo de Ising')

sns.heatmap(EV_matr0, annot=False, cbar = False, cmap = cmap, norm = norm, ax=ax[0])
ax[0].set_ylabel('Num Particles')

sns.heatmap(EV_matr4, annot=False, cbar = False, cmap = cmap, norm = norm, ax=ax[1])
ax[1].set_xlabel('t (Metrop. units)')
ax[1].set_ylabel('')

#ax.set_xlim(0, 300) #Iterations
#ax.set_ylim(0, 200) #Num. particles

cbar = fig1.colorbar(ax[0].collections[0], ax=ax, orientation='vertical')
cbar.set_ticks([-0.5, 0.5])             # Ticks halfway between boundaries
cbar.set_ticklabels(['-1', '1'])        # Label those positions

plt.subplots_adjust(hspace=0.05, top=0.95, bottom=0.09, right=0.77, left=0.06)
for axis in ax:
    axis.tick_params(axis='y', labelsize=8)
    axis.tick_params(axis='x', labelsize=10)

ax[0].locator_params(axis='x', nbins=10)
ax[0].locator_params(axis='y', nbins=5)
ax[1].locator_params(axis='x', nbins=10)
ax[1].locator_params(axis='y', nbins=5)
#fig1.savefig('State_evolution.pdf')
plt.show()


##Graph equilibration check

fig2 = plt.figure(figsize = (5,5))
plt.title('Verif. del equil. promediando la energia del sistema')
plt.plot(time, E_equil, label = "Energ. promedio")
plt.xlabel('t(Metrop. units)')
plt.ylabel('Energia (J)')
plt.grid()
plt.legend()
#fig2.savefig('Avr_Energy_equilCheck.pdf')
plt.show()



#Graphs Analytic vs Termodinamic quantitis

fig3, ax = plt.subplots(1, 3, figsize = (15,5))
fig3.suptitle('Cantidades termodin. en el equilibrio, analíticas vs numéricas', fontsize=16)
##Magnetization

ax[0].set_title('Magentización')
ax[0].plot(Temp, Magnetiz, label = "Numer")
ax[0].plot(t,An.mag_ana(n,j,k,t,b,miu), linestyle='--', color = 'black', alpha = 0.7, label = "Analit")
ax[0].set_xlabel(r'Temp(k)')
ax[0].set_ylabel(r'Magnetiz.') 
ax[0].legend()
ax[0].grid()

##Internal_Energy

ax[1].set_title('Energia Interna')
ax[1].plot(Temp, Internal_energy, label = "Numer")
ax[1].plot(t, An.u_ana(n,j,k,t,b,miu)[0], linestyle='--', color = 'black', alpha = 0.7, label = "Analit cons. B")
ax[1].plot(t, An.u_ana(n,j,k,t,b,miu)[1], linestyle='--', color = 'orange', alpha = 0.7, label = "Analit no cons. B")
ax[1].set_xlabel(r'Temp(k)')
ax[1].set_ylabel(r'Energia(J)')
ax[1].legend()
ax[1].grid()

##Speci_heat

ax[2].set_title('Calor especifico')
ax[2].plot(Temp, Speci_heat, label = "Numer")
ax[2].plot(Dr.X[1:-1], Dr.Specif_heat, linestyle='--', color = 'black', alpha = 0.7, label = "Analit cons. B")
ax[2].plot(t, An.cal_ana(n,j,k,t), linestyle='--', color = 'orange', alpha = 0.7, label = "Analit no cons. B")
ax[2].set_xlabel(r'Temp(k)')
ax[2].set_ylabel(r'Calor espec.(J/K)')
ax[2].legend()
ax[2].grid()

#fig3.savefig('Thermo_quanti.pdf')
fig3.tight_layout(pad=2.0)
plt.show()