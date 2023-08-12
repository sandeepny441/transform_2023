# value counts 
s.value_counts()  
s.unique()
s.nunique()
# missing data 
s.isnull().sum()
s.dropna()
s.fillna(value)
# sorting 
s.sort_values()
s.sort_index()
#data allignment 
s.reindex()
s.reset_index()
# more 
s.drop() # Drop values from rows (axis=0) or columns (axis=1)
#membership 
s.isin(values)
s.drop_duplicates() # Drop duplicate values
s.astype(dtype) # Cast values to dtype
s.replace(val1, val2) # Replace values 
s.rename() # Rename index labels
s.between(val1, val2) # Filter between values
s.clip(lower, upper) # Trim values to range
s.duplicated() # Check for duplicates
s.interpolate() # Fill NaNs by interpolation 
s.expanding(min_periods).mean() # Expanding statistics

# apply functions 
s.apply(func)
s.map(dict)

