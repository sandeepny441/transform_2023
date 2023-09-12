# str to pandas datetime 
pd.to_datetime('2020-01-01')

# date_range
pd.date_range(start='2020-01-01', end='2020-12-31')

# dateTime Index 
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
df['day_of_week'] = df['date'].dt.dayofweek

# Time Diff 
pd.Timestamp('2020-01-02') - pd.Timestamp('2020-01-01')

# Add  days
df['date_plus_20'] = df['date'] + pd.Timedelta(days=20)

# Subtract days
df['date_minus_5'] = df['date'] - pd.Timedelta(days=5)

# Resample 
df.resample('M').mean() 

# Shift
df.shift(1)  # Shifts data down by one period

# diff 
df.diff()  # Finds the difference between a row and the previous row

# rolling 
df.rolling(window=3).mean()  # Calculates the rolling mean over a 3 period window
