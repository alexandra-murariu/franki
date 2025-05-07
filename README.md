# Franki — From Netflix to Native

Franki is a French subtitle mining assistant that helps language learners turn TV shows into personalized vocabulary flashcards — **automatically**.

Inspired by my grandma’s old Larousse dictionary game, Franki brings slow, deliberate vocabulary discovery back into the digital age — from clipboard to Anki.

---

## What It Does

Franki listens to your **clipboard** and:

1. Detects new subtitles (e.g. copied via the [ASBPlayer extension](https://chromewebstore.google.com/detail/asbplayer-language-learni/hkledmpjpaehamkiehglnbelcpdflcab)).
2. Extracts **hard words** using:
   - Lemmatization via [spaCy French model](https://spacy.io/models/fr)
   - Filtering out common French words using a [top 50k frequency list](https://github.com/hermitdave/FrequencyWords)
   - Removing stopwords and named entities
3. Looks up definitions from [Larousse.fr](https://www.larousse.fr/dictionnaires/francais/)
4. Formats a clean Anki card with:
   - The subtitle for context
   - The word and its definition, including synonyms and antonyms
5. Sends the flashcard to [Anki](https://apps.ankiweb.net/) using [AnkiConnect](https://foosoft.net/projects/anki-connect/) (**NOTE**: you have to configure AnkiConnect first in the Anki app, [this](https://www.youtube.com/watch?v=KxLRp1yd8Ro) is a nice video explaining how to expose Anki on `localhost`, port `8765`, as required by Franki)

---

## Prerequisites
1. Configure [AnkiConnect](https://foosoft.net/projects/anki-connect/), and create a `franki` deck in your Anki app.  [This](https://www.youtube.com/watch?v=KxLRp1yd8Ro) is a nice video explaining how to expose Anki on `localhost`, port `8765`, as required by Franki.
2. Install the [`asbplayer`](https://chromewebstore.google.com/detail/asbplayer-language-learni/hkledmpjpaehamkiehglnbelcpdflcab) browser extension.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alexandra-murariu/franki.git
   cd franki

2. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install .

## Run!
This is the command to start Franki and generate cards:
   ```bash
   python -m franki
   ```

Before this, make sure the `asbplayer` extension is mining the subtitles in your browser. This is a tutorial to get you started: ![tutorial](tutorial.gif)
