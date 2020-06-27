import sqlite3
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect('db/adult.db')
cur = conn.cursor()

education_level = [-1, 0, 1]
dic_e = {}
for e in education_level:
    dic_c = {}
    if e == -1:
        qry = ('SELECT count(*) counter '
            'FROM ADULT '
            'WHERE education_num<\'{e}\' '
            'AND native_country=\'{c}\''.format(e=13,c='United-States'))
        cur.execute(qry)
        rs = cur.fetchall()
        for r in rs:
            dic_c['United-States'] = r[0]
        dic_e['Withouth_Bachelor'] = dic_c
    elif e == 0:
        qry = ('SELECT count(*) counter '
            'FROM ADULT '
            'WHERE education_num=\'{e}\' '
            'AND native_country=\'{c}\''.format(e=13,c='United-States'))
        cur.execute(qry)
        rs = cur.fetchall()
        for r in rs:
            dic_c['United-States'] = r[0]
        dic_e['Bachelor'] = dic_c
    else:
        qry = ('SELECT count(*) counter '
            'FROM ADULT '
            'WHERE education_num>\'{e}\' '
            'AND native_country=\'{c}\''.format(e=13,c='United-States'))
        cur.execute(qry)
        rs = cur.fetchall()
        for r in rs:
            dic_c['United-States'] = r[0]
        dic_e['Graduate'] = dic_c

list_1 = []
list_1.append('Withouth_Bachelor')
list_1.append('Bachelor')
list_1.append('Graduate')
list_2 = []
counter = dic_e.get('Bachelor').get('United-States', 0)
counter_2 = dic_e.get('Withouth_Bachelor').get('United-States', 0)
counter_3 = dic_e.get('Graduate').get('United-States', 0)
list_2.append(counter_2)
list_2.append(counter)
list_2.append(counter_3)

df = pd.DataFrame(list(zip(list_1, list_2)), columns=['Education-Level', 'Count'])
print(df)

sns.set(style="whitegrid", font_scale=0.6)
f, ax = plt.subplots(figsize=(8, 6))

sns.set_color_codes("muted")
sns.barplot(x="Education-Level", y="Count", data=df)

ax.set(xlabel="Native Country: USA", ylabel='Count')

plt.show()