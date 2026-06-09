import pandas as pd
with open("C:/Users/Виктория/Desktop/6/6_0_6.txt", "w") as f:
    df = pd.read_csv("C:/Users/Виктория/Downloads/wild_boars.csv")
    q1 = df.groupby('gender')['length_cm'].quantile(0.25) #групп по уник значеням м ж и проценталь
    q3 = df.groupby('gender')['length_cm'].quantile(0.75)
    iqr = q3-q1
    for gender in iqr.index: #автоматичски создастся индекс из-за групбай, те тут это мэйл фемэйл
        print(f"{gender}\t iqr = {iqr[gender]:.2f} cm", file=f)
#размах по длине для м и в отдельный файл, дисперсия(уд от их ср ариф)
