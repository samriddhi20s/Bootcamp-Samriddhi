import re

STOP_WORDS = {"a", "an", "the", "and", "or"}

def lower_case(text: str) -> str:
    return text.lower()

def upper_case(text: str) -> str:
    return text.upper()

def remove_stop_words(text: str) -> str:
    words = text.split()
    return " ".join(word for word in words if word.lower() not in STOP_WORDS)

def uk_to_us(text: str) -> str:
    return re.sub(r"sation\b", "zation", text)
