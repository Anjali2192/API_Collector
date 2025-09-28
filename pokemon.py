import requests
import json

params = {
    "limit":20,
    "offset":0
}

base_url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(base_url, params = params)

if response.status_code == 200:
    data = response.json()
    result = data["results"]
    
    for i,pokemon in enumerate(result):
        print(i+1)
        print(pokemon["name"])
        print(pokemon["url"])
        print()
else:
    print(f"Error: {response.status_code} - {response.text}")