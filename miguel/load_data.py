import sqlite3
import pandas as pd

conn = sqlite3.connect('db/adult.db')

read_adults = pd.read_csv(r'db/adult.csv', skipinitialspace=True)
#print(read_adults)
table= 'ADULT'
read_adults.to_sql(table, conn, if_exists='replace', index = False)
