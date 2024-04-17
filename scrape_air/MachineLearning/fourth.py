import pandas as pd
import plotly.express as px

# Function to load and clean data from a JSON file
def load_and_clean_data(file_path):
    df = pd.read_json(file_path)
    df['Price'] = df['Price'].str.replace(',', '').astype(float)
    return df

# List of JSON file paths - Replace these with your actual file paths
json_files = [
    '../ml_jsons/Day_1.json',
    '../ml_jsons/Day_2.json',
    '../ml_jsons/Day_3.json',
    '../ml_jsons/Day_4.json',
]

# Load and concatenate all flight data into a single DataFrame
all_flights_data = pd.concat([load_and_clean_data(file) for file in json_files])

# Group by 'Flight Unique Number' to find the minimum price for each unique flight
min_price_per_flight = all_flights_data.groupby('Flight Unique Number', as_index=False)['Price'].min()

# Sorting the results by price for better visualization
min_price_per_flight_sorted = min_price_per_flight.sort_values(by='Price')

# Using Plotly to create an interactive bar chart
fig = px.bar(min_price_per_flight_sorted, x='Flight Unique Number', y='Price',
             hover_data=['Flight Unique Number', 'Price'],
             labels={'Price': 'Lowest Price', 'Flight Unique Number': 'Flight Unique Number'},
             title='Lowest Price for Each Unique Flight Number')

fig.update_layout(xaxis={'categoryorder':'total descending'}, xaxis_title='Flight Unique Number',
                  yaxis_title='Lowest Price', title_x=0.5)

# Show plot
fig.show()
