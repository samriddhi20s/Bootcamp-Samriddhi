#Get User Details from GitHub
#Objective: Retrieve user details from GitHub using their REST API.
#Task: Create a command line program that takes a GitHub username as an argument and fetches details about the user (https://api.github.com/users/{username}).
# Approach: Use argparse to take a GitHub username as a command-line argument,
# make a GET request to GitHub's API, and extract relevant user details.
import requests
import argparse

def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        user_data = response.json()
        
        print("GitHub User Details:")
        print(f"Name: {user_data.get('name', 'N/A')}")
        print(f"Public Repositories: {user_data.get('public_repos', 'N/A')}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user details: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch GitHub user details.")
    parser.add_argument("username", type=str, help="GitHub username")
    args = parser.parse_args()
    
    fetch_github_user(args.username)
