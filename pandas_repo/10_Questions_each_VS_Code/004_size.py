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



What does the size function return when applied directly to the pet_stores_df DataFrame?

After grouping the pet_stores_df by 'Location', what is the size of each group?

When using the size function after filtering for stores with an 'Annual_Revenue($1000s)' above 400, what is the result?

If you group the DataFrame by 'Specialty', what is the size of each group?

How would you use the size function to count the number of unique store names in the DataFrame?

======================================================================================================
After creating a pivot table with 'Location' as index and 'Specialty' as columns, what is the size of the resulting DataFrame?

Use the size function to determine the number of stores that have a name starting with the letter 'P'.

When chaining methods, if you filter the DataFrame to show only 'Dogs' specialty and then use size, what number would you get?

How would you employ the size function to determine the number of stores with an 'Annual_Revenue($1000s)' between 300 and 500?

If you were to break down the DataFrame by both 'Location' and 'Specialty' using the groupby method, what would be the size of each subgroup?