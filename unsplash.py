import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("unsplash_KEY")

url = "https://api.unsplash.com/search/photos"

headers = {
    "Accept-Version": "v1",
    "Authorization": API_KEY
}

page = 1
all_urls = []

while True:
    params = {
        "page": page,
        "per_page": 30,
        "query": "nature"
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if not data:
            break

        result = data["results"]
        page += 1
        for i,photo in enumerate(result):
            link = photo["urls"]["regular"]       
            all_urls.append(link)            

    else:
        print(f"Error: {response.status_code} - {response.text}")

limit = response.headers.get("X-Ratelimit-Limit")
remaining = response.headers.get("X-Ratelimit-Remaining")    

print(f"Rate Limit: {limit}")
print(f"Remaining: {remaining}")

print(F"Total unique urls collected: {len(set(all_urls))}")