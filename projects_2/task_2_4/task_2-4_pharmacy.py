def count_sets():
    capsules_produced = int(input("Введите общее количество произведенных капсул (шт): "))
    packing_capacity = int(input("Введите количество капсул в одной упаковке (шт): "))

    if capsules_produced < 0 or packing_capacity < 0:
        print("Проверьте веденные данные")
        return count_sets()
    
    full_pak = capsules_produced // packing_capacity
    rem_cap = capsules_produced % packing_capacity

    return full_pak, rem_cap

full_packages, remaining_capsules = count_sets()

print(f"--- Отчет фасовочного цеха ---\nПолных упаковок:\t{full_packages}\nОстаток капсул:\t\t{remaining_capsules}")