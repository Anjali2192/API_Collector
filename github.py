import requests

url = "https://api.github.com/search/repositories"

params = {
    "q": "python",
    "sort": "stars",
    "order": "desc"
    }

response = requests.get(url, params= params)

if response.status_code == 200:
    data = response.json()
    for repo in data["items"]:
        name = repo["name"]
        repo = repo["watchers"]
        
        print(f"repo: {name}")
        print(f"watchers: {repo}")

else:
    print(f"Error: {response.status_code} - {response.text}")