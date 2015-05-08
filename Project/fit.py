import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as scint

#This program calculate the flux function as well as find the chi-squared value

#Limb Darkening function
def I(r):
	mu = math.sqrt(1-(r**2))
	return 1-(1-(mu**(1.0/2.0)))

#Delta Method
def delta(r,p,z):
	if(r>=z+p or r<=z-p):
		return 0
	elif(r+z<=p):
		return 1
	else:
		return math.acos((z**2-p**2+r**2)/(2*z*r))/math.pi

#Two function for calculation of Flux
def Func1(r,p,z):
	return I(r)*(1-delta(r,p,z))*2*r

def Func2(r,p,z):
	return I(r)*2*r

#Function for calculating gamma which is used to find p-value
def Func_gamma(t,a):
	return (math.e**(-t))*(t**(a-1))

def chi_square(F_real,sigma,t,T0,Tao,P):
	z_out = []
	F_out = []
	chi_out = 0
	for i in range(len(F_real)):
		z_out.append((t[i]-T0)/Tao)
		#find flux using integration function with equation
		#from problem set 2
		ans1 = scint.quad(Func1,0,1,args=(P,abs(z_out[i])))[0]
		ans2 = scint.quad(Func2,0,1,args=(P,abs(z_out[i])))[0]
		F_out.append(ans1/ans2)
		chi_out = chi_out + ((F_real[i]-F_out[i])/sigma[i])**2
	return chi_out,F_out

#Fuction for calculating p-value
def p_value(x,A):
	ans3 = scint.quad(Func_gamma,x,np.inf,args=(A))[0]
	ans4 = scint.quad(Func_gamma,0,np.inf,args=(A))[0]
	p = ans3/ans4
	return p

