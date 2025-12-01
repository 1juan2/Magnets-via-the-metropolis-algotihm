### Libraries in used HERE

import Functions as Fc
import numpy as np


##Defining the state vector of spins that create the material (they're fixed, we don't care about positions or momenta)
# and defining the evolution Matrix (it's a matrix since it has to store the state chain vector at each time in order to visualize it)

Chain_Spin_StateVect = np.full(Fc.Values["Num_particles"],1)
Evol_Matr = np.zeros((Fc.Values["Num_particles"], Fc.Values["total_Time"]))

#print(Chain_Spin_StateVect)
#print(Evol_Matr)

Evol_Matr[:,0] = np.transpose(Chain_Spin_StateVect) # Matrix where all states will be saved

E_equil_verf = []                                   # Vector where I'm going to save energy differences to check equilibration
E_equil_verf.clear()

E_equil_verf.append(Fc.State_Energy(Chain_Spin_StateVect))  # Save energy of the initial state


##Evolution of the state vector (Metropolis)

time = np.arange(0, Fc.Values["total_Time"], 1)

Final_evol = Fc.Metropoolis(time, Chain_Spin_StateVect, Evol_Matr, E_equil_verf, Fc.Values["Start_quantit_calcu"])


##Save data to graph

print(Final_evol[2])
print(Final_evol[3])
print(Final_evol[4])

Data_checkEnergy_Equi = np.column_stack((time, Final_evol[1]))

np.savetxt('StateEvol.txt', Final_evol[0])              #Save the evolution of the initial state data in a txt to graph
np.savetxt('AvrEnergy.txt', Data_checkEnergy_Equi)      #Save the Average Energy values in each state to check equilibrium to graph