import os
import requests
from datetime import datetime
import json

current_date = datetime.now().strftime('%Y-%m-%d')
folder = f"data_{current_date}"
os.makedirs(folder, exist_ok=True)

vehicles = ['3707', '3159']
data = []

for v in vehicles:
    url = f"https://busdata.cs.pdx.edu/api/getBreadCrumbs?vehicle_id={v}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        vehicle_data = response.json()
        data.extend(vehicle_data)
        print(f"Downloaded data for vehicle ID: {v}")

    except requests.RequestException as e:
        print(f"Error for vehicle ID {v}: {e}")

output_file = 'vehicle_info.json'
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Data saved to file: {output_file}")
