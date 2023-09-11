import pandas as pd

data = {
    'Coffee_Shop': ['Brewed Awakening', 'Coffee Cloud', 'Bean Dream', 'Espresso Express', 'Latte Love', 
                    'Mocha Magic', 'Cafe Comfort', 'Seattle Sip', 'Drip Drop', 'Grind Ground'],
    'Location': ['Downtown', 'Capitol Hill', 'Green Lake', 'Ballard', 'West Seattle', 
                 'Fremont', 'Queen Anne', 'Belltown', 'University District', 'Magnolia'],
    'Avg_Rating': [4.5, 4.2, 5.0, 4.8, 4.6, 4.3, 4.9, 4.0, 4.7, 4.6],
    'Coffee_Type': ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Cold Brew', 
                   'Macchiato', 'Espresso', 'Latte', 'Drip Coffee', 'Americano'],
    'Tables_Available': [5, 8, 6, 7, 5, 9, 7, 8, 6, 5]
}

coffee_shops_df = pd.DataFrame(data)


How would you use the between method to filter rows from the coffee_shops_df where Avg_Rating is between 4.5 and 5.0, inclusive?
Which coffee shops from the DataFrame are located in areas between 'Ballard' and 'Fremont' alphabetically using the between method?
How can you use the between method to identify coffee shops that have between 5 and 7 tables available?
Is there a way to use the between method with dates? If so, how?
 Given a DataFrame df with a column 'Names', how would you filter rows where the name length is between 3 and 7 characters using the between method?
 If coffee_shops_df has a 'Barista' column with names of baristas, how would you use between to select only the rows where the barista's name length is between 4 and 8 characters?
 Considering a 'Comments' column in df that contains customer feedback, how would you retrieve rows where the comment length is between 10 and 100 characters?
In coffee_shops_df, if there's a 'Ratings' column, how would you use between with loc to replace all ratings between 2 and 4 (inclusive) with a string "Average"?
 Given a column 'Prices' in df, how would you use loc combined with between to increase the price by 10% for all products priced between $5 and $20?
 What advantage does using between provide over using relational operators (&, |) when filtering rows in df with 'Age' values between 25 and 30?
 Given a 'Temperature' column in df, how would you filter rows where the temperature is between 20°C and 25°C using both the between method and relational operators for comparison?