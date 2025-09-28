import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("pexels_KEY")

url = "https://api.pexels.com/v1/search?page=1&per_page=80&query=nature"
headers = {"Authorization": API_KEY}

photo_list =[]

while url and len(photo_list) < 1000:
    response = requests.get(url, headers=headers)    

    if response.status_code == 200:
        data = response.json()
        url = data["next_page"]
        #print(json.dumps(data, indent=4))
        for photo in data["photos"]:
            photo_list.append(photo["id"])
            photo_list.append(photo["url"])

            if len(photo_list) >= 1000:
                break
            
        limit = response.headers.get("X-Ratelimit-Limit")
        remaining = response.headers.get("X-Ratelimit-Remaining")    

        print(f"rate Limit: {limit}")
        print(f"Remaining: {remaining}")
        
    else: 
        print(f"Error: {response.status_code} - {response.text}")
        break

# Save data to JSON file
with open("photo.json", "w") as f:
    json.dump(photo_list, f, indent=4)

print(F"Saved {len(photo_list)} photos in photo.json")