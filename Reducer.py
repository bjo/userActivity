#!/usr/bin/python

import os, sys, re, string

searchmap = {}

for line in sys.stdin:
	val = line.split("\t")
	if len(val) == 3:

		user = val[0]
		sym = val[2].rstrip('\n')

		if user not in searchmap:
			searchmap[user] = []
		if sym not in searchmap[user]:
			searchmap[user].append(sym)

for (key, value) in searchmap.items():
	print "%s %s" % (key, ' '.join(value)) 