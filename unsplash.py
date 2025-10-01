import requests
import json
import os
from dotenv import load_dotenv
import time

load_dotenv()
API_KEY = os.getenv("unsplash_KEY")

url = "https://api.unsplash.com/search/photos"

headers = {
    "Accept-Version": "v1",
    "Authorization": API_KEY
}

page = 1

all_urls = []

while len(all_urls) < 1000 :
    try:
        params = {
            "page": page,
            "per_page": 30,
            "query": "nature"
        }

        response = requests.get(url, headers=headers, params=params)
         
        if response.status_code == 200:
            data = response.json()
            page += 1
            result = data["results"]
            for photo in result:
                link = photo["urls"]["regular"]       
                all_urls.append(link)          
            print(f"Fetching page: {page}, total collected: {len(all_urls)}")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.Timeout:
        print("Request timed out. Retrying in 5 sec...")
        time.sleep(5)
        continue

    except requests.exceptions.RequestException as e:
        print("Request failed: ", str(e))
        break

# Save data to JSON file
with open("photo.json", "w") as f:
    json.dump(all_urls, f, indent=4)

limit = response.headers.get("X-Ratelimit-Limit")
remaining = response.headers.get("X-Ratelimit-Remaining")    

print(f"Rate Limit: {limit}")
print(f"Remaining: {remaining}")