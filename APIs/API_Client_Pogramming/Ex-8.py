#Convert Currency Rates

#Objective: Fetch and calculate currency conversion rates.
#Task: Use the requests library to access the ExchangeRate-API (https://api.exchangerate-api.com/v4/latest/USD) and convert USD to another specified currency.
## Approach: Fetch the latest exchange rates from the ExchangeRate-API, extract the conversion rate,
# and compute the converted amount for a specified currency.
import requests
import argparse


def fetch_exchange_rate(base_currency, target_currency, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if target_currency not in data["rates"]:
            print(f"Currency {target_currency} not found.")
            return
        
        rate = data["rates"][target_currency]
        converted_amount = amount * rate
        
        print(f"Exchange Rate ({base_currency} -> {target_currency}): {rate}")
        print(f"Converted Amount: {converted_amount:.2f} {target_currency}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert USD to another currency using ExchangeRate-API.")
    parser.add_argument("base_currency", type=str, help="Base currency code (e.g., USD)")
    parser.add_argument("target_currency", type=str, help="Target currency code (e.g., EUR)")
    parser.add_argument("amount", type=float, help="Amount in base currency")
    args = parser.parse_args()
    
    fetch_exchange_rate(args.base_currency, args.target_currency, args.amount)
