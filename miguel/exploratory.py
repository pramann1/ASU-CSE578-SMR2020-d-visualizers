import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np


conn = sqlite3.connect('db/adult.db')
cur = conn.cursor()

#qry = 'PRAGMA table_info(ADULT)'
#cur.execute(qry)
#rs = cur.fetchall()
#print(rs)

#qry = 'SELECT * FROM ADULT'
#cur.execute(qry)
#rs = cur.fetchall()
#for r in rs:
#    print(r)

qry = ('SELECT sex, count(*) counter '
       'FROM ADULT '
       'GROUP BY sex')
cur.execute(qry)
rs = cur.fetchall()
#for r in rs:
#    print(r)

df = pd.DataFrame.from_records(rs, columns=['sex', 'counter'])

plt.pie(df['counter'], labels=df['sex'], autopct='%1.1f%%', shadow=False)
plt.title('Sex Pie Chart')
plt.axis('equal')
plt.show()

#rolls = [random.randrange(1,7) for i in range(6000000)]
#values, frequencies = np.unique(rolls, return_counts=True)
#title = f'Folling a Six-Sided Die {len(rolls):,} Times'
#axes = sns.barplot(x=values, y=frequencies, palette='bright')
#plt.show()