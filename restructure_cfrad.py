from netCDF4 import Dataset
import numpy as np
import sys
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# open file
fname = sys.argv[1]
ncfile = Dataset(fname)
sw_stind = ncfile.variables['sweep_start_ray_index'][:]
sw_enind = ncfile.variables['sweep_end_ray_index'][:]
ranm = ncfile.variables['range'][:]
raygates = ncfile.variables['ray_n_gates'][:]
angles = ncfile.variables['fixed_angle'][:]
azimuth = ncfile.variables['azimuth'][:]
vel = ncfile.variables['VEL'][:]
ref = ncfile.variables['REF'][:]

numsw = len(sw_stind)
numran = raygates[sw_enind]

# get info on a particular sweep
sw = 0
azi_sw = azimuth[sw_stind[sw]:sw_enind[sw]+1]
rankm_sw = ranm[:numran[sw]]/1000.
el_sw = angles[sw]
numazi = len(azi_sw)
numpointssw = numazi*numran[sw]
vel_sw = vel[:numpointssw]
ref_sw = ref[:numpointssw]

# change shape of radar field to (numazi, numran) for that sweep
vel_sw.shape = (numazi, numran[sw])
ref_sw.shape = (numazi, numran[sw])

# make x and y coordinates for plot
rankm_sw.shape = (1, numran[sw])
azi_sw.shape = (numazi, 1)
x = rankm_sw*np.cos(np.pi/180.*(90.-azi_sw))
y = rankm_sw*np.sin(np.pi/180.*(90.-azi_sw))

# create basic plot to test mapping
plt.pcolormesh(x, y, ref_sw, cmap='gist_ncar')
plt.colorbar()
plt.savefig('ref_test.png')
