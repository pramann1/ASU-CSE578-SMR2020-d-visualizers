import sqlite3
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect('db/adult.db')
cur = conn.cursor()

countries = []
qry = ('SELECT DISTINCT native_country '
      'FROM ADULT '
      'ORDER BY native_country ASC')
cur.execute(qry)
rs = cur.fetchall()
for r in rs:
    countries.append(r[0])
#print(countries)

education = []
qry = ('SELECT DISTINCT education '
      'FROM ADULT '
      'ORDER BY education_num ASC')
cur.execute(qry)
rs = cur.fetchall()
for r in rs:
    education.append(r[0])
#print(education)
#Withouth Bachelors -> 12
#Bachelor -> 13
#Graduate -> 13
education_level = [-1, 0, 1]
dic_e = {}
for e in education_level:
    dic_c = {}
    for c in countries:
        if c != 'United-States':
            if e == -1:
                qry = ('SELECT count(*) counter '
                    'FROM ADULT '
                    'WHERE education_num<\'{e}\' '
                    'AND native_country=\'{c}\''.format(e=13,c=c))
                cur.execute(qry)
                rs = cur.fetchall()
                for r in rs:
                    dic_c[c] = r[0]
                dic_e['Withouth_Bachelor'] = dic_c
            elif e == 0:
                qry = ('SELECT count(*) counter '
                    'FROM ADULT '
                    'WHERE education_num=\'{e}\' '
                    'AND native_country=\'{c}\''.format(e=13,c=c))
                cur.execute(qry)
                rs = cur.fetchall()
                for r in rs:
                    dic_c[c] = r[0]
                dic_e['Bachelor'] = dic_c
            else:
                qry = ('SELECT count(*) counter '
                    'FROM ADULT '
                    'WHERE education_num>\'{e}\' '
                    'AND native_country=\'{c}\''.format(e=13,c=c))
                cur.execute(qry)
                rs = cur.fetchall()
                for r in rs:
                    dic_c[c] = r[0]
                dic_e['Graduate'] = dic_c

list_b = []
for country, counter in dic_e['Bachelor'].items():
    #print(country)
    list_i = []
    list_i.append(country)
    counter_2 = dic_e.get('Withouth_Bachelor').get(country, 0)
    list_i.append(counter_2)
    #print(counter_2)
    list_i.append(counter)
    #print(counter)
    counter_3 = dic_e.get('Graduate').get(country, 0)
    list_i.append(counter_3)
    #print(counter_3)
    counter_4 = counter + counter_2 + counter_3
    list_i.append(counter_4)
    list_b.append(list_i)

#print(list_b)
df = pd.DataFrame(list_b, columns=['Country', 'Withouth-Bachelor', 'Bachelor', 'Graduate', 'Total'])
print(df)

#normalize
x = df[['Total']].values.astype(float)
#print(x)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df['Normalized_Total'] = x_scaled
#print(df)


sns.set(style="whitegrid", font_scale=0.6)
f, ax = plt.subplots(figsize=(12, 6))

sns.set_color_codes("pastel")
sns.barplot(x="Total", y="Country", data=df, label="Total", color="b")

sns.set_color_codes("muted")
#sns.barplot(x="Withouth-Bachelor", y="Country", data=df, label="Withouth-Bachelor", color="b")
#sns.barplot(x="Bachelor", y="Country", data=df, label="Bachelor", color="b")
sns.barplot(x="Graduate", y="Country", data=df, label="Graduate", color="b")

ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlabel="Total, Native Country: No USA")
sns.despine(left=True, bottom=True)

plt.show()
