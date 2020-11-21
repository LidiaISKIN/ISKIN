import numpy as np
import pandas as pd

# df3 = pd.DataFrame({
#      'id стены': ['маша','саша','маша','дима','дима','дима','маша','наташа','маша','саша','маша','наташа'],
#      'url комментария':[5,6,2,4,12,13,14,15,16,17,18,19],
#      'type':[1,2,3,2,3,1,2,1,1,3,3,1],
#      'кол-во лайков':[300,10,1000,500,600,30,50,290,890,50,10,0],
#      'кол-во коментов':[2,1,3,4,2,5,7,10,100,300,600,0,],
#      'кол-во просмотров':[500,600,1202,3000,50,80,6700,5980,3450,2340,2350,5460],
#      'число друзей':[100,200,100,100,100,100,100,100,100,100,100,100]
#
#
#  })
df3 = pd.read_excel('Исходник.xlsx')
print(df3)
df4=list(df3)
#df3 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=df4)
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
            df5.loc[i,df6[1]]=df5[df6[1]][i]+(1)+(1*df3[df4[2]][j])
            print('df5[df6[1]][i]=',df5[df6[1]][i],'i=',i,'df3[df4[2]][j]=',df3[df4[2]][j])
            df5.loc[i,df6[3]]=df5[df6[3]][i]+df3[df4[3]][j]+df3[df4[4]][j]
            df5.loc[i,df6[4]]=df5[df6[4]][i]+df3[df4[3]][j]+df3[df4[5]][j]
            df5.loc[i,df6[5]]=df3[df4[6]][j]


for i in range(len(df5[df4[0]])):
    df5.loc[i,df6[3]]=df5[df6[3]][i]/df5[df6[5]][i]
    df5.loc[i,df6[4]]=df5[df6[4]][i]/df5[df6[5]][i]
    df5.loc[i,df6[6]]=0
for i in range(len(df5[df4[0]])):
    df5.loc[i,df6[6]]=df5[df6[3]][i]+df5[df6[4]][i]




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


df5.to_csv('filo_3.csv')
df11, df10 = [x for _, x in df5.groupby(df5['potential_sours'] < 3)]
#df11 - это те кто больше 3 потенциал
df11.to_csv('filo_3.csv')


df12, df13 = [x for _, x in df10.groupby(df10['potential_sours'] < 2)]
#df13 - это те кто меньше 2 потенциал
df13.to_csv('filo_1.csv')
df12.sort_values('индекс влиятельности',ascending=False).iloc[:10].to_csv('filo_top2.csv')



df14=pd.DataFrame({
    'Объект воздействия':[],
    'Адрес воздействия':[],
    'potential_sours':[],
    'кол-во сообщений':[]


})





df11.reset_index(inplace=True)
df12.reset_index(inplace=True)
df13.reset_index(inplace=True)
t=0

for i in range(len(df11['id стены'])):
    df14.loc[i,'Адрес воздействия']=df11['id стены'][i]
    df14.loc[i,'potential_sours']=df11['potential_sours'][i]
    df14.loc[i,'Объект воздействия']='стена'
    t=t+1


d=0



for i in range(len(df3['id стены'])):
    for j in range(len (df12['potential_sours'])):
        if df3['id стены'][i]==df12['id стены'][j]:
            if i <=10:
                df14.loc[i+t,'Адрес воздействия']=df12['id стены'][j]
                df14.loc[i+t,'potential_sours']=df12['potential_sours'][i]
                df14.loc[i+t,'Объект воздействия']='стена'
                d=d+1

for i in range(len(df14['Адрес воздействия'])):
    df14.loc[i,'кол-во сообщений']=0
    for j in range(len(df3['id стены'])):
        if df14['Адрес воздействия'][i]==df3['id стены'][j]:
            df14.loc[i,'кол-во сообщений']=df14['кол-во сообщений'][i]+1

e=0
for i in range(len(df3['id стены'])):
    for j in range(len (df12['potential_sours'])):
        if df3['id стены'][i]==df12['id стены'][j]:
            if i>10:
                df14.loc[i+t+d, 'Адрес воздействия'] = df3['url комментария'][i]
                df14.loc[i+t+d, 'potential_sours'] = df12['potential_sours'][j]
                df14.loc[i + t + d, 'кол-во сообщений'] = 1
                df14.loc[i+t+d, 'Объект воздействия'] = 'сообщение'
                e=e+1

for i in range(len(df3['id стены'])):
    for j in range(len (df13['potential_sours'])):
        if df3['id стены'][i] == df13['id стены'][j]:
            df14.loc[i+t+d+e, 'Адрес воздействия'] = df3['url комментария'][i]
            df14.loc[i + t + d+e, 'кол-во сообщений'] = 1
            df14.loc[i + t + d+e, 'potential_sours'] = df13['potential_sours'][j]
            df14.loc[i+t+d+e, 'Объект воздействия'] = 'сообщение'




print(df14)

df14.sort_values('potential_sours',ascending=False).to_csv('улы.csv')







