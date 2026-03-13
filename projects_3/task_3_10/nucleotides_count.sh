#!/bin/bash

printf "%-19s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do

	if [ ! -s "$file" ]; then
		continue
	fi

	a_count=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "A" | wc -l)
	t_count=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "T" | wc -l)
	c_count=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "C" | wc -l)
	g_count=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "G" | wc -l)
	printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$a_count" "$t_count" "$g_count" "$c_count"
done
