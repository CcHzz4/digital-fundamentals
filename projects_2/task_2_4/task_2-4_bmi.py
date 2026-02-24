def bmi_count():
    w = float(input("Введите вес (кг): "))
    h = float(input("Введите рост (м): "))

    if h < 0 or h > 3 or w < 0 or w > 500:
        print("Перепроверьте данные. Вес должен быть в (кг), рост должен быть в (м)")
        return bmi_count()

    bmi = w / (h ** 2)

    return w, h, bmi

weight, height, bmi_result = bmi_count()
print(f"--- Отчет о состоянии здоровья ---\nРост:\t{weight}\nВес:\t{height}\nИндекс массы тела:\t{bmi_result:.2f}")