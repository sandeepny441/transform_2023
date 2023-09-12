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

If you had a column in coffee_shops_df that contained lists of coffee varieties offered, how would you use explode to create a separate row for each coffee type?
How does the index behave when you use the explode method on a DataFrame?
Can you use the explode method on columns with non-list data types?
How would you handle columns with mixed data, some rows having lists and others having single values, when using explode?
What happens to the other columns in the DataFrame when you explode a specific column?
How does the explode method compare to the melt method?
In what scenarios might you prefer to use explode over manually splitting and stacking data?