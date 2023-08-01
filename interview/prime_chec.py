# pandas groupby to select city with top 5  salaries

import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
df = df.dropna()
df = df[df['Salary or Hourly'] == 'Salary']
df = df.groupby('Department')['Annual Salary'].mean()
df = df.sort_values(ascending=False)
df = df.head(5)
print(df)

#program to find the most common words in a sentence
# Path: most_common_words.py


def most_common_words(text):
    text = text.split()
    d = {}
    for word in text:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d
  
