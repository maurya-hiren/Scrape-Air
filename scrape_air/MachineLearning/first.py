import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt

# Example function to load and prepare the data
def load_and_prepare_data(json_files):
    all_data = pd.DataFrame()
    for day, file in enumerate(json_files, start=1):
        df = pd.read_json(file)
        df['Day'] = day
        all_data = pd.concat([all_data, df], ignore_index=True)
    all_data['Price'] = all_data['Price'].str.replace(',', '').astype(float)
    return all_data

# Replace 'json_files' with the list of your JSON files paths
json_files = ['../ml_jsons/Day_1.json', '../ml_jsons/Day_2.json'] # Update this list
data = load_and_prepare_data(json_files)

# Simplified Feature Engineering: Using only numeric columns and 'Day' as features for demonstration
X = data[['Day', 'Price']]  # Assuming 'Day' and 'Price' are the only numeric columns
y = data['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate the model
predictions = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, predictions))

print(f"RMSE: {rmse}")

# Note: This is a very basic example. Real-world scenarios require more detailed feature engineering,
# model selection, and evaluation.
