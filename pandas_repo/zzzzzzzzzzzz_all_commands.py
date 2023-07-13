df = pd.read_csv('file.csv')  # Load data from a CSV file
df = pd.read_excel('file.xlsx')  # Load data from an Excel file
df = pd.read_html('http://www.example.com')  # Load data from a HTML file or URL

#series methods
s.value_counts()  # Count the number of occurrences of each unique value in the Series
s.unique()  # Get the unique values in the Series
s.nunique()  # Get the number of unique values in the Series
s.isnull().sum()  # Get the number of missing values in the Series
s.dropna()  # Drop missing values in the Series
s.fillna(value)  # Fill missing values in the Series with a specified value
s.apply(function)  # Apply a function to each value in the Series
s.map(dict)  # Replace values in the Series based on a dictionary
s.sort_values()  # Sort the Series


#basic info
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



#missing values 
df['A'].isnull()  # Check if values in column 'A' are missing
df['A'].isna()  # Same as isnull()
df['A'].isnull().sum()  # Get the count of missing values in column 'A'
df.isnull().sum().sum()  # Get the total count of missing values in the DataFrame
df['A'].dropna()  # Drop the missing values in column 'A'
df.dropna()  # Drop rows with any column having NA/null data
df.dropna(axis=1) #Drop columns with any missing values
df.drop(how = 'any')
df.drop(how = 'all')
df.drop(how = '0.4')
df.fillna(fill_with_this_value)  # Replace all NA/null data with a specified value
df.fillna(df.mean())
df.fillna(method='ffill')
df.fillna(method='bfill')
df.isnull().sum() #Summarize number of missing values in each column
df.memory_usage() #Get memory usage of DataFrame
df.min()/df.max() #Get minimum and maximum values in each column




