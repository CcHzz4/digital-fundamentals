peptyde_weight = int(input("Введите количество белков (г): "))
lipids_weight = int(input("Введите количество жиров (г): "))
carbohydrates_weight = int(input("Введите количество углеводов (г): "))

calories = (peptyde_weight + carbohydrates_weight) * 4 + lipids_weight * 9

print(f"Расчетная калорийность: {calories}")