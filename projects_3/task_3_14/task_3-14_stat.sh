#!/bin/bash

sum=$(awk '{sum += $2} END {print sum}' students.txt)
avg=$(awk '{sum += $2} END {printf "%.2f", sum/NR}' students.txt)
max=$(awk 'NR==1 {max=$2} $2 > max {max=$2} END {print max}' students.txt)

echo "Сумма всех оценок: $sum"
echo "Средняя оценка: $avg"
echo "Максимальная оценка: $max"
