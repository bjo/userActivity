#!/bin/bash

for i in {1120..1129}
do
	echo $i
	cat "#your directory"/secure.access.log.2012$i* | python Mapper.py > data/out$i
	cat data/out$i | python Reducer.py > data/vector$i
	cat data/vector$i | python Indexer.py
	cat index | python a.py > popular
	python Trender.py popular data/out$i > data/trender$i
done

