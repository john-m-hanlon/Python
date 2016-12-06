import numpy as np
import matplotlib.pyplot as pp
import seaborn
import urllib.request

#print(open('stations.txt','r', encoding='utf8').readlines()[:10])

stations = {}
for line in open('stations.txt','r', encoding='utf8'):
	if 'GSN' in line:
		fields = line.split()

		stations[fields[0]] = ' '.join(fields[4:])

print(len(stations))

def findstations(s):
	found = {code: name for code, name in stations.items() if s in name}
	print(found)

#findstations('LIHUE')
#findstations('SAN DIEGO')
#findstations('MINNEAPOLIS')
#findstations('IRKUTSK')

datastations = ['USW00022536', 'USW00023188', 'USW00014922', 'RSM00030710']

#print(open('USW00022536.dly','r').readlines()[:10])
#print(open('readme.txt','r').readlines()[98:121])

def parsefile(filename):
	return np.genfromtxt(filename,delimiter = dly_delimiter, usecols = dly_usecols, dtype = dly_dtype, names = dly_names)


dly_delimiter = [11,4,2,4] + [5,1,1,1] * 31
dly_usecols = [1,2,3] + [4*i for i in range(1,32)]
dly_dtype = [np.int32,np.int32,(np.str_,4)] + [np.int32] * 31
dly_names = ['years','month','obs'] + [str(day) for day in range(1,31+1)]

lihue = parsefile('USW00022536.dly')
print(lihue)


