### Libraries in used HERE

import numpy as np


### Dictionary
## Constants and general values

Values = {
"Num_particles" : 100,

"total_Time" : 60000,   #Total MC samples

"J" : 1,                # Exchange Energy

"B" : 1,                # Value of the external magnetic field

"Miu" : 0.33,           # giromag times Bohr magneton

"K" : 1,                # Botlzmann constant

"T" : 5,                # Temperature

#################

"Start_quantit_calcu" : 10000     #Since which MC iteration we are going ro calculate termal quantities.
}


### Functions:

#Energy calculation:

def State_Energy(State):

    sum_ss = sum(State[:-1]*State[1:]) + State[-1]*State[0]         #Cyclic Boundary conditions
    sum_s = sum(State)

    E = - (Values["J"]*sum_ss) - (Values["B"]*Values["Miu"]*sum_s)
    return E
   

#Energy local calculation. Aproximation:  (The algotihm seems to work with the total energy calculation and with the local one)

#def Local_Energy(State, spin_posit):
#
#    if spin_posit == 0:
#        sum_ss = State[0]*State[1] + State[0]*State[-1]
#        sum_s = State[0] + State[1] + State[-1]
#
#    elif spin_posit == Values["Num_particles"] - 1:
#        sum_ss = State[-1]*State[-2] + State[-1]*State[0]
#        sum_s = State[-1] + State[-2] + State[0]
#
#    else:
#        sum_ss = sum(State[spin_posit - 1 : spin_posit + 1]*State[spin_posit : spin_posit + 2])
#        sum_s = sum(State[spin_posit - 1 : spin_posit + 2])
#
#    E = - (Values["J"]*sum_ss) - (Values["B"]*Values["Miu"]*sum_s)
#    return E


#Equilibration check using Running avarage

def Equil_check(vec_save, E_act, t):

    if t == 1:
        sum_E = vec_save[-1] + E_act
    
    else:
        sum_E = vec_save[-1]*t + E_act

    avr_E = sum_E / (t + 1)

    vec_save.append(avr_E)


#Metropolis algorithm

def Metropoolis(Time, Chain_vector, Evol_M, E_eq_verif, Num_itera_star_temoCalcul):

    for i in Time[1:]:

        prev_state = np.copy(Chain_vector)                                      ##Save the previous state in case we reject the new one.

        Posit_Rand_Particl = np.random.randint(0, Values["Num_particles"])      # first we choose randomly a particle

        #print(Posit_Rand_Particl)

        E_prev = State_Energy(Chain_vector)                                     #Calculate and save the energy of the previous state (locally)

        Chain_vector[Posit_Rand_Particl] = -Chain_vector[Posit_Rand_Particl]

        E_now = State_Energy(Chain_vector)                                      #Calculate and save the energy of the proposed state (locally)
        #print(E_now)

        ## If the energy of the new state is equal or lower than the energy of the previous state, we keep the new one.
        ## If the energy of the new state is higher than the energy of the previous state we use the relative probability and a random number to choose
        delt_E = E_now - E_prev                                                 ## Calculate de Energy difference

        if delt_E <= 0:
            Evol_M[:,i] = np.transpose(Chain_vector)

            Equil_check(E_eq_verif, E_now, i)
        else:

            Relat_prob = np.exp((-delt_E)/(Values["K"]*Values["T"]))  # Calculate the relative probability

            Choose_num = np.random.rand()                             ## we uniformly generate a 1 >= number >= 0 to make the desicion

            if Relat_prob >= Choose_num:
                Evol_M[:,i] = np.transpose(Chain_vector)

                Equil_check(E_eq_verif, E_now, i)
            else:
                Chain_vector = prev_state
                Evol_M[:,i] = np.transpose(Chain_vector)
                Equil_check(E_eq_verif, E_prev, i)

        ## In equili, termodin quantities are calculated:

        if i >= Num_itera_star_temoCalcul:
            if i == Num_itera_star_temoCalcul:
                Magnetizat = 0
                Inter_Energy = 0
                Segund_mome_Energ = 0

            Magnetizat = Magnetization(Magnetizat, Chain_vector, i, Num_itera_star_temoCalcul)
            Inter_Energy = Moment_energy(Inter_Energy, Chain_vector, i, Num_itera_star_temoCalcul, 1)
            Segund_mome_Energ = Moment_energy(Segund_mome_Energ, Chain_vector, i, Num_itera_star_temoCalcul, 2)

    Specif_heat = (Segund_mome_Energ - (Inter_Energy**2))/((Values["Num_particles"]**2) * Values["K"] * (Values["T"]**2))

    return Evol_M, E_eq_verif, Magnetizat, Inter_Energy, Specif_heat


##When the system reaches equilibrium Magnetization, Specific heat and Internal Energy are calculated.

def Magnetization(Final_magnetiz, State, t, start):
    Magnet = sum(State)

    Final_magnetiz = (Final_magnetiz*(t - start) + Magnet) / (t - start + 1)

    return Final_magnetiz


def Moment_energy(Final_moment, State, t, start, expo):  #Expo is to be able to calculate the first and second Energy moments.
    Energ = (State_Energy(State))**(expo)                   #The first moment is the Internal energy and the second moment is necesary to calculate the Specific heat.

    Final_moment = (Final_moment*(t - start) + Energ) / (t - start + 1)

    return Final_moment
    