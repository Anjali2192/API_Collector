import requests

url = "https://api.github.com/search/repositories"

params = {
    "q": "python"
}

response = requests.get(url, params= params)

if response.status_code == 200:
    data = response.json()
    for i, repo in enumerate(data["items"]):
        name = repo["name"]
        repo = repo["watchers"]

        print(f"{i}. repo: {name}")
        print(f"    watchers: {repo}")
        print()

else:
    print(f"Error: {response.status_code} - {response.text}")