import pandas as pd
with open("C:/Users/Даша/Desktop/6/6_0_5.txt", "w") as f:
  df = pd.read_csv("C:/Users/Даша/Downloads/wild_boars.csv")
  col = list(df.columns)
  for i in col[2:]:  #напишу полотно для каждого столбца
        parts = i.split('_')
        if len(parts) == 2:
            param = parts[0] 
        else:
            param = parts[0] + ' ' + parts[1]
        print(param, ":", file=f)
        print(f"Percentile 25 (Q1):\t{df[i].quantile(0.25):.1f} {parts[-1]}", file=f)
        print(f"Median 50 (Q2):\t{df[i].quantile(0.50):.1f} {parts[-1]}", file=f)
        print(f"Percentile 75 (Q3):\t{df[i].quantile(0.75):.1f} {parts[-1]}", file=f)
        print(f"Percentile 90:\t{df[i].quantile(0.90):.1f} {parts[-1]}", file=f)
        print(f"Max:\t{df[i].quantile(1.00):.1f} {parts[-1]}\n", file=f)
