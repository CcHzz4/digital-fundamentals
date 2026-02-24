reagent_name = input("Введите название реагента: ")
reagent_value = int(input("Введите количество: "))

print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_value} шт.")

f = open("inventory.txt", "w", encoding="utf-8")
print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_value} шт.", file=f)
f.close()