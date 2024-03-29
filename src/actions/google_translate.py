from os import environ, path
from typing import Text
import six

from google.cloud import translate_v2 as translate

environ["GOOGLE_APPLICATION_CREDENTIALS"] = path.abspath("../credentials.json")
translate_client = translate.Client()
languages = {}


def load_languages_in_memory():
    results = translate_client.get_languages()

    for language in results:
        name = str(language["name"]).lower()
        code = language["language"]
        languages[name] = code


def get_language_code(language: Text) -> Text:
    return languages[language.lower().strip()]


def translate_text(text, language):
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    language_code = get_language_code(language)
    result = translate_client.translate(
        values=text,
        target_language=language_code
    )

    return result["translatedText"]
