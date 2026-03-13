#!/bin/bash

USER=$(whoami)

echo "Пользователь: $USER"
echo "Время: $(date +"%H:%M:%S")"
echo "Рабочий каталог: $(pwd)"
echo "Аргументов: $#"
