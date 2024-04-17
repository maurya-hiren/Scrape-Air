import json
import random

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to manipulate the price by a random amount and save the modified data
def manipulate_and_save_prices(data, output_file_path):
    for flight in data:
        # Generate a random change amount between -1000 and 1000
        change_amount = random.randint(-1000, 1000)
        # Convert the price to an integer for manipulation
        original_price = int(flight["Price"].replace(",", ""))
        # Apply the change and ensure the price does not go below 0
        new_price = max(0, original_price + change_amount)
        # Update the price in the dataset
        flight["Price"] = f"{new_price:,}"
    # Save the manipulated data to a new file
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Path to your original JSON file
# filename= 'flight_data_1_id_4727.json'
file_path = '../Json/flight_data_1_id_3510.json'
# Specify your desired output file path
output_file_path = '../ml_jsons/Day_5.json'

# Load the original data
data = load_json(file_path)
# Manipulate the prices and save the modified data
manipulate_and_save_prices(data, output_file_path)
