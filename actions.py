# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List,Union
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


class BookForm(FormAction):
    
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "book_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["room_count", "room_type"]

    def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict]:
        """Define what the form has to do
        after all required slots are filled"""

        # utter submit template
        rooms_count=int(tracker.get_slot("room_count"))
        type_of_room=tracker.get_slot("room_type")
 
        dispatcher.utter_message(text="You chose {} {} rooms to book\nDid I help you?".format(rooms_count,type_of_room))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""

        return {
        "room_count": self.from_entity(entity="room_count", intent="number_of_rooms"),
        "room_type": self.from_entity(entity="room_type", intent="type_of_room")
        }

    def validate_room_count(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> Dict[Text, Any]:
        """Validate room_count value."""

        if int(value) <=10:
           
            return {"room_count": value}
        else:
            dispatcher.utter_message(template="utter_wrong_room_count")

            return {"room_count": None}


class CleanForm(FormAction):
    
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "clean_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["time"]

    def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict]:
        """Define what the form has to do
        after all required slots are filled"""

        # utter submit template
        time = tracker.get_slot("time")
        
        if time =="right now" or time =="immediately":
            dispatcher.utter_message(text="Sure I will send someone right now")
            
        
        else:

            numbers=["1","2","3","4","5","6","7","8","9","0"]

            time_value_h=0
            time_value_m=0

            for i,val in enumerate(time):

                if val=='h':
                    if time[i-1] ==' ':
                        time_value_h+=int(time[i-2])
                        if time[i-3] in numbers:
                            time_value_h+=(int(time[i-3])*10)
                    else:
                        time_value_h+=int(time[i-1])
                        if time[i-2] in numbers:
                            time_value_h+=(int(time[i-2])*10)

                if val=='m':
                    if time[i-1] ==' ':
                        time_value_m+=int(time[i-2])
                        if time[i-3] in numbers:
                            time_value_m+=(int(time[i-3])*10)
                    else:
                        time_value_m+=int(time[i-1])
                        if time[i-2] in numbers:
                            time_value_m+=(int(time[i-2])*10)
            

            if "hour" in time and "minute" in time:


                hour = int(time_value_h) + datetime.now().time().hour
                minute = int(time_value_m) + datetime.now().time().minute

                if minute >= 60:
                    hour = hour + 1
                    minute=minute-60
                    if minute/10 <1:
                        minute="0"+str(minute)
                 
                if hour >= 12:
                    hour =hour-12
                    if hour/10 < 1:
                        hour="0"+str(hour)
                    dispatcher.utter_message(text="Sure I will send someone at {}:{} PM".format(hour,minute))
                else:
                    if hour/10 <1:
                        hour="0"+str(hour)
                    dispatcher.utter_message(text="Sure I will send someone at {}:{} AM".format(hour,minute))
            

            elif "hour" in time:
                hour = int(time_value_h) + datetime.now().time().hour

                minute=datetime.now().time().minute

                if minute/10 <1 :
                    minute="0"+str(minute)

                if hour >= 12:
                    hour =hour-12
                    if hour/10 <1 :
                        hour="0"+str(hour)
                    dispatcher.utter_message(text="Sure I will send someone at {}:{} PM".format(hour,minute))
                else:
                    if hour/10 <1 :
                        hour="0"+str(hour)
                    dispatcher.utter_message(text="Sure I will send someone at {}:{} AM".format(hour,minute))

            elif "minute" in time:
                hour = datetime.now().time().hour
                minute = int(time_value_m) + datetime.now().time().minute
    
                if minute >= 60:
                    hour = hour + 1
                    minute=minute-60
                    if minute/10 <1:
                        minute="0"+str(minute)
                 
                if hour >= 12:
                    hour =hour-12
                    if hour/10 < 1:
                        hour="0"+str(hour)
                    dispatcher.utter_message(text="Sure I will send someone at {}:{} PM".format(hour,minute))
                else:
                    if hour/10 <1:
                        hour="0"+str(hour)
                    dispatcher.utter_message(text="Sure I will send someone at {}:{} AM".format(hour,minute))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""

        return {
        "time": self.from_entity(entity="time", intent="when_to_clean")
        }

    def validate_time(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> Dict[Text, Any]:
        """Validate time value."""

        if "hour" in value or "minute" in value or "right now" in value or "immediately" in value :
           
            return {"time": value}
        else:
            dispatcher.utter_message(template="utter_wrong_time")

            return {"time": None}



