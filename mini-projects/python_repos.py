import requests

# Make an API call and store the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"State code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

# Process the results.
print(response_dict.keys())

