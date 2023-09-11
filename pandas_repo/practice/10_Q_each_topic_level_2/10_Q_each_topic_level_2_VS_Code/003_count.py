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

===========================================================================

How many pet stores are there in the given DataFrame?

How many unique locations are represented in the dataset? (Hint: Consider combining nunique with count for this)

Using the count function, can you identify if there are any missing values in the 'Specialty' column of the dataset?

After grouping by 'Location', how many stores are listed for each location?

How many pet stores have an 'Annual_Revenue($1000s)' value listed in the DataFrame?

===========================================================================


If you filter the DataFrame to only include stores with an 'Annual_Revenue($1000s)' above 400, how many stores meet this criterion?

How many stores have a specialty other than 'Dogs' or 'Cats'? (You might want to use a combination of boolean indexing and count)

How many stores in the DataFrame have a name that contains the word "Pet"?

After grouping by 'Specialty', how many stores can be counted for each type of pet specialty?

How many of the stores are located either in 'New York' or 'Los Angeles'?