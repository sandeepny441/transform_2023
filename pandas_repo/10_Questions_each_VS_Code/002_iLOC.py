import pandas as pd

# Sample data for pet stores in the US
data = {
    'Store_ID': [101, 102, 103, 104, 105],
    'Store_Name': ['Paws and Play', 'Pet Paradise', 'Whisker Wonders', 'Fin & Feather', 'Bark & Purr'],
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Specialty': ['Dogs', 'Cats', 'Fish', 'Birds', 'Reptiles'],
    'Annual_Revenue($1000s)': [500, 400, 300, 450, 320]
}

# Create DataFrame
pet_stores_df = pd.DataFrame(data)

pet_stores_df


#iLOC questions
How would you use the iloc method to select the details of the third store in the DataFrame?

Using iloc, how would you extract the Specialty and Annual_Revenue($1000s) columns for the first and fourth stores?

If you wanted to change the Annual_Revenue($1000s) of the last store in the DataFrame to 400, how would you achieve this using the iloc method?

How would you retrieve details of the first, third, and fifth stores in the DataFrame using iloc?

Using the iloc method, how can you retrieve details for all stores, but only for the columns Store_Name and Location?

-----------------------------------------------------------------------------------------------------------------------------

How would you extract details for the second to fifth stores using iloc?

If you wanted to change the Location of the second store to 'Los Angeles', how would you use the iloc method to achieve this?

How would you use iloc to get details from the third column for all stores?

Using iloc, how can you retrieve the details of the stores from index 3 to index 7 (inclusive)?

Imagine you want to select every alternate store's details from the DataFrame. How would you use iloc to achieve this?

-----------------------------------------------------------------------------------------------------------------------------

