### Libraries in used HERE

import Functions2D as Fc2
import numpy as np
import os


for case in range(len(Fc2.Values["T"])):

    ##Defining the state matrix of spins that create the material (they're fixed, we don't care about positions or momenta)

    Matrix_Spin_StateVect = np.random.choice([-1, 1], size = (Fc2.Values["Num_particles"],Fc2.Values["Num_particles"]), replace = True) #Create a matrix N*N with spin up 

    #print(Chain_Spin_StateVect)
    #print(Evol_Matr)


    E_equil_verf = []                                   # Vector where I'm going to save energy differences to check equilibration
    E_equil_verf.clear()

    E_equil_verf.append(Fc2.State_Energy(Matrix_Spin_StateVect))  # Save energy of the initial state


    ##Evolution of the state vector (Metropolis)

    time = np.arange(0, Fc2.Values["total_Time"], 1)

    Final_evol = Fc2.Metropoolis(time, Matrix_Spin_StateVect, E_equil_verf, Fc2.Values["Start_quantit_calcu"], Fc2.Values["T"][case])


    ##Save data to graph

    #print(Final_evol[2])
    #print(Final_evol[3])
    #print(Final_evol[4])

    Final_evol_array = np.array(Final_evol[2:])

    ##Name creation to save the data

    FoldName_State = "StateEvol"                                        #Create and save the data of the initial state and state evolution for each temp
    FileName_State = 'StateEvol' + str(Fc2.Values["T"][case]) + '.txt'
    FileName_InitStat = 'Init_state' + str(Fc2.Values["T"][case]) + '.txt'
    Path_InitStat = os.path.join(FoldName_State, FileName_InitStat)
    Path_State = os.path.join(FoldName_State, FileName_State)
    os.makedirs(FoldName_State, exist_ok=True)

    FoldName_AvrEner = "AvrEnergy"                                      #Create and save the data of the aver energy of the state for each temp
    FileName_AvrEner = 'AvrEnergy' + str(Fc2.Values["T"][case]) + '.txt'
    Path_AvrEner = os.path.join(FoldName_AvrEner, FileName_AvrEner)
    os.makedirs(FoldName_AvrEner, exist_ok=True)

    if case == 0:                                                       #Save termod. quantities in a .txt file
        np.savetxt('Termo_values.txt', Final_evol_array.reshape(1, -1), header='Magnetization Internal_Energy Specific_heat')
    else:
        with open('Termo_values.txt', 'a') as f:
            np.savetxt(f, Final_evol_array.reshape(1, -1))

    Data_checkEnergy_Equi = np.column_stack((time, Final_evol[1]))

    np.savetxt(Path_InitStat, Matrix_Spin_StateVect)     #Save the initial state of the system in the same folder as the evol. states (per temp)
    np.savetxt(Path_State, Final_evol[0])                #Save the evolution of the initial state data per temperature in a txt to graph
    np.savetxt(Path_AvrEner, Data_checkEnergy_Equi)      #Save the Average Energy values in each state per temperature to check equilibrium to graph