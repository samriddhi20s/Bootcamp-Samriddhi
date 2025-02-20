#List Public Events on GitHub
#Objective: Access and display GitHub's public events.
#Task: Use requests to fetch and print the recent public events from GitHub (https://api.github.com/events).
# Approach: Use the requests library to fetch public events from GitHub's API,
# parse the JSON response, and display relevant event details.
import requests

def fetch_github_events():
    url = "https://api.github.com/events"
    try:
        response = requests.get(url)
        response.raise_for_status()
        events = response.json()
        
        print("Recent GitHub Public Events:")
        for event in events[:10]:  
            print(f"Type: {event['type']}, Repo: {event['repo']['name']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching events: {e}")

if __name__ == "__main__":
    fetch_github_events()
