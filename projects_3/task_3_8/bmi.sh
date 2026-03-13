#!/bin/bash

read -r -p "Введите ваш вес (в кг): " WEIGHT
read -r -p "Введите ваш рост (в метрах): " HEIGHT

BMI=$(echo "scale=0; $WEIGHT / $HEIGHT" | bc)

echo "Индекс массы вашего тела: $BMI"


