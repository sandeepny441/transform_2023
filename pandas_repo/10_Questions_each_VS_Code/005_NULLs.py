data = {
'Product_ID': [1, 2, 3, 4, 5, np.nan],
'Product_Name': ['Laptop', 'Phone', 'TV', 'Headphones', None, 'Microwave'],
'Stock': [20, 15, np.nan, 30, 25, 12],
'Price': [999.99, 799.99, 399.99, np.nan, 59.99, 99.99],
'Discounted': [True, False, True, False, np.nan, True],
}

target_df = pd.DataFrame(data)

NULLs

Identify Null values
How would you identify rows where the 'Stock' column has null values in the provided target_df DataFrame?
Can you list the columns in target_df that contain at least one null value?
How would you use pd.isna() to identify null values in the entire target_df DataFrame?
If you wanted to identify rows where both 'Stock' and 'Price' have null values, how would you do it?

Filtering
How would you filter out rows where the 'Stock' column has null values in the target_df DataFrame?
What method would you use to remove any row that has at least one null value in target_df?
If you only want to drop rows where both 'Stock' and 'Price' have null values, how would you go about doing this in target_df?

Filling
How would you fill null values in the 'Stock' column with the median value of that column?
Can you use the .fillna() method to fill null values in multiple columns ('Stock' and 'Price') at once? If so, how?
If you only want to fill the first null value in each column with a zero, how would you do it?

Counting
How would you count the number of null values in the entire DataFrame?
Is there a way to get a count of non-null values for each column in the DataFrame?
How would you count null values in a specific row, say the row at index 2?

Replacing
If you wanted to replace all null values in the DataFrame with the string "Unknown", how would you do it?
Can you replace null values in one column ('Stock') with zero and in another column ('Discounted') with False, all in a single line of code?
How would you replace all instances of a specific value, let's say 999.99 in the 'Price' column, with np.nan?

Operations
How would you calculate the sum of each column in target_df, considering that some columns might have null values?
If you have null values in the 'Stock' and 'Price' columns, and you attempt to multiply these columns element-wise, what will happen to the resulting product where null values are involved?
How would you use the dropna method to perform an operation, say calculating the mean, only on non-null elements in the 'Stock' column?

Propagating
How would you propagate the last valid observation in the 'Stock' column to fill NaN values?
Can you propagate the next valid observation backward to fill NaN values in the 'Price' column? If so, how would you do it?
How would you limit the number of NaN values filled by forward fill (or backward fill) to 1 in the 'Stock' column