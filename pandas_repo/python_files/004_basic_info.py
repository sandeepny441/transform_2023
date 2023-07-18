# basic info
df.shape  # Get the shape of the DataFrame (rows, columns)
df.size  # Get the size of the DataFrame (rows * columns)
df.info()  # Get a summary of the DataFrame
df.describe()  # Get statistical summary of numerical columns
df.index  # Get the index of the DataFrame
df.columns  # Get the column names of the DataFrame
df.values  # Get the values in the DataFrame as a numpy array
df.dtypes  # Get the data types of the columns
df.head()  # Returns the first 5 rows of the DataFrame. 
df.tail()  # Returns the last 5 rows of the DataFrame. .
df.sample(6) # Returns a random sample of 6 rows 
df.count() # Count the non-NaN values in each column
df.unique() # Get unique values in each column