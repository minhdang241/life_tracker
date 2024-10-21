import json
from datetime import datetime

# Load the JSON data
with open('test.json', 'r') as file:
    data = json.load(file)

total_duration = 0

# Iterate through the items
for event in data['items']:
    if event.get('colorId') == '2':
        start_time = datetime.fromisoformat(event['start']['dateTime'])
        end_time = datetime.fromisoformat(event['end']['dateTime'])
        duration = (end_time - start_time).total_seconds() / 3600  # Convert seconds to hours
        total_duration += duration

print(f"Total time spent on events with colorId = 2: {total_duration} hours")