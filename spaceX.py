import requests

url = "https://api.spacexdata.com/v4/rockets"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for nme in data:
        print(nme["name"])

else:
    print(f"Error: {response.status_code} - {response.text}")