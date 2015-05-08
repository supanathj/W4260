import numpy as np
import matplotlib.pyplot as plt
import os.path
from get_data import download_data
from find_central_transit_time import find_central_t
from plot_range import plot

#Main Program
#Check if the data file already exist or not. If not, download the data and create file
if not os.path.isfile('KOI97.01.out'):
	time,flue,ferr = download_data(97.01)
else:
	#load data to program's variables
	time,flux,ferr = np.loadtxt('KOI97.01.out', unpack = True)

#Plot raw data to find period of interest (446-538) (465-468) (495-496.5)
plot(time,flux,ferr,484,535)

if not os.path.isfile('central_transit_time.out'):
	central_time = find_central_t(time,flux,ferr)
else:
	#load data to program's variables
	central_time = np.loadtxt('central_transit_time.out', unpack = True)

print '--------------------------------------------'
print 'The calculated transit time are as followed:'
for y in central_time:
	print '%.5f' %y
print '--------------------------------------------'

#Plot calculated central time
plt.figure(2)
X = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,
28,29,30,32,33,34,35,36,37,38,39,41]
p = central_time[1]-central_time[0]
p = 4.8855 #This is also the period of the transit
y = [x*p for x in X] + central_time[0]
plt.scatter(X,central_time)
plt.plot(X,y)
plt.title('Plot of the transit number versus calculated central time')
plt.xlabel('Transit Number')
plt.ylabel('Calculated Central Time (UTC)')
plt.xlim([0,41])

#Plot variation in calculated central time
plt.figure(3)
plt.scatter(X,central_time-y)
plt.title('Difference between fitted linear curve and calculated central time')
plt.xlabel('Transit Number')
plt.ylabel('Time Difference(UTC)')
plt.ylim([-0.005,0.005])
plt.xlim([0,41])
plt.show()