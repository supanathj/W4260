import kplr
import math

#This program use kplr to download kepler data

def download_data(ID):
	#Download Flux Data
	client = kplr.API()
	koi = client.koi(ID) # Find the target KOI.
	lcs = koi.get_light_curves(short_cadence=False) # Get list of datasets.
	time,flux,ferr,quality = [],[],[],[]

	for lc in lcs:
		with lc.open() as f:
			hdu_data = f[1].data
			time.append(hdu_data["time"])  # get the time of each observation
			flux.append(hdu_data["sap_flux"]) # get the flux
			ferr.append(hdu_data["sap_flux_err"]) # get the error in the flux
			quality.append(hdu_data["sap_quality"])
	f.close()

	#write to file
	F = open('KOI97.01.out','w')
	for i in range(len(time)):
		for j in range(len(time[i])):
			if (not math.isnan(flux[i][j])):
				F.write('%.18e\t%.18e\t%.18e\n' %(time[i][j],flux[i][j],ferr[i][j]))
	F.close()
	return time, flux, ferr