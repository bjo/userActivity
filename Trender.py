#!/usr/bin/python

# Usage: python popular new_vector

import os, sys, math

path = "#your path for trenders"

old_vector = sys.argv[1]
f1 = open(path + old_vector)

new_vector = sys.argv[2]
f2 = open(path + new_vector)

old_s = {}

for line1 in f1:
	val = line1.strip()
	val = line1.split(" ")
	val[1] = val[1].strip("\n")

	old_s[val[1]] = int(val[0])

new_s = {}
usernum2 = 0

for line2 in f2:
	val = line2.split("\t")

	if len(val) == 3:
		stocks = val[2].strip("\n")
		user = val[0]
		if stocks not in new_s:
			new_s[stocks] = []
		if user not in new_s[stocks]:
			new_s[stocks].append(user)

f1.close()
f2.close()

trenders = {}
for (stocks, users) in new_s.items():
	new_s[stocks] = len(users)
	num = new_s[stocks]
	if num > 10:
		if stocks not in trenders:
			trenders[stocks] = num * 1.0
		if stocks not in old_s:
			old_s[stocks] = 50.0
		ratio = 1.0 * num / old_s[stocks]
		trenders[stocks] = ratio * math.sqrt(old_s[stocks])
		

for entry in trenders:
	print (entry, trenders[entry])
