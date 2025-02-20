#Use GraphQL to Query GitHub User Repositories
#Objective: Fetch a list of repositories for a GitHub user using GraphQL.
#Task: Utilize the gql library to query GitHub's GraphQL API for a user's repositories. Include the repository name and description in the query.
#GraphQL Endpoint: https://api.github.com/graphql - You'll need a GitHub token.
# Approach: Use GraphQL to query GitHub's API, providing a personal access token,
# sending a query to retrieve a user's repositories with names and descriptions.
import requests
import json
import argparse

def fetch_github_repos(username, token):
    url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    query = {
        "query": f"""
        query {{
            user(login: \"{username}\") {{
                repositories(first: 10) {{
                    nodes {{
                        name
                        description
                    }}
                }}
            }}
        }}
        """
    }
    
    response = requests.post(url, headers=headers, json=query)
    response.raise_for_status()
    data = response.json()
    
    print("GitHub Repositories:")
    for repo in data["data"]["user"]["repositories"]["nodes"]:
        print(f"Name: {repo['name']}, Description: {repo['description'] or 'No description'}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch GitHub repositories using GraphQL.")
    parser.add_argument("username", type=str, help="GitHub username")
    parser.add_argument("token", type=str, help="GitHub personal access token")
    args = parser.parse_args()
    
    fetch_github_repos(args.username, args.token)
