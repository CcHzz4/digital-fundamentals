def ph_indetificator(ph_value):

    if ph_value > 7:
        return print("Основная среда")
    elif ph_value < 7:
        return print("Кислая среда")
    else:
        return print("Нейтральная среда")

ph_indetificator(float(input("Введите значение pH: ")))