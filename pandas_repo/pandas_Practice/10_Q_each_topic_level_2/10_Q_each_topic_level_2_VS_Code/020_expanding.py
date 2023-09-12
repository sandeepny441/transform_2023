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
