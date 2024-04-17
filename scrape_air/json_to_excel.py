import pandas as pd
import os
import json

json_folder = './Json'

excel_folder = './Excel'
os.makedirs(excel_folder, exist_ok=True)

for json_file in os.listdir(json_folder):
    if json_file.endswith('.json'):
        json_path = os.path.join(json_folder, json_file)
       
        with open(json_path, 'r') as file:
            data = json.load(file)
        
        df = pd.DataFrame(data)
        
        excel_file = json_file.replace('.json', '.xlsx')
        excel_path = os.path.join(excel_folder, excel_file)
        
        df.to_excel(excel_path, index=False, engine='openpyxl')

print("Conversion completed. Check the Excel files in the specified folder.")
