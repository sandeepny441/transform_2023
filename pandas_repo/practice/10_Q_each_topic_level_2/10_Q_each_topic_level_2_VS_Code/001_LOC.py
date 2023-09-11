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

#LOC questions
How would you use the loc method to select all the details of the store with Store_ID 103?

Using loc, how can you extract the Specialty and Annual_Revenue($1000s) columns for stores located in 'Los Angeles' or 'Houston'?

If you wanted to change the Specialty of the store with Store_ID 105 to 'All Pets', how would you achieve this using the loc method?

How would you filter out stores using loc that have an Annual_Revenue($1000s) of more than 400?

Using the loc method, how can you retrieve the Store_Name and Location for the last two rows in the DataFrame?

-----------------------------------------------------------------------------------------------------------------------------

How would you use loc to filter rows where the Type is 'Aquatic'?

Using loc, how would you modify the Stock count for the store named 'PetLovers'?

How can you retrieve the Location and Stock columns for stores named 'PetWorld' and 'AquaBuddies' using the loc method?

If you wanted to see all details for stores located in 'New York', how would you use the loc function?

Using loc, how would you select all rows up to (and including) the store 'PetLovers' and only retrieve the columns from Type to Stock?

-----------------------------------------------------------------------------------------------------------------------------

