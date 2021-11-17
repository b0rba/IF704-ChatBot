from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils import is_empty_or_none
from .google_translate import translate_text, load_languages_in_memory

load_languages_in_memory()


class ActionTranslate(Action):
    def name(self) -> Text:
        return "action_translate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots = tracker.current_slot_values()
        print(slots)
        sentence = slots["phrase"]
        language = slots["lang"]

        if is_empty_or_none(sentence) or is_empty_or_none(language):
            dispatcher.utter_message(text="Sorry I don't have enough information to translate")
            return []

        try:
            response = translate_text(sentence, language)
            dispatcher.utter_message(text=u"The translation is: {}".format(response))
        except KeyError:
            dispatcher.utter_message(text="Sorry I can't translate to this language.")

        return []
