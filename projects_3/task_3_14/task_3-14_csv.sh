#!/bin/bash

awk -F',' '{print $2}' data.csv
awk -F',' '$3 > 20 {print $2, "-", $3}' data.csv
awk -F',' '{sum += $3} END {print "Сумма:", sum}' data.csv
