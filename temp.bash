#!/bin/bash

for i in {1120..1129}
do
	echo $i
	cat ../../web10w2/web1*/secure.access.log.2012$i* | python Mapper.py > data/out$i
	cat data/out$i | python Reducer.py > data/vector$i
	cat index | python a.py > popular
	python Trender.py popular data/out$i > data/trender$i
done

