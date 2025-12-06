import numpy as np


##Analytic solution

#Internal Energy

def u_ana(n,j,k,t,b,miu):

    a = (miu*b)/(k*t)
    c = (j)/(k*t)
    delt = np.sqrt(np.sinh(a)**2 + np.exp(-4*c))

    u = -n*j - (n/(np.cosh(a) + delt))*((miu*b*np.sinh(a)) + ((miu*b*np.sinh(a)*np.cosh(a) - 2*j*np.exp(-4*c))/delt))
    return u

    #return -n*j*np.tanh(j/(k*t))

#print(u_ana(n,j,k,t))

#Specific Heat (without considering Magnetic field)

#def cal_ana(n,j,k,t):

    #return (j/(k*t))**2/(np.cosh(j/(k*t))**2)

#print(cal_ana(n,j,k,t))

#Magnetization

def mag_ana(n,j,k,t,b,miu):
    return n*np.exp(j/(k*t))*np.sinh((b*miu)/(k*t))/np.sqrt(np.exp(2*j/(k*t))*(np.sinh((b*miu)/(k*t)))**2 + np.exp(-2*j/(k*t)))

#print(mag_ana(n,j,k,t,b))
