import pandas as pd
with open("C:/Users/Даша/Desktop/6/6_0_4.txt", "w") as f:
  df = pd.read_csv("C:/Users/Даша/Downloads/wild_boars.csv")
  col = list(df.columns)
  for i in col[2:]: 
        mod =  df[i].mode()
        parts = i.split('_')
        if len(parts) == 2:
            param = parts[0] 
        else:
            param = parts[0] + ' ' + parts[1]
        print(f'Boars mode {param} is {mod:.2f} {parts[-1]}\n', file=f)
