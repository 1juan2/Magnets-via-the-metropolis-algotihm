### Libraries in used HERE

import Functions as Fc
import numpy as np
import os


for case in range(len(Fc.Values["T"])):

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

    Final_evol = Fc.Metropoolis(time, Chain_Spin_StateVect, Evol_Matr, E_equil_verf, Fc.Values["Start_quantit_calcu"], Fc.Values["T"][case])


    ##Save data to graph

    #print(Final_evol[2])
    #print(Final_evol[3])
    #print(Final_evol[4])

    Final_evol_array = np.array(Final_evol[2:])

    ##Name creation to save the data

    FoldName_State = "StateEvol"
    FileName_State = 'StateEvol' + str(round(Fc.Values["T"][case], 1)) + '.txt'
    Path_State = os.path.join(FoldName_State, FileName_State)
    os.makedirs(FoldName_State, exist_ok=True)

    FoldName_AvrEner = "AvrEnergy"
    FileName_AvrEner = 'AvrEnergy' + str(round(Fc.Values["T"][case], 1)) + '.txt'
    Path_AvrEner = os.path.join(FoldName_AvrEner, FileName_AvrEner)
    os.makedirs(FoldName_AvrEner, exist_ok=True)

    if case == 0:
        np.savetxt('Termo_values.txt', Final_evol_array.reshape(1, -1), header='Magnetization Internal_Energy Specific_heat')
    else:
        with open('Termo_values.txt', 'a') as f:
            np.savetxt(f, Final_evol_array.reshape(1, -1))

    Data_checkEnergy_Equi = np.column_stack((time, Final_evol[1]))

    np.savetxt(Path_State, Final_evol[0])                #Save the evolution of the initial state data per temperature in a txt to graph
    np.savetxt(Path_AvrEner, Data_checkEnergy_Equi)      #Save the Average Energy values in each state per temperature to check equilibrium to graph