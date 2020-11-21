import pandas as pd
df = pd.DataFrame({
     'Контрмеры': [ ],
     'Значение контрмеры':[],
     'Тип':[],
     'Замещение':[],
     'Блок':[],
     'Зашумление':[],
     'Метод':[],
     'Ручной':[],
     'Автоматизированный':[],
     'Смещанный':[],
     'Широта':[],
     'Группа':[],
     'Сообщение':[],
     
 })

rez=pd.DataFrame({
     'Контрмеры': [ ],
     'Значение контрмеры':[]
     })

rez1=list(rez)
df1=list(df)
df1.pop(0)



            
print('Введите количество контрмер');
contrmer=[]
colcontr=int(input());
for i in range(colcontr):
    row = input()
    contrmer.append(row)
print(contrmer)
df['Контрмеры']=contrmer
rez['Контрмеры']=contrmer
print(df.stack())

print(df)



lst1=[]
print('Введите количество экспертов')
ekspert=int(input());
for i in range(ekspert):
    row = input().split()
    lst1.append(row)
      
 
A=[]    


t=0
r=0
for i in range(colcontr):
    for j in range(len(df1)):
        for e in range(ekspert):
            print(lst1[e], df1[j],contrmer[i])
            row = int(input())
            
            if t!=ekspert:
                t=t+1
                r=row+r 
            if t==ekspert:
                A.append(df1[j])
                A.append(r/ekspert)
                r=0
                t=0
            
print(A)
            

        

r=0
t=0


 

for j in range(len(A)):
    for i in df1:
        if i==A[j]:
            if t<12:
                df.loc[r,i]=A[j+1]
                print('i=',i)
                print('A[]j]=',A[j])
                print('A[]j]=',A[j+1]) 
                print('t=',t)
                print('r=',r)
                t=t+1
            if t>=12:
                t=0
                r=r+1
            

print(df.iloc[0])     
    

for i in range(colcontr):
    rez.loc[i,rez1[1]]=1
    for j in df1:
        
        rez.loc[i,rez1[1]]=rez[rez1[1]][i]*df[j][i]
        
    

print(rez)













    
    