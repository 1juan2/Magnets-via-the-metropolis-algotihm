### Libraries in used HERE
#te amo les
import numpy as np


### Dictionary
## Constants and general values

Values = {
"Num_particles" : 100,

"total_Time" : 10000,

"J" : 1.0,     # Exchange Energy

"B" : 1.0,      # Value of the external magnetic field

"Miu" : 0.33,   # giromag times Bohr magneton

"K" : 1.0,

"T" : 0.02,
}


### Functions:

#Energy calculation:

def State_Energy(State):

    sum_ss = sum(State[:-1]*State[1:])
    sum_s = sum(State)

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

def Metropoolis(Time, Chain_vector, Evol_M, E_eq_verif):

    for i in Time[1:]:

        prev_state = np.copy(Chain_vector)                                      ##Save the previous state in case we reject the new one.

        Posit_Rand_Particl = int(0 + Values["Num_particles"]*np.random.rand())  # first we choose randomly a particle

        #print(Posit_Rand_Particl)

        E_prev = State_Energy(Chain_vector)                                     #Calculate and save the energy of the previous state

        Chain_vector[Posit_Rand_Particl] = -Chain_vector[Posit_Rand_Particl]

        E_now = State_Energy(Chain_vector)                                      #Calculate and save the energy of the proposed state
        #print(E_now)

        ## If the energy of the new state is equal or lower than the energy of the previous state, we keep the new one.
        ## If the energy of the new state is higher than the energy of the previous state we use the relative probability and a random number to choose

        if(E_now <= E_prev):
            Evol_M[:,i] = np.transpose(Chain_vector)

            Equil_check(E_eq_verif, E_now, i)

        else:
            delt_E = E_now - E_prev                                 ## Calculate de Energy difference

            Relat_prob = np.exp(-delt_E/(Values["K"]*Values["T"]))  # Calculate the relative probability

            Choose_num = np.random.rand()                           ## we uniformly generate a 1 >= number >= 0 to make the desicion

            if(Relat_prob >= Choose_num):
                Evol_M[:,i] = np.transpose(Chain_vector)

                Equil_check(E_eq_verif, E_now, i)
            
            else:
                Evol_M[:,i] = np.transpose(prev_state)

                Equil_check(E_eq_verif, E_prev, i)

    
    return Evol_M
