import requests
import json

params = {
    "limit":20,
    "offset":0
}

base_url = "https://pokeapi.co/api/v2/pokemon"

pokemon_list = []

while base_url and len(pokemon_list) < 200:
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        pokemon_list.extend(data["results"])
        base_url = data["next"]

    else:
        print(f"Error: {response.status_code} - {response.text}")
        break

# Save to JSON file
with open("pokemons.json", "w") as f:
    json.dump(pokemon_list, f, indent=4)

print(f"Saved {len(pokemon_list)} Pokemons in pokemons.json")