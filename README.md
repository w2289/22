# English-Chinese Flashcards

Simple web-based flashcards for studying common English vocabulary. Each card
has a green background with white text. The front shows the English word with
its phonetic transcription and an example sentence, and the back shows the
Chinese translation.

## Files

- `index.html` – main page to view cards
- `style.css` – green theme styling
- `script.js` – loads card data and handles flipping
- `flashcards.json` – sample card data
- `generate_flashcards.py` – script to generate a full set of cards
- `requirements.txt` – Python dependencies for the generator

## Usage

Open `index.html` in a browser to practice the included sample cards.

To create a complete set of roughly 3000 cards:

```bash
pip install -r requirements.txt
python generate_flashcards.py
```

This requires an internet connection to fetch phonetics, example sentences and
Chinese translations.
