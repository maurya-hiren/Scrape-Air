import pandas as pd
import plotly.express as px

# Updated function to load, clean data, and add a column for the file name/identifier
def load_and_clean_data(file_path, identifier):
    df = pd.read_json(file_path)
    df['Price'] = df['Price'].str.replace(',', '').astype(float)
    df['Source'] = identifier  # Add a column with the identifier (e.g., Day_1)
    return df

# List of JSON file paths and their corresponding identifiers
json_files_with_identifiers = [
      
    ('../ml_jsons/Day_1.json', 'Day 1'),
    ('../ml_jsons/Day_2.json', 'Day 2'),
    ('../ml_jsons/Day_3.json', 'Day 3'),
    ('../ml_jsons/Day_4.json', 'Day 4'),
    # ('/path/to/your/day2.json', 'Day_2'),
    # Add other file paths and identifiers as needed
]

# Load, clean, and concatenate all flight data into a single DataFrame
all_flights_data = pd.concat([load_and_clean_data(file, identifier) for file, identifier in json_files_with_identifiers])

# Group by 'Flight Unique Number' and 'Source' to find the minimum price for each unique flight from each source
min_price_per_flight = all_flights_data.groupby(['Flight Unique Number', 'Source'], as_index=False)['Price'].min()

# Sorting the results by price for better visualization
min_price_per_flight_sorted = min_price_per_flight.sort_values(by='Price')

# Create an interactive bar chart with Plotly
fig = px.bar(min_price_per_flight_sorted, x='Flight Unique Number', y='Price',
             color='Source',  # Use the source as a color dimension
             hover_data=['Flight Unique Number', 'Price', 'Source'],
             labels={'Price': 'Lowest Price', 'Flight Unique Number': 'Flight Unique Number', 'Source': 'Source Day'},
             title='Lowest Price for Each Unique Flight Number by Source')

fig.update_layout(xaxis={'categoryorder':'total descending'}, xaxis_title='Flight Unique Number',
                  yaxis_title='Lowest Price', title_x=0.5)

# Show plot
fig.show()
