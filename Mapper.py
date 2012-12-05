#!/usr/bin/python


import sys, re, time, string

start = time.time()
previd = ""
prevsym = ""

for line in sys.stdin:
	val = line.strip()
	fields = val.split()

	times = fields[3][13:18].replace(":", "-")

	i1 = fields[6].find("symbol=")
	i2 = fields[10].find("symbol=")

	i3 = fields[6].find("symbol=&")
	i4 = fields[10].find("symbol=&")

	if fields[5] != '"HEAD' and (i1 != -1 or i2 != -1):
	#and fields[2] != "-"
		if (i3 == -1 and i4 == -1):
			if i1 != -1:
				sym = re.search(r'[a-zA-Z\.]+', fields[6][i1+7:])
			else:
				sym = re.search(r'[a-zA-Z\.]+', fields[10][i2+7:])
			if sym is not None:
				symbol = string.upper(sym.group())
			#if previd != fields[2] or prevsym != symbol:
			print "%s\t%s\t%s" % (fields[2], times, symbol)
			previd = fields[2]
			prevsym = symbol

	sys.stdout.flush()

print time.time() - start