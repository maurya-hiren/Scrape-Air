import pandas as pd
import matplotlib.pyplot as plt

# Function to load and clean data from a JSON file
def load_and_clean_data(file_path):
    df = pd.read_json(file_path)
    # Remove commas from the 'Price' field and convert it to a float
    df['Price'] = df['Price'].str.replace(',', '').astype(float)
    return df

# List of JSON file paths - Replace these with your actual file paths
json_files = [
    '../ml_jsons/Day_1.json',
    '../ml_jsons/Day_2.json',
    # Add other file paths as needed
]

# Load and concatenate all flight data into a single DataFrame
all_flights_data = pd.concat([load_and_clean_data(file) for file in json_files])

# Group by 'Flight Unique Number' to find the minimum price for each unique flight
min_price_per_flight = all_flights_data.groupby('Flight Unique Number')['Price'].min().reset_index()

# Sorting the results by price for better visualization
min_price_per_flight_sorted = min_price_per_flight.sort_values(by='Price')

# Plotting
plt.figure(figsize=(20, 10))  # Adjust the size as necessary to accommodate all flight numbers
plt.bar(min_price_per_flight_sorted['Flight Unique Number'], min_price_per_flight_sorted['Price'], color='skyblue')
plt.xlabel('Flight Unique Number', fontsize=14)
plt.ylabel('Lowest Price', fontsize=14)
plt.title('Lowest Price for Each Unique Flight Number', fontsize=16)
plt.xticks(rotation=90)  # Rotate the labels to make them readable
plt.tight_layout()  # Adjust subplots to fit into the figure area.
plt.show()
