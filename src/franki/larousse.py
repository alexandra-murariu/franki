import requests
from bs4 import BeautifulSoup


def get_translation(word):
    url = f"https://www.larousse.fr/dictionnaires/francais/{word}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        definition_tag = soup.select_one(".Definitions .DivisionDefinition")

        if not definition_tag:
            definition_tag = soup.select_one(".Definitions .definition")

        if not definition_tag:
            return None

        return definition_tag.get_text(strip=True)

    except Exception as e:
        print(f" Error getting translation for {word}: {e}")
        return None