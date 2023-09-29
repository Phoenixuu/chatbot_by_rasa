# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from telnetlib import DO
from typing import Any, Text, Dict, List

from numpy import disp

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType 
from rasa_sdk.types import DomainDict
size_coffee = ['m','s','l']
type_coffee = ['capuchino','mocha','latte','americano','caramel','espresso','black']
class ValidateSimpleCoffeeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_coffee_form"
    
    def validate_coffee_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'coffee_size' value."""

        if slot_value.lower not in size_coffee:
            dispatcher.utter_message(text=f"Chúng tôi có 3 size cho các loại cafe: s/m/l\nBạn muốn chọn size nào")
            return {"coffee_size":None}
        dispatcher.utter_message(text = f"OK! Chúng tôi đã ghi nhận bạn muốn đặt size {slot_value}.")
        return {"coffee_size":slot_value}

    def validate_coffee_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'coffee_type' value."""

        if slot_value not in type_coffee:
            dispatcher.utter_message(text = f"Ở đây chúng tôi chỉ có các loại: {'/'.join(type_coffee)}.")
            return {"coffee_type": None}
        dispatcher.utter_message(text = f"Bạn đã chọn {slot_value} coffee.\nVui lòng đợi trong giây lát")
        return {"coffee_type": slot_value}



# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionHelloWorld(Action):
#     def name(self) -> Text:
#         return "action_show_time"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any])
#         print("Custom code goes here!")

#         return []
