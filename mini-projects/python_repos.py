import requests

# Make an API call and store the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

# Process the results.
print(response_dict.keys())

# Convert the response object to a dictionary.
print(f"Total number of repositories: {response_dict['total_count']}") 
print(f"Is the complete result set returned?: "
      f"{not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict['items'] 
print(f"Number of repositories returned: {len(repo_dicts)}")


# Analyze the first repository.
repo_dict = repo_dicts[0] 
print(f"\nNumber of keys: {len(repo_dict)}") 
for key in sorted(repo_dict.keys()): 
    print(key)

print("\nSelected information about the first repository:")
print(f"Name: {repo_dict['name']}")  
print(f"Owner: {repo_dict['owner']['login']}")  
print(f"Stars: {repo_dict['stargazers_count']}")  
print(f"Repository URL: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")  
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

print("\nSelected information about each repository:")  
for repo_dict in repo_dicts:  
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository URL: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

# Rate limiting (maximum number of requests that can be made in a given 
# time period):
# https://api.github.com/rate_limit

# The 'reset' key value represents, expressed as Unix epoch time 
# (i.e., the number of seconds that have elapsed since midnight 
# on January 1, 1970), the time when the rate limit will be reset.

# For many APIs, registration is required, and after registering, 
# you can obtain an API key that allows you to make API calls.

