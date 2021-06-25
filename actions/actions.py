# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class dados(FormValidationAction):
    def name(self) -> Text:
        """Identifica o form na estória do Rasa."""
        return "validate_numero_form"
    
    def validate_numero(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(slot_value)
        
        numero = int(slot_value)
        if (numero%2) == 0:
            print("Par")
            dispatcher.utter_message(text="Par")
        else:
            print("Ímpar")
            dispatcher.utter_message(text="Ímpar")

        return {}
    