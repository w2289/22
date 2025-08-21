"""Generate English-Chinese flashcards with phonetics and example sentences.

The script requires internet access to query free dictionary and translation
services. It generates a JSON file "flashcards.json" with a list of objects:
{
    "word": "example",
    "phonetic": "ɪɡˈzɑːmpəl",
    "example": "This is an example sentence.",
    "chinese": "例子"
}

Dependencies:
    pip install wordfreq googletrans==4.0.0-rc1 eng-to-ipa requests
"""

import json
import time
from typing import Dict

import requests
from wordfreq import top_n_list
from googletrans import Translator
from eng_to_ipa import convert


def fetch_word_data(word: str, translator: Translator) -> Dict[str, str]:
    """Fetch phonetic, example sentence and Chinese translation for a word."""
    phonetic = ""
    example = ""
    # dictionaryapi.dev provides free dictionary data
    try:
        resp = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}", timeout=5
        )
        data = resp.json()[0]
        phonetic = data.get("phonetic", "")
        for meaning in data.get("meanings", []):
            for definition in meaning.get("definitions", []):
                ex = definition.get("example")
                if ex:
                    example = ex
                    break
            if example:
                break
    except Exception:
        pass

    if not phonetic:
        phonetic = convert(word)

    try:
        chinese = translator.translate(word, dest="zh-CN").text
    except Exception:
        chinese = ""

    return {
        "word": word,
        "phonetic": phonetic,
        "example": example,
        "chinese": chinese,
    }


def main() -> None:
    translator = Translator()
    words = top_n_list("en", n=3000)
    flashcards = []
    for word in words:
        flashcards.append(fetch_word_data(word, translator))
        time.sleep(0.1)  # be polite with free services
    with open("flashcards.json", "w", encoding="utf-8") as fh:
        json.dump(flashcards, fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
