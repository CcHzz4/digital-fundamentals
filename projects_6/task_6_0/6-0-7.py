import pandas as pd
with open("C:/Users/Даша/Desktop/6/6_0_7.txt", "w") as f:
  df = pd.read_csv("C:/Users/Даша/Downloads/wild_boars.csv")
  col = list(df.columns)
  for i in col[2:]: 
        vari =  df[i].var()
        std = df[i].std()
        cv = (std / df[i].mean()) * 100
        parts = i.split('_')
        if len(parts) == 2:
            param = parts[0] 
        else:
            param = parts[0] + ' ' + parts[1]  
        print(f'{param} variance is {vari:.1f} {parts[-1]}²', file=f)
        print(f'{param} standart deviation is {std:.1f} {parts[-1]}', file=f)
        print(f'{param} coefficient of variation is {cv:.1f}\n', file=f)
