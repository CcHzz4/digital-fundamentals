import pandas as pd
with open("C:/Users/Даша/Desktop/6/6_0_8.txt", "w") as f:
    df = pd.read_csv("C:/Users/Даша/Downloads/wild_boars.csv")
    std = df.groupby('gender')['tusk_length_cm'].std()
    sr = df.groupby('gender')['tusk_length_cm'].mean()
    cv = std/sr * 100
    print(f'Coefficient of variations:\n{cv:.1f}', file=f)
