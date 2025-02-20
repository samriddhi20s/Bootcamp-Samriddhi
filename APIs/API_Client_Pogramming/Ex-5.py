#Post a message using Blueskey app API
#Objective: Use the Bluesky API to post a short 'tweet'.
#Task: Write a script that posts a message to your Bluesky account.
#API Endpoint: Refer to Bluesky's API documentation for posting tweets.
# Approach: Authenticate with Bluesky, obtain a session token, post a message, and log out.
import requests
import json

def authenticate(username, password):
    url = "https://bsky.social/xrpc/com.atproto.server.createSession"
    payload = {"identifier": username, "password": password}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["accessJwt"]

def post_message(token, message):
    url = "https://bsky.social/xrpc/com.atproto.repo.createRecord"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "repo": "your-handle.bsky.social",
        "collection": "app.bsky.feed.post",
        "record": {
            "text": message,
            "createdAt": "2025-02-20T00:00:00Z"
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    username = input("Enter your Bluesky username: ")
    password = input("Enter your Bluesky password: ")
    message = input("Enter your message: ")
    
    try:
        token = authenticate(username, password)
        response = post_message(token, message)
        print("Message posted successfully!", response)
    except requests.exceptions.RequestException as e:
        print("Error posting message:", e)
