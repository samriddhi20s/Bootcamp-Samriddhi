#GraphQL Query for AniList Anime Data
#Objective: Fetch and display anime information using AniList's GraphQL API.
#Task: Use gql to query AniList for information on an anime by its title.
#GraphQL Endpoint: https://graphql.anilist.co
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

# Approach: Use GraphQL to query AniList's API, sending a query to retrieve anime details by title.

def fetch_anime(title):
    url = "https://graphql.anilist.co"
    headers = {"Content-Type": "application/json"}
    query = {
        "query": """
        query ($title: String) {
            Media(search: $title, type: ANIME) {
                title {
                    romaji
                    english
                }
                description
                status
            }
        }
        """,
        "variables": {"title": title}
    }
    try:
        response = requests.post(url, headers=headers, json=query)
        response.raise_for_status()
        data = response.json()
        anime = data["data"]["Media"]
        
        print("Anime Details:")
        print(f"Title: {anime['title']['romaji']} ({anime['title'].get('english', 'N/A')})")
        print(f"Description: {anime['description']}")
        print(f"Status: {anime['status']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching anime data: {e}")

if __name__ == "__main__":
    fetch_characters()
    anime_title = input("Enter an anime title: ")
    fetch_anime(anime_title)
