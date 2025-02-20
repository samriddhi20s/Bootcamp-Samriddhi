#Access Rick and Morty Characters
#Objective: Fetch character information from "The Rick and Morty API".
#Task: Write a script to get and display information about characters from "The Rick and Morty API" (https://rickandmortyapi.com/api/character).
# Approach: Fetch data from the Rick and Morty API, parse JSON response, and display character names and species.
import requests

def fetch_characters():
    url = "https://rickandmortyapi.com/api/character"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print("Rick and Morty Characters:")
        for character in data["results"]:
            print(f"Name: {character['name']}, Species: {character['species']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching character data: {e}")

if __name__ == "__main__":
    fetch_characters()
