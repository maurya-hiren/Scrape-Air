import json

# Load the JSON data from the file
with open("scraped_data_stratechery.json", "r") as f:
    json_data = json.load(f)

# Convert the JSON data into a structured format
for item in json_data:
    item["title"] = item['title']
    del item['title']

# Save the structured data to a new file
with open("structured_data.json", "w") as f:
    json.dump(json_data, f)