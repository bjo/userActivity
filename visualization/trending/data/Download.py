#!/usr/bin/python

import os, sys, subprocess
import time

start = time.time()

for line in sys.stdin:
	val = line.split()
	stock = val[0]
	
	directory = '#your quotes directory'
	url = 'ichart.finance.yahoo.com/table.csv?s='
	directory = directory + stock
	url = url + stock

	print "Downloading " + stock + " from " + url

	subprocess.call(['curl', '-x', 'your proxy address', '-U', 'userID:password', '-o', directory, url])

#subprocess.call(['curl', '-x', 'your proxy address', '-U', 'userID:password', '-o', '#your quote directory/COMP.IDX', 'ichart.finance.yahoo.com/table.csv?s=^IXIC'])
print time.time() - start
