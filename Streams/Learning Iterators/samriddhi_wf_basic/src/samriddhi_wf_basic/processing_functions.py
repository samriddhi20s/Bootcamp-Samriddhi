import os
import requests
import re

STOP_WORDS = {"a", "an", "the", "and", "or"}

def upper_case(input_filename: str, output_filename: str = None):
    """Converts all text in a file to uppercase."""
    if output_filename is None:
        output_filename = f"{input_filename}.processed"

    with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
        for line in infile:
            outfile.write(line.upper())

    print(f"Processed file saved as: {output_filename}")


def lower_case(input_filename: str, output_filename: str = None):
    """Converts all text in a file to lowercase."""
    if output_filename is None:
        output_filename = f"{input_filename}.processed"

    with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
        for line in infile:
            outfile.write(line.lower())

    print(f"Processed file saved as: {output_filename}")


def remove_stop_words(text: str) -> str:
    """Removes stop words from a given text string."""
    words = text.split()
    filtered_words = [word for word in words if word not in STOP_WORDS]
    return " ".join(filtered_words)


def capitalize(input_filename: str, output_filename: str = None):
    """Capitalizes all words in a file."""
    if output_filename is None:
        output_filename = f"{input_filename}.processed"

    with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
        for line in infile:
            outfile.write(line.title())

    print(f"Processed file saved as: {output_filename}")


def fetch_geo_ip(ip_number: str) -> str:
    """Fetches city, region, and country for an IP address from ipinfo.io."""
    url = f"https://ipinfo.io/{ip_number}/geo"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return f"{data.get('city', '')}, {data.get('region', '')}, {data.get('country', '')}"
    except requests.RequestException:
        return "Error fetching IP data"


def uk_to_us(text: str) -> str:
    """Replaces words ending in 'sation' with 'zation'."""
    return re.sub(r"\bsation\b", "zation", text)
