import requests
import json

offset = 0

base_url = f"https://pokeapi.co/api/v2/pokemon?limit=20&offset={offset}"

pokemon_list = []

while base_url and len(pokemon_list) < 200:
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        pokemon_list.extend(data["results"])
        base_url = data["next"]
        offset += 20

    else:
        print(f"Error: {response.status_code} - {response.text}")
        break

# Save to JSON file
with open("pokemons.json", "w") as f:
    json.dump(pokemon_list, f, indent=4)

print(f"Saved {len(pokemon_list)} Pokemons in pokemons.json")