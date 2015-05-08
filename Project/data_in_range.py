#This program return the range of data when specify 
#the approximate central transit time

def range_data(time,flux,ferr,approx_center):
	lower_bound = approx_center-0.6
	upper_bound = approx_center+0.6
	t = []
	F = []
	sigma = []
	F_real = []
	for i in range(len(time)):
		if(time[i]>lower_bound and time[i]<upper_bound):
			t.append(time[i])
			F.append(flux[i])
			F_real.append(flux[i])
			sigma.append(ferr[i])
	return t,F,F_real,sigma