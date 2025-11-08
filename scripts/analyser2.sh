#!/bin/bash

for i in $(ls &1)
do
  for j in $(cat $1$i)
  do
    email=$(echo $j | cut -d ":" -f3)
    echo $email | grep -o ".*@spbstu.ru"
  done
done
