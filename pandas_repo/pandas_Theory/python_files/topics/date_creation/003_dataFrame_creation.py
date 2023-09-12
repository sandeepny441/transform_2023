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


# create a dictionary and use all methods 
# to create a dataframe
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df = pd.DataFrame(data)
print(df)
# create a fucntion to check if a number is prime 
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True 
# create a list of prime numbers
prime_numbers = []    
for i in range(100):
    if is_prime(i):
        prime_numbers.append(i) 
# create a dictionary of prime numbers
data = {'Prime Numbers': prime_numbers}
# create a dataframe from the dictionary
df = pd.DataFrame(data)
print(df)
# create a list of lists

data = [['tom', 10], ['nick', 15], ['juli', 14]]
# create a dataframe from the list of lists
df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df)
# create a list of dictionaries
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# create a dataframe from the list of dictionaries
df = pd.DataFrame(data)
print(df)
# create a list of tuples
data = [('tom', 10), ('nick', 15), ('juli', 14)]
# create a dataframe from the list of tuples

df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df)
# create a list of tuples
data = [('tom', 10), ('nick', 15), ('juli', 14)]
# create a dataframe from the list of tuples
df = pd.DataFrame(data, columns = ['Name', 'Age'], dtype = float)
print(df)
# create a list of tuples

data = [('tom', 10), ('nick', 15), ('juli', 14)]
# create a dataframe from the list of tuples
df = pd.DataFrame(data, columns = ['Name', 'Age'], dtype = float, index=['rank1','rank2','rank3'])
print(df)
# create a list of tuples
data = [('tom', 10), ('nick', 15), ('juli', 14)]
# create a dataframe from the list of tuples
df = pd.DataFrame(data, columns = ['Name', 'Age'], dtype = float, index=['rank1','rank2','rank3'])
print(df)
# create a list of tuples
data = [('tom', 10), ('nick', 15), ('juli', 14)]
# create a dataframe from the list of tuples
df = pd.DataFrame(data, columns = ['Name', 'Age'], dtype = float, index=['rank1','rank2','rank3'])

print(df)
# create a list of tuples
data = [('tom', 10), ('nick', 15), ('juli', 14)]
# create a dataframe from the list of tuples
df = pd.DataFrame(data, columns = ['Name', 'Age'], dtype = float, index=['rank1','rank2','rank3'])


print('Hello world')