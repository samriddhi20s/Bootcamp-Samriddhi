#Display NYT Best Sellers List
#Objective: Access and display the current New York Times Best Sellers list.
#Task: Use the requests library to fetch the current Best Sellers list from the New York Times API (https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={your-api-key}).

import requests

NYT_API_KEY = "your_api_key_here"  # Replace with your actual NYT API key
NYT_BESTSELLERS_URL = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json"

def fetch_nyt_bestsellers():
    """Fetch and display the current NYT Hardcover Fiction Best Sellers list."""
    params = {"api-key": NYT_API_KEY}
    
    try:
        response = requests.get(NYT_BESTSELLERS_URL, params=params)
        response.raise_for_status()
        data = response.json()

        books = data.get("results", {}).get("books", [])
        
        if not books:
            print("No best sellers found.")
            return
        
        print("\nNew York Times Best Sellers - Hardcover Fiction:\n")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book['title']} by {book['author']}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NYT Best Sellers: {e}")

if __name__ == "__main__":
    fetch_nyt_bestsellers()
