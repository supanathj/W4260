import fit

#This function find the value of T0 that give minimum chi-squared value

def get_t0(input_range,F_real,sigma,t,tao,P):
	T0 = input_range
	min_chi2 = 10000
	min_t0 = 0

	for x in T0:
		chi_2,F_fit = fit.chi_square(F_real,sigma,t,x,tao,P)
		print 'Calculated Chi-2 value (To = %.5f) : %.2f' %(x,chi_2)
		if (chi_2<min_chi2):
			min_chi2 = chi_2
			min_t0 = x
	return min_t0, min_chi2