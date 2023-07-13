import pandas as pd
import numpy as np
import sqlite3

# From a Dictionary of equal-length lists
data1 = {'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]}
df1 = pd.DataFrame(data1)

# From a Dictionary of Series
data2 = {'col1': pd.Series([1, 2, 3]), 'col2': pd.Series([4, 5, 6])}
df2 = pd.DataFrame(data2)

# From a List of Dictionaries
data3 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df3 = pd.DataFrame(data3)

# From a List of Lists (like a 2D array)
data4 = [[1, 2, 3], [4, 5, 6]]
df4 = pd.DataFrame(data4, columns=['a', 'b', 'c'])


# From a List of Lists (like a 2D array) with Index
data4 = [[1, 2, 3], [4, 5, 6]]
df4 = pd.DataFrame(data4, columns=['a', 'b', 'c'], index=['row1', 'row2'])

# From a NumPy array
data5 = np.array([[1, 2, 3], [4, 5, 6]])
df5 = pd.DataFrame(data5, columns=['a', 'b', 'c'])

# From a CSV file (you need a real CSV file for this to work)
df6 = pd.read_csv('filename.csv')

# From an Excel file (you need a real Excel file for this to work)
df7 = pd.read_excel('filename.xlsx')

# From a SQL query (you need a real SQLite database for this to work)
conn = sqlite3.connect('database.db')
df8 = pd.read_sql_query("SELECT * FROM tablename", conn)
