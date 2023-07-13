# Selecting a single row:
print(df.iloc[0])  # Selects the first row by integer index

# Selecting a range of rows:
print(df.iloc[1:5])  # Selects rows 2 through 5 (end index is exclusive)

# Selecting a single column:
print(df.iloc[:, 0])  # Selects the first column by integer index

# Selecting multiple columns:
print(df.iloc[:, [0, 1]])  # Selects the first and second columns by integer index

# Setting the value of a single cell:
df.iloc[1, 0] = 120  # Sets the value of the cell at the 2nd row and 1st column

# Setting the value of a range of cells:
df.iloc[0:2, 0] = 5  # Sets the value of the cells in the first column and first three rows

# Print the dataframe to check changes
print(df)
