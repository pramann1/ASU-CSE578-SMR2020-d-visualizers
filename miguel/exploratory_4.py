import sqlite3
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect('db/adult.db')
cur = conn.cursor()

data = []
qry = ('SELECT age, education, education_num, hours_per_week '
       'FROM ADULT')
cur.execute(qry)
rs = cur.fetchall()
for r in rs:
    row = []
    row.append(r[0])
    row.append(r[1])
    row.append(r[2])
    row.append(r[3])
    data.append(row)

#print(data)
df = pd.DataFrame(data, columns=['Age', 'Education', 'Education-Num', 'Hours-Per-Week'])
#print(df)

sns.set(style="whitegrid", font_scale=0.6)
#sns.catplot(x='Education-Num', y='Hours-Per-Week', hue='Education', data=df)
sns.catplot(x='Education-Num', y='Age', hue='Education', data=df)

plt.show()