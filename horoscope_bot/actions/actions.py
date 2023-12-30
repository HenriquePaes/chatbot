from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests

class GetTodaysHoroscope(Action):
    def name(self) -> Text:
        return "get_todays_horoscope"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        base_url = 'https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign}&day={day}'
        url = base_url.format(**{'day': "today", 'sign': user_horoscope_sign})

        res = requests.get(url)
        todays_horoscope = res.json()['horoscope_data']
        response = "Your today's horoscope:\n{}".format(todays_horoscope)

        dispatcher.utter_message(response)

        return [SlotSet("horoscope_sign", user_horoscope_sign)]

class SubscriberUser(Action):
    def name(self):
        return "subscriber_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        subscribe = tracker.get_slot('subscribe')

        if subscribe == 'True':
            response = "You're successfully subscribed"
        if subscribe == 'False':
            response =  "You're successfully unsubscribed"

        dispatcher.utter_message(response)
        return [SlotSet("subscribe", subscribe)]