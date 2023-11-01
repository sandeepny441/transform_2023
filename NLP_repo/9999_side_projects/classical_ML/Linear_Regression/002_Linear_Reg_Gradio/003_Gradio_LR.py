import gradio as gr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set the seed for reproducibility
np.random.seed(0)

# Creating the DataFrame
data = {
    'X1': np.random.randint(1, 100, 12),
    'X2': np.random.randint(1, 100, 12),
}
df = pd.DataFrame(data)

# Assuming a linear relation: Y = 2*X1 + 3*X2 + some_noise
df['Y'] = round(2*df['X1'] + 3*df['X2'] + np.random.normal(0, 10, 12))

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['X1', 'X2']], df['Y'], test_size=0.2, random_state=0)

# Creating the model
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, y_train)

def predict_Y_and_plot(X1, X2):
    # Making a prediction
    prediction = model.predict([[X1, X2]])

    # Calculating the line of best fit
    x_range = np.array(sorted(np.concatenate((X_train['X1'].values, X_train['X2'].values))))
    y_range = model.coef_[0] * x_range + model.coef_[1] * x_range + model.intercept_

    # Creating the plot
    plt.title("Linear Regression Demo")  # Added title
    plt.scatter(df['X1'], df['Y'], color='black', label='Training Data')
    plt.scatter(X1, prediction, color='red', marker='x', label='Prediction')
    plt.plot(x_range, y_range, color='blue', label='Line of Best Fit')

    plt.xlabel('Input (X1 & X2)')
    plt.ylabel('Output (Y)')
    plt.legend()
    plt.grid(True)

    # Saving the plot to a file
    plt.savefig('prediction_plot.png')
    plt.close()

    return round(prediction[0]), 'prediction_plot.png'


# Creating the Gradio interface
iface = gr.Interface(
    fn=predict_Y_and_plot,  # function to call
    inputs=["number", "number"],  # input types
    outputs=["number", "image"],  # output types
    live=True,  # update the output while changing inputs
    title="Linear Regression Demo"  # Setting the title for the Gradio interface
)

# Launching the interface
iface.launch(share=True)
