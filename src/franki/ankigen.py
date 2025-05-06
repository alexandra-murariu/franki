import requests

ANKI_CONNECT_URL = "http://localhost:8765"
DEFAULT_DECK = "Franki"


def ensure_deck(deck_name=DEFAULT_DECK):
    response = requests.post(ANKI_CONNECT_URL, json={
        "action": "createDeck",
        "version": 6,
        "params": {"deck": deck_name}
    })
    return response.json()


def add_card(front, back, deck_name=DEFAULT_DECK, tags=None):
    if tags is None:
        tags = ["franki"]

    note = {
        "deckName": deck_name,
        "modelName": "Basic",
        "fields": {
            "Front": front,
            "Back": back,
        },
        "tags": tags,
        "options": {
            "allowDuplicate": False
        }
    }

    response = requests.post(ANKI_CONNECT_URL, json={
        "action": "addNote",
        "version": 6,
        "params": {"note": note}
    })
    return response.json()