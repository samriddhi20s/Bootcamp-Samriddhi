def upper_case(text: str) -> str:
    return text.upper()

def lower_case(text: str) -> str:
    return text.lower()

def capitalize(text: str) -> str:
    return text.title()

def remove_stop_words(text: str) -> str:
    stop_words = {"a", "an", "the", "and", "or"}
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

def uk_to_us(text: str) -> str:
    import re
    return re.sub(r"(\w*)sation\b", r"\1zation", text)
