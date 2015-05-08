import matplotlib.pyplot as plt
import numpy as np
import os.path

#This program stacks the different transits into one plot

def plot(time,flux,ferr,lowerbound,upperbound,count):
	t = []
	F = []
	sigma = []
	F_real = []

	#Get the data in the specified range
	for i in range(len(time)):
		if(time[i]>=lowerbound and time[i]<=upperbound):
			t.append(time[i])
			F.append(flux[i])
			F_real.append(flux[i])

	#Normalize the data set
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
	F_real = F_real/F_avg
	sigma = sigma/F_avg

	#Plot each transit with shifted constant
	plt.plot([x - t[0] for x in t],[y - F_real[0]- count*0.0002 for y in F_real])

#Check if the data file already exist or not. If not, download the data and create file
if not os.path.isfile('KOI97.01.out'):
	time,flue,ferr = download_data(97.01)
else:
	#load data to program's variables
	time,flux,ferr = np.loadtxt('KOI97.01.out', unpack = True)

#Get the central_time from file or calculate it
if not os.path.isfile('central_transit_time.out'):
	central_time = find_central_t(time,flux,ferr)
else:
	#load data to program's variables
	central_time = np.loadtxt('central_transit_time.out', unpack = True)

central_time = np.loadtxt('central_transit_time.out', unpack = True)
X = [0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,
28,29,30,32,33,34,35,36,37,38,39,41]

#calculate the period
period = central_time[1]-central_time[0]

#Plot the final stacked figure
fig = plt.figure(1)
for i in X:
	plot(time,flux,ferr,period*i+central_time[0]-.25,period*i+central_time[0]+0.25,i)
ax = fig.add_subplot(111)
plt.ylim([-0.018,0.002])
plt.xlim([0.05,0.45])
ax.get_yaxis().set_visible(False)
plt.xlabel('Relative Time (UTC)')
plt.show()
