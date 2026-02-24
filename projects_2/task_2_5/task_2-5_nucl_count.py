print(f"=== Анализ последовательности ДНК ===\n")

def nucleotide_count():

    sequence = input("Введите последовательность ДНК: ").upper()

    print(f"\nПоследовательность в верхнем регистре: {sequence}")

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    len_sequence = len(sequence)

    return a_count, t_count, g_count, c_count, len_sequence

result = nucleotide_count()

print(f"\nПодсчёт нуклеотидов:\nA:\t{result[0]}\nT:\t{result[1]}\nG:\t{result[2]}\nC:\t{result[3]}")
print(f"\nОбщая длина: {result[4]}")