import pandas as pd

df = pd.read_excel('test.xlsx')

df1=list(df)
df1.pop(0)


rez=pd.DataFrame({
     'Контрмеры': [ ],
     'Значение контрмеры':[]
     })
rez['Контрмеры']=df['Контрмеры']

for i in range(len(df['Контрмеры'])):
     rez.loc[i, 'Значение контрмеры'] = 1
     for j in df1:
          rez.loc[i, 'Значение контрмеры'] = rez['Значение контрмеры'][i] * df[j][i]

print(rez)




