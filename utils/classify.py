# from googletrans import Translator

# translator = Translator()

# def classify_severity(title: str) -> str:
#     # Translate Telugu to English
#     try:
#         translated = translator.translate(title, src='te', dest='en').text.lower()
#     except Exception:
#         translated = title.lower()

#     huge_keywords = ["blast", "fire", "flood", "death", "murder", "earthquake", "collapse"]
#     medium_keywords = ["protest", "attack", "accident", "crime", "violence"]
#     small_keywords = ["meeting", "visit", "announcement", "campaign"]

#     if any(word in translated for word in huge_keywords):
#         return "Huge"
#     elif any(word in translated for word in medium_keywords):
#         return "Medium"
#     elif any(word in translated for word in small_keywords):
#         return "Small"
#     return "Small"

from googletrans import Translator

translator = Translator()

def classify_severity(title: str) -> str:
    try:
        translated = translator.translate(title, src='te', dest='en').text.lower()
    except Exception:
        translated = title.lower()

    huge_keywords = ["blast", "fire", "flood", "death", "murder", "earthquake", "collapse"]
    medium_keywords = ["protest", "attack", "accident", "crime", "violence"]
    small_keywords = ["meeting", "visit", "announcement", "campaign"]

    if any(word in translated for word in huge_keywords):
        return "Huge"
    elif any(word in translated for word in medium_keywords):
        return "Medium"
    elif any(word in translated for word in small_keywords):
        return "Small"
    return "Small"
