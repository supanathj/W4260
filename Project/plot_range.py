import numpy as np
import matplotlib.pyplot as plt

#This program plot the raw data in the specified range

def plot(time,flux,ferr,lowerbound,upperbound):
	t = []
	F = []
	sigma = []
	for i in range(len(time)):
		if(time[i]>lowerbound and time[i]<upperbound):
			t.append(time[i])
			F.append(flux[i])

	plt.figure(1)
	plt.plot(t,F)
	plt.xlabel('Time (reduced UTC)')
	plt.ylabel('Flux (counts/s)')
	plt.title('Plot of flux vs time for KOI 97.01')