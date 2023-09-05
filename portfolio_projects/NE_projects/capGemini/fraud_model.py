import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Generate synthetic data
n = 1000  # Number of transactions

# Generate transaction IDs
transaction_ids = np.arange(1, n + 1)

# Generate random amounts between 1 and 1000
amounts = np.random.randint(1, 1001, n)

# Generate random sender and receiver IDs
senders = np.random.randint(1, 101, n)
receivers = np.random.randint(1, 101, n)

# Generate random timestamps
timestamps = pd.date_range(start='2021-01-01', end='2021-12-31', periods=n)

# Generate account creation dates (for the sake of this example, we'll assume the same for sender and receiver)
account_creation_dates = pd.date_range(start='2020-01-01', end='2020-12-31', periods=n)

# Generate user profile data: Age (20-60), Location (1-5 as different regions), Employment (0-unemployed, 1-employed)
ages = np.random.randint(20, 61, n)
locations = np.random.randint(1, 6, n)
employments = np.random.randint(0, 2, n)

# Create the data frame
df = pd.DataFrame({
    'Transaction_ID': transaction_ids,
    'Amount': amounts,
    'Sender': senders,
    'Receiver': receivers,
    'Timestamp': timestamps,
    'Account_Creation_Date': account_creation_dates,
    'Age': ages,
    'Location': locations,
    'Employment': employments,
})

# Introduce some fraudulent transactions (for the sake of this example, we'll flag transactions over 900 as fraudulent)
df['Is_Fraud'] = (df['Amount'] > 900).astype(int)


print(df)