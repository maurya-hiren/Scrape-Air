import pandas as pd
import plotly.express as px

# Function to load, clean data, and add a column for the file name/identifier
def load_and_clean_data(file_path, identifier):
    df = pd.read_json(file_path)
    df['Price'] = df['Price'].str.replace(',', '').astype(float)
    print(df['Price'])
    df['Day'] = identifier  # Add a column for the identifier (e.g., Day_1)
    return df

# List of JSON file paths and their corresponding identifiers
json_files_with_identifiers = [
    ('../ml_jsons/Day_1.json', 'Day 1'),
    ('../ml_jsons/Day_2.json', 'Day 2'),
    ('../ml_jsons/Day_3.json', 'Day 3'),
    ('../ml_jsons/Day_4.json', 'Day 4'),
]

# Load, clean, and concatenate all flight data into a single DataFrame
all_flights_data = pd.concat([load_and_clean_data(file, identifier) for file, identifier in json_files_with_identifiers])

# Group by 'Flight Unique Number' and 'Day' to find the minimum price for each unique flight from each source
min_price_per_flight = all_flights_data.groupby(['Flight Unique Number', 'Day'], as_index=False)['Price'].min()
print(min_price_per_flight)
# Creating an advanced scatter plot with Plotly
fig = px.scatter(min_price_per_flight, x='Flight Unique Number', y='Price',
                 color='Day', symbol='Day',  # Different colors and symbols for each day
                 hover_name='Flight Unique Number', hover_data=['Day', 'Price'],
                 title='Lowest Price for Each Unique Flight Number by Day',
                 labels={'Price': 'Lowest Price', 'Flight Unique Number': 'Flight Unique Number', 'Day': 'Source Day'})

# Improve layout for better readability
fig.update_traces(marker=dict(size=10))  # Adjust marker size for visibility
fig.update_layout(xaxis_title='Flight Unique Number',
                  yaxis_title='Lowest Price',
                  xaxis={'categoryorder':'total descending'},
                  title_x=0.5)

# Show plot
fig.show()
