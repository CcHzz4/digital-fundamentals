#!/bin/bash

read -r -p "Введите имя гена: " GEN_NAME
read -r -p "Введите уровень экспрессии гена: " EXPRESSION_LEVEL

if ! [[ "$GEN_NAME" =~ ^[[:alpha:]]+$ ]] || ! [[ "$EXPRESSION_LEVEL" =~ ^[0-9]+$ ]]; then
    echo "Ошибка: введите корректное название или значение"
    exit 1
fi


echo "Экспрессия гена $GEN_NAME составляет $EXPRESSION_LEVEL единиц"
