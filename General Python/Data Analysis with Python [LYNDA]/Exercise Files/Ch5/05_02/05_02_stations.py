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

findstations('LIHUE')
findstations('SAN DIEGO')
findstations('MINNEAPOLIS')
findstations('IRKUTSK')

datastations = ['LIHUE', 'SAN DIEGO', 'MINNEAPOLIS', 'IRKUTSK']



