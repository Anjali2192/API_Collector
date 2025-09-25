import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("pexels_KEY")

url = "https://api.pexels.com/v1/search"
headers = {"Authorization": API_KEY}
params = {"query": "nature"}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    #print(json.dumps(data, indent=4))
    for photo in data["photos"]:
        photo_id = photo["id"]
        photo_url = photo["url"]
        print(f"ID: {photo_id}")
        print(f"URL: {photo_url}")
        print()

    limit = response.headers.get("X-Ratelimit-Limit")
    remaining = response.headers.get("X-Ratelimit-Remaining")

    print(f"rate Limit: {limit}")
    print(f"Remaining: {remaining}")
    
else: 
    print(f"Error: {response.status_code} - {response.text}")