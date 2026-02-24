def blood_group():

    matching = {
        "0": ["0", "A", "B", "AB"],
        "A": ["A", "AB"],
        "B": ["B", "AB"],
        "AB": ["AB"]
    }

    donor_phenotype = input("Введите фенотип группы крови донора (0, A, B, AB): ").strip().upper()
    patient_phenotype = input("Введите фенотип группы крови пациента (0, A, B, AB): ").strip().upper()

    if patient_phenotype in matching[donor_phenotype]:
        return print("\nСовместимые группы крови.")
    else:
        suitable_donors = []
        for donor, patients in matching.items():
            if patient_phenotype in patients:
                suitable_donors.append(donor)
        return print("\nНесовместимые группы крови.\nРекомендованные группы крови пациенту:", ", ".join(suitable_donors))
    
blood_group()