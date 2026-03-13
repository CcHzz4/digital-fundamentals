#!/bin/bash

for i in {1..10}; do
	touch "test${i}.txt"
	echo "Создан файл: test${i}.txt"
done

counter=10
while [ $counter -ge 1 ]; do
	if [ -f "test${counter}.txt" ]; then
        	rm "test${counter}.txt"
        	echo "Удален файл: test${counter}.txt"
	fi
	counter=$((counter - 1))
done
