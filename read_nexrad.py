import numpy as np
import struct
from datetime import date, timedelta

# functions
#----------------------------------------------------
# convert modified julian date to 'yyyymmdd' dtring
def mjd2date(mjd):
    mjd_date = date(1970, 1, 1)
    date_new = mjd_date+timedelta(days=mjd-1)
    return date_new.strftime('%y%m%d')

# convert seconds past midnight to 'hhmmss' string
def sec2timestr(sec):
    hh = int(sec/3600.)
    mm = int((sec-hh*3600.)/60.)
    ss = int(sec-hh*3600.-mm*60.)
    return '{:.0f}{:.0f}{:.0f}'.format(hh, mm, ss)
#----------------------------------------------------

# open file
f = open('KBMX20160426_201337_V06', 'rb')

# read header
fname = f.read(9)
ext = f.read(3)
judate = struct.unpack('>i', f.read(4))[0]
time = struct.unpack('>i', f.read(4))[0]/1000.
stn = f.read(4)
print fname, ext, mjd2date(judate), sec2timestr(time), stn

# read metadata record
data = np.fromfile('KBMX20160426_201337_V06', dtype='>i4')
first_bin = '{0:08b}'.format(data[0])
print str(first_bin).decode('utf-8')

# control word of length for each archive 2 message
# 4 byte, big-endian, signed binary

