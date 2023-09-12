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

