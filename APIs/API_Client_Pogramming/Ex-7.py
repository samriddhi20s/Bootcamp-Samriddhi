#Query SpaceX Launch Data with GraphQL
#Objective: Fetch details about SpaceX launches.
#Task: Write a Python script that queries the SpaceX API (https://api.spacex.land/graphql/) for the latest launch details using GraphQL.
# Approach: Use GraphQL to query the SpaceX API, sending a query to retrieve details
# about the latest launch, including mission name, launch date, and rocket name.
import requests
import json

def fetch_latest_launch():
    url = "https://api.spacex.land/graphql/"
    headers = {"Content-Type": "application/json"}
    query = {
        "query": """
        query {
            launchLatest {
                mission_name
                launch_date_utc
                rocket {
                    rocket_name
                }
            }
        }
        """
    }
    
    response = requests.post(url, headers=headers, json=query)
    response.raise_for_status()
    data = response.json()
    
    launch = data["data"]["launchLatest"]
    print("Latest SpaceX Launch:")
    print(f"Mission: {launch['mission_name']}")
    print(f"Launch Date: {launch['launch_date_utc']}")
    print(f"Rocket: {launch['rocket']['rocket_name']}")

if __name__ == "__main__":
    fetch_latest_launch()
