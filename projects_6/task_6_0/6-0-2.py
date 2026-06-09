import pandas as pd
with open("C:/Users/Виктория/Desktop/6/6_0_2.txt", "w") as f:
  df = pd.read_csv("C:/Users/Виктория/Downloads/wild_boars.csv")
  col = list(df.columns) #имена всех колонок в список
  for i in col[2:]: #проходимся по элементам с 3 (т.к. 1 и 2 номер и пол)
        srznac =  df[i].mean() #ср ариф колонки
        parts = i.split('_') 
        if len(parts) == 2:
            param = parts[0] 
        else:
            param = parts[0] + ' ' + parts[1]
        print(f'Boars average {param} is {srznac:.2f} {parts[-1]}\n', file=f)

#медиан. масса 
