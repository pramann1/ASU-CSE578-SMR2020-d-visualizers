import sqlite3

conn = sqlite3.connect('db/adult.db')
cur = conn.cursor()

table = ('CREATE TABLE ADULT '
        '( '
        'id INTEGER PRIMARY KEY, '
        'age INTEGER, '
        'workclass TEXT, '
        'fnlwgt INTEGER, '
        'education TEXT, '
        'education_num INTEGER, '
        'marital_status TEXT, '
        'occupation TEXT, '
        'relationship TEXT, '
        'race TEXT, '
        'sex TEXT, '
        'capital_gain INTEGER, '
        'capital_loss INTEGER, '
        'hours_per_week INTEGER, '
        'native_country TEXT, '
        'class_type TEXT '
        ')'
        )
print(table)

cur.execute(table)
conn.commit()