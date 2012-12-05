#!/usr/bin/python
# or your python directory
# Remove all comments on print statements for debugging purposes.

import os, sys, re, math
import time

comp_map = {}
user_map = {}

#print "Building User Map"

start = time.time()

for line in sys.stdin:
	val = line.split()
	user = val[0]
	stocks = val[1:]
	
	if user not in user_map:
		user_map[user] = []

	for item in stocks:
		if item not in comp_map:
			comp_map[item] = 0
		if item not in user_map[user]:
			user_map[user].append(item)
			comp_map[item] += 1

#print len(comp_map)

prune = []

for entry in comp_map:
	if comp_map[entry] < 50:
		prune.append(entry)

for entry in prune:
	del comp_map[entry]

map_size = len(comp_map)
#print map_size
i = 0
matrix = []

all_stocks = sorted(comp_map)

f = open('#your directory for your list of symbols', 'w+')
f.write(str(len(all_stocks)) + ' ' + ' '.join([str(k) for k in all_stocks]))
f.flush()
f.close()

while i < map_size:
	matrix.append([0 for k in range(map_size)])
	i += 1

total = len(user_map)
#print total
i = 0

for user in user_map:
	for item_a in user_map[user]:
		if item_a in comp_map:
			a = all_stocks.index(item_a)
			matrix[a][a] += 1
			for item_b in user_map[user]:
				if item_b in comp_map:
					b = all_stocks.index(item_b)
					if a != b:
						matrix[a][b] += 1
	i += 1
	#if i % 10000 == 0:
	#	print i

lengths = []
matrix1 = []

i = 0
while i < len(matrix):
	lengths.append(matrix[i][i])
	matrix1.append([0 for k in range(len(matrix))])
	i += 1

#print time.time() - start

#print "Starting Matrix Calculations"

start = time.time()

i = 0
while i < len(matrix):
	j = 0
	while j < len(matrix):
		if j == i:
			matrix1[i][j] = 1
		elif j < i:
			matrix1[i][j] = matrix1[j][i]
		else:
			pa = 1.0*matrix[i][i]
			pb = 1.0*matrix[j][j]
			pab = 1.0*matrix[i][j]

			sab = (pab)*(1 - (pa/total))*(1 - (pb/total)) + (pa - pab)*(1 - (pa/total))*(-1*(pb/total)) + (pb - pab)*(-1*(pa/total))*(1 - (pb/total)) + (total - pa - pb + pab)*(-1*(pa/total))*(-1*(pb/total))
			ssa = pa*pow(1 - (pa/total),2) + (total-pa)*pow(-1*(pa/total),2)
			ssb = pb*pow(1 - (pb/total),2) + (total-pb)*pow(-1*(pb/total),2)

			matrix1[i][j] = sab / pow(ssa * ssb, 0.5)
		j += 1
	i += 1

#print time.time() - start

f2 = open('#your directory for your matrix', 'w+')
f3 = open('#your directory for your index', 'w+')

#print "Building Indexes"

start = time.time()

i = 0
while i < len(matrix):
	f2.write(' '.join([str(k) for k in matrix[i]]))
	f2.write('\n')

	if lengths[i] >= 10:

		recommend = [('', 0) for j in range(15)]

		j = -1
		while j < 15:
			ind1, val1 = matrix1[i].index(max(matrix1[i])), max(matrix1[i])
			# print ind1, val1
			if j != -1:
				recommend[j] = (all_stocks[ind1], val1)
			j += 1
			# print "zeroing %s and %s" % (comp_map[i], comp_map[ind1]) + str(matrix[i][ind1])
			matrix1[i][ind1] = 0

		f3.write(all_stocks[i] + '\t' + str(lengths[i]) + '\t'+ ' '.join(str(entry) for entry in recommend))
		f3.write('\n')

	i += 1

	#if i % 1000 == 0:
	#	print "1000"

#print time.time() - start

f2.close()
f3.close()
