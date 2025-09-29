import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("unsplash_KEY")

url = "https://api.unsplash.com/photos"

headers = {
    "Accept-Version": "v1",
    "Authorization": API_KEY
}

page = 1

params = {
    "page": page,
    "per_page": 30
}

while page <= 2:
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        page += 1
        for photo in data:
            link = photo["urls"]["regular"]        

            print(f"url: {link}")        

    else:
        print(f"Error: {response.status_code} - {response.text}")

limit = response.headers.get("X-Ratelimit-Limit")
remaining = response.headers.get("X-Ratelimit-Remaining")    

print(f"Rate Limit: {limit}")
print(f"Remaining: {remaining}")