import numpy as np
import pandas as pd
df3 = pd.DataFrame({
     'id стены': ['маша','саша','маша','дима','дима','дима','маша','наташа','маша','саша','маша','наташа'],
     'url комментария':[5,6,2,4,12,13,14,15,16,17,18,19],
     'type':[1,2,3,2,3,1,2,1,1,3,3,1],
     'кол-во лайков':[300,10,1000,500,600,30,50,290,890,50,10,0],
     'кол-во коментов':[2,1,3,4,2,5,7,10,100,300,600,0,],
     'кол-во просмотров':[500,600,1202,3000,50,80,6700,5980,3450,2340,2350,5460],
     'число друзей':[100,200,100,100,100,100,100,100,100,100,100,100]
     
     
 })

df4=list(df3)
df3 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=df4)
type1=list(df3['type'])
for i in range(len(type1)):
    if type1[i]>1 and type1[i]<3:
        type1[i]=0.5
    elif  type1[i]>=3:
        type1[i]=0.25
print(type1)
df3['type']=type1
        
df5 = pd.DataFrame({
     'id стены': [ ],
     'сумма url':[],
     'potential_sours':[],
     'индекс активности':[],
     'индекс просматриваемости':[],
     'кол-во друзей':[],
     'индекс влиятельности':[]
     
     
 })



df6=list(df5)

df7 = pd.DataFrame({
     'id стены':[],
     'индекс активности':[],
     
     
     
 })
df8=list(df7)



df5['id стены']=df3["id стены"].unique()
df7['url комментария']=df3["url комментария"]
print(df5)

for i in range(len(df5[df4[0]])):
    df5.loc[i,df6[1]]=0
    df5.loc[i,df6[3]]=0
    df5.loc[i,df6[4]]=0
    df5.loc[i,df6[5]]=0
    for j in range(len(df3[df4[0]])):
        if df5[df4[0]][i]==df3[df4[0]][j]:
            df5.loc[i,df6[1]]=df5[df6[1]][i]+(1*df3[df4[2]][j])
            df5.loc[i,df6[3]]=df5[df6[3]][i]+df3[df4[3]][j]+df3[df4[4]][j]
            df5.loc[i,df6[4]]=df5[df6[4]][i]+df3[df4[3]][j]+df3[df4[5]][j]
            df5.loc[i,df6[5]]=df3[df4[6]][j]
            print(df5[df6[1]][i])

for i in range(len(df5[df4[0]])):
    df5.loc[i,df6[3]]=df5[df6[3]][i]/df5[df6[5]][i]
    df5.loc[i,df6[4]]=df5[df6[4]][i]/df5[df6[5]][i]
    df5.loc[i,df6[6]]=0
for i in range(len(df5[df4[0]])):
    df5.loc[i,df6[6]]=df5[df6[3]][i]+df5[df6[4]][i]
    
   
print('-------------------------')            
print(df5[df6[3]])
print('-------------------------')            
print(df5[df6[4]])    

print(df5)

t=0
aver1_potential_sours=df5['сумма url'].median()
aver2_count=0
for i in range(len(df5[df4[0]])):
        if df5[df6[1]][i]<=aver1_potential_sours:
            df5.loc[i,df6[2]]=1
        if df5[df6[2]][i]!=1:
            aver2_count= aver2_count+df5[df6[1]][i]
            t=t+1
aver2_potential_sours=aver2_count/t  
for i in range(len(df5[df4[0]])):
        if df5[df6[1]][i]<=aver2_potential_sours and df5[df6[1]][i]>=aver1_potential_sours:
            df5.loc[i,df6[2]]=2
        elif  df5[df6[1]][i]>aver2_potential_sours :
            df5.loc[i,df6[2]]=3
print(df5)



         
print(aver2_potential_sours)

df9 = df5.copy(deep=True)

for i in range(len(df9[df4[0]])):
    if df9[df6[2]][i]==3:
        print('Удаляем страницу', df9[df4[0]][i])
        




    






