### Libraries in used HERE

import numpy as np


### Dictionary
## Constants and general values

Values = {
"Num_particles" : 10,  # (50) The length of the side plate

"total_Time" : 18400,   #Total MC samples

"J" : 1,                # Exchange Energy (1)

"B" : 0,                # Value of the external magnetic field (1)

"Miu" : 0.33,           # giromag times Bohr magneton (0.33)

"K" : 1,                # Botlzmann constant (1)

"T" : [0.1, 0.3, 0.5, 0.7, 0.9, 1.2, 1.5, 1.7, 1.9, 2.2, 2.5, 2.7, 2.9, 3.2, 3.5, 3.7, 3.9, 4.2, 4.5, 4.7, 4.9],                # Temperature (1)

#################

"Start_quantit_calcu" : 2500     #Since which MC iteration we are going to calculate termal quantities.
}


### Functions:

#Energy calculation:

def State_Energy(State):

    sum_ssHoriz = np.sum(State[:, :-1]*State[:, 1:]) + np.sum(State[:, -1]*State[:, 0])         #Cyclic Boundary conditions
    sum_ssVerti = np.sum(State[:-1, :]*State[1:, :]) + np.sum(State[-1, :]*State[0, :])
    sum_ss = sum_ssHoriz + sum_ssVerti
    sum_s = np.sum(State)

    E = - (Values["J"]*sum_ss) - (Values["B"]*Values["Miu"]*sum_s)
    return E


#Equilibration check using Running avarage

def Equil_check(vec_save, E_act, t):

    if t == 1:
        sum_E = vec_save[-1] + E_act
    
    else:
        sum_E = vec_save[-1]*t + E_act

    avr_E = sum_E / (t + 1)

    vec_save.append(avr_E)


#Metropolis algorithm

def Metropoolis(Time, Chain_vector, E_eq_verif, M_eq_verif, Num_itera_star_temoCalcul, temp):

    for i in Time[1:]:

        for _ in range(Values["Num_particles"]**2):                                    #Change multiple spins "at the same time".

            prev_state = np.copy(Chain_vector)                                      ##Save the previous state in case we reject the new one.
            #print(prev_state)
            E_prev = State_Energy(Chain_vector)                                     #Calculate and save the energy of the previous state

            Posit_Rand_Particl = np.random.randint(0, Values["Num_particles"], size = 2)      # first we choose randomly a particle generating a 2d position (x,y)
            #print(Posit_Rand_Particl)

            Chain_vector[Posit_Rand_Particl[0]][Posit_Rand_Particl[1]] *= -1
            #print(Chain_vector)
            E_now = State_Energy(Chain_vector)                                      #Calculate and save the energy of the proposed state
            #print(E_now)

            ## If the energy of the new state is equal or lower than the energy of the previous state, we keep the new one.
            ## If the energy of the new state is higher than the energy of the previous state we use the relative probability and a random number to choose
            delt_E = E_now - E_prev                                                 ## Calculate de Energy difference

            if delt_E <= 0:
                pass
            else:

                Relat_prob = np.exp((-delt_E)/(Values["K"]*temp))  # Calculate the relative probability

                Choose_num = np.random.rand()                             ## we uniformly generate a 1 >= number >= 0 to make the desicion

                if Relat_prob >= Choose_num:
                    pass
                else:
                    Chain_vector = prev_state

        E = State_Energy(Chain_vector)
        M = np.abs(np.sum(Chain_vector))
        Equil_check(E_eq_verif, E, i)
        Equil_check(M_eq_verif, M, i)

        # In equili, termodin quantities are calculated:

        if i >= Num_itera_star_temoCalcul:
            if i == Num_itera_star_temoCalcul:
                Magnetizat = 0
                Inter_Energy = 0
                Segund_mome_Energ = 0

            Magnetizat = Magnetization(Magnetizat, Chain_vector, i, Num_itera_star_temoCalcul)
            Inter_Energy = Moment_energy(Inter_Energy, Chain_vector, i, Num_itera_star_temoCalcul, 1)
            Segund_mome_Energ = Moment_energy(Segund_mome_Energ, Chain_vector, i, Num_itera_star_temoCalcul, 2)

    Specif_heat = (Segund_mome_Energ - (Inter_Energy**2))/((Values["Num_particles"]**2) * Values["K"] * (temp**2))

    return Chain_vector, E_eq_verif, M_eq_verif, Magnetizat, Inter_Energy, Specif_heat


##When the system reaches equilibrium Magnetization, Specific heat and Internal Energy are calculated.

def Magnetization(Final_magnetiz, State, t, start):
    Magnet = np.abs(np.sum(State))

    Final_magnetiz = (Final_magnetiz*(t - start) + Magnet) / (t - start + 1)

    return Final_magnetiz


def Moment_energy(Final_moment, State, t, start, expo):  #Expo is to be able to calculate the first and second Energy moments.
    Energ = (State_Energy(State))**(expo)                   #The first moment is the Internal energy and the second moment is necesary to calculate the Specific heat.

    Final_moment = (Final_moment*(t - start) + Energ) / (t - start + 1)

    return Final_moment
    