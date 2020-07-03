# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionCleanConfirm(Action):

    def name(self) -> Text:
        return "action_clean_confirm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        time_type = tracker.get_slot("time_type")
        time_type = time_type.lower()
        if time_type == "right now":
            dispatcher.utter_message(text="Sure I will send someone right now")
            s = SlotSet("time_type", time_type)
            return [s]
        else:
            time_type = tracker.get_slot("time_type")
            time_type = time_type.lower()
            time_value = int(tracker.get_slot("time_value"))
            time = datetime.now().time()
            if time_type[0] == 'h':
                hour = int(time_value) + datetime.now().time().hour
                if hour >= 12:
                    dispatcher.utter_message(text="Sure I will send someone at {}:{} PM".format(hour - 12,datetime.now().time().minute))
                else:
                    dispatcher.utter_message(text="Sure I will send someone at {}:{} AM".format(hour,datetime.now().time().minute))

            if time_type[0] == 'm':
                hour = datetime.now().time().hour
                mi = int(time_value) + datetime.now().time().minute
    
                if mi + int(time_value) >= 60:
                    hour = hour + 1
                    if hour >= 12:
                        dispatcher.utter_message(text="Sure I will send someone at {}:{} PM".format(hour - 12,datetime.now().time().minute))
                    else:
                        dispatcher.utter_message(text="Sure I will send someone at {}:{} AM".format(hour,datetime.now().time().minute))
                else:
                    dispatcher.utter_message(text="Sure I will send someone after {} minutes".format(time_value))
    
            return [SlotSet("time_type", time_type), SlotSet("time_value", time_value)]




