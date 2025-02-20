#Fetch Public GitHub Repositories
#Objective: Use the GitHub REST API to fetch public repositories.
#Task : Write a Python script that uses the requests library to get a few of public repositories from the GitHub API
# Approach: Use the requests library to make a GET request to GitHub API
# and parse the JSON response to extract repository names.
import requests

def fetch_github_repos():
    url = "https://api.github.com/repositories"
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()

        print("Public GitHub Repositories:")
        for repo in repositories[:10]:  # Limit to the first 10 repositories
            print(repo['name'])
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_github_repos()
