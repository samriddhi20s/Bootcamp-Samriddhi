#Fetch User Contributions on GitHub
#Objective: Use the GitHub REST API to fetch a user's contributions.
#Task: Write a command line program that takes a GitHub username and fetches the number of contributions in the last year.
#API Endpoint: Use GitHub's API to construct a query for contributions. Note: This may require parsing HTML or leveraging unofficial APIs.
#Approach: Use GitHub GraphQL API
import requests

GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
TOKEN = "your_personal_access_token"  # Replace with your GitHub token

def fetch_github_contributions(username):
    query = """
    query($login: String!) {
        user(login: $login) {
            contributionsCollection {
                contributionCalendar {
                    totalContributions
                }
            }
        }
    }
    """
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(GITHUB_GRAPHQL_URL, json={"query": query, "variables": {"login": username}}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contributions = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
        print(f"{username} has made {contributions} contributions in the last year.")
    else:
        print(f"Error fetching contributions: {response.status_code}, {response.text}")

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    fetch_github_contributions(username)
