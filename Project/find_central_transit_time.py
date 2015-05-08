import numpy as np
import math
from t0_approx import get_t0
from data_in_range import range_data

def find_central_t(time,flux,ferr):

	t = []
	F = []
	sigma = []
	F_real = []

	#Different start value of central transit time can be specified here to calculate 
	#the precise central transit time
	approximate_center = [495.8,500.7,505.6,510.5,515.3,520.2,525.1,530.0,534.9]
	#approximate_center = [539.8,544.7,549.6,554.5,559.4,564.3,569.2,574.1,579.0,583.9,588.8,593.6]
	#approximate_center = [603.4,608.3,613.2,618.1,623.0,627.9]
	#approximate_center = [632.5,637.5,642.4,637.3,642.2,647.1,652.0,656.9,661.8,666.7,671.6,676.5,681.4,686.3,696.0]
	calculated_t0 = []

	for x in approximate_center:
		t,F,F_real,sigma = range_data(time,flux,ferr,x)

		#********************************************
		#Finding the Flux average when not transiting
		N = 5
		for j in range(N):
			F_1 = list(F)
			F_avg = np.average(F)
			F_std = np.std(F)
			m  = 0
			for k in range(len(F)):
				if(abs(F[k]-F_avg)/F_std > 2):
					del F_1[m]
					m = m-1
				m  = m+1
			F = F_1

		F_avg = np.average(F)
		F_std = np.std(F)

		#Normalization with the calculated mean value
		F_real = F_real/F_avg
		sigma = sigma/F_avg

		#Given values of parameters (this value has been calculated from one transit)
		P = 0.07682
		Tao = 0.101150
		T0 = 495.80255
		z = []
		F_fit = []
		chi_2 = 0

		#Calculation of chi-squred (this algorithm narrowing down to a more precise
		#value of T0)
		ranging = np.linspace(x-1,x+1,100)
		a,b = get_t0(ranging, F_real, sigma, t,Tao,P)
		ranging = np.linspace(a-0.1,a+0.1,10)
		a,b = get_t0(ranging, F_real, sigma, t,Tao,P)
		ranging = np.linspace(a-0.01,a+0.01,100)
		a,b = get_t0(ranging, F_real, sigma, t,Tao,P)
		ranging = np.linspace(a-0.001,a+0.001,10)
		a,b = get_t0(ranging, F_real, sigma, t,Tao,P)
		ranging = np.linspace(a-0.0001,a+0.0001,100)
		a,b = get_t0(ranging, F_real, sigma, t,Tao,P)

		calculated_t0.append(a)

		#Write the central time to file
		F = open('central_transit_time.out','w')
		for y in calculated_t0:
			F.write('%.5f\n' %y)
		F.close()

	return calculated_t0