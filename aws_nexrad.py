import boto3
from numpy import array, argmin, abs
from datetime import datetime
import os

# function to convert string time 'HHMMSS' into number of seconds past midnight
def tstring2secs(tstring):
    h = float(tstring[0:2])
    m = float(tstring[2:4])
    s = float(tstring[4:6])
    return 3600.*h+60.*m+s

# set up access to aws server
s3 = boto3.resource('s3')
bucket = s3.Bucket('noaa-nexrad-level2')

# set radar site and set time as now
radsite = 'KCCX'
now = datetime.utcnow()
yyyy = now.year
mm = now.month
dd = now.day
hh = now.hour
mn = now.minute
ss = now.second

# optionally enter date and time manually
'''
yyyy = 2017
mm = 4
dd = 26
hh = 20
mn = 13
ss = 0
'''

# get keys for restricted files
prefix = '{:04d}/{:02d}/{:02d}/{}'.format(yyyy, mm, dd, radsite)
objs = bucket.objects.filter(Prefix=prefix)
keys = [o.key for o in objs]
fnames = [k.split('/')[-1] for k in keys]
times = [f.split('_')[1] for f in fnames]

# remove erroneous files with 'NEXRAD' in name
numtimes = 0
for t in times:
    if t=='NEXRAD':
        pass
    else:
        numtimes = numtimes+1

times_valid = times[0:numtimes-1]

# get file with closest time to want time
secs = [tstring2secs(t) for t in times_valid]
want_time = '{:02d}{:02d}{:02d}'.format(hh, mn, ss)
want_secs = tstring2secs(want_time)
secs_arr = array(secs)
closeind = argmin(abs(secs_arr-want_secs))

# download file
dkey = keys[closeind]
dfile = fnames[closeind]
s3_client = boto3.client('s3')
s3_client.download_file('noaa-nexrad-level2', dkey, dfile)
os.system('gunzip {}'.format(dfile))
