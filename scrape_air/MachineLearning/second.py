import pandas as pd
import matplotlib.pyplot as plt

# Function to load data from a single JSON file
def load_data_from_json(file_path):
    df = pd.read_json(file_path)
    # Convert price to a numeric value after removing commas
    df['Price'] = df['Price'].str.replace(',', '').astype(float)
    return df

# Assuming you have a list of file paths for each day
json_files = [
    '../ml_jsons/Day_1.json',
    '../ml_jsons/Day_2.json',
    # Add more files as needed
]

# Load data and find minimum-priced flights for each day
min_price_flights = []
for day, file in enumerate(json_files, start=1):
    df = load_data_from_json(file)
    min_price_flight = df.loc[df['Price'].idxmin()]
    min_price_flight['Day'] = day
    min_price_flights.append(min_price_flight)

# Convert the list to a DataFrame
min_price_flights_df = pd.DataFrame(min_price_flights)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(min_price_flights_df['Day'].astype(str), min_price_flights_df['Price'], color='skyblue')
plt.xlabel('Day')
plt.ylabel('Lowest Price')
plt.title('Lowest Flight Price by Day')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
