import sys, os

a = []
b = []
c = {}
for line in sys.stdin:
	name, count = line.split('\t')[0], line.split('\t')[1]
	links = line.split('\t')[2]
	a.append(name)
	b.append(int(count))

	links = links.strip("(")
	links = links.strip(")\n")
	links = links.split(") (")

	c[name] = []
	for entry in links:
		sym, corr = entry.split(", ")[0].strip("'"), float(entry.split(", ")[1])
		c[name].append((sym, corr))
	
f = open('#your webapps directory/visualization/data/stocks.json', 'w+')

f.write('{"nodes":[')
i = 0
while i < len(a):
	if i < len(a)-1:
		f.write('{"name":"' + a[i].strip("'") + '","count":' + str(b[i]) + ',"group":1},')
	else:
		f.write('{"name":"' + a[i].strip("'") + '","count":' + str(b[i]) + ',"group":1}')
	i += 1

f.write('],"links":[')

for entry in c:
	i = a.index(entry)
	k = 0
	while k < len(c[entry]):
		j = a.index(c[entry][k][0])
		if c[entry][k][1] >= 0.1 and i > j:
			f.write('{"source":' + str(i) + ',"target":' + str(j) + ',"value":' + str(c[entry][k][1]) + '},')
		k += 1

f.write(']}')

f.close()
