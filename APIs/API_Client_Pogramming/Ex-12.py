#Query Pokémon Data
#Objective: Access data on Pokémon via the PokéAPI.
#Task: Create a Python script that fetches data about a specific Pokémon from https://pokeapi.co/api/v2/pokemon/{name} and prints its types.
import requests

# Approach: Fetch data from the Rick and Morty API, parse JSON response, and display character names and species.

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

# Approach: Fetch top post IDs from Hacker News API, then retrieve and display titles and URLs.

def fetch_hacker_news():
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"
    try:
        response = requests.get(top_stories_url)
        response.raise_for_status()
        top_story_ids = response.json()[:10]
        
        print("Top Hacker News Posts:")
        for story_id in top_story_ids:
            story_response = requests.get(item_url.format(story_id))
            story_response.raise_for_status()
            story = story_response.json()
            print(f"Title: {story['title']}")
            print(f"URL: {story.get('url', 'No URL')}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Hacker News data: {e}")

# Approach: Fetch Pokémon details from PokéAPI and extract its type information.

def fetch_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        types = [t["type"]["name"] for t in data["types"]]
        print(f"Pokémon: {pokemon_name.capitalize()}")
        print(f"Types: {', '.join(types)}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pokémon data: {e}")

if __name__ == "__main__":
    fetch_characters()
    anime_title = input("Enter an anime title: ")
    fetch_anime(anime_title)
    fetch_hacker_news()
    pokemon_name = input("Enter a Pokémon name: ")
    fetch_pokemon(pokemon_name)
