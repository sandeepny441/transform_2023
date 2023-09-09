import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load data
df = pd.read_csv('data.csv')

# Split data into features and target variable
X = df[['Month']]
y = df['Sales']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)


# Save the trained model as a .pkl file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# # Make predictions for the next month (Month 12)
# next_month = 12
# predicted_sales = model.predict([[next_month]])

# print(f"Predicted sales for month {next_month}: {predicted_sales[0]}")

# # Visualizing the training set results
# plt.scatter(X_train, y_train, color='red')
# plt.plot(X_train, model.predict(X_train), color='blue')
# plt.title('Sales vs Month (Training set)')
# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.show()
