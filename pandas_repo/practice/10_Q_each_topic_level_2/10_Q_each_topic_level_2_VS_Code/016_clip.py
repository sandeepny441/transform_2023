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


How would you use the clip method to ensure that all Avg_Rating values in the coffee_shops_df are between 4.0 and 4.5?
If you wanted to clip only the lower bound of Tables_Available to 6 without changing the upper values, how would you do it?
What happens to the original DataFrame after using the clip method? Is it modified in place or do you get a new DataFrame?
Can the clip method be applied to string data in a DataFrame?
How would you clip all numerical columns in a DataFrame at once?
What's the difference between using the clip method and using conditional statements to limit data range?
Why might you use the clip method in data preprocessing?