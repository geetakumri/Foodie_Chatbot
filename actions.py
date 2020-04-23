# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
# Import the email modules we'll need
from email.message import EmailMessage
import zomatopy
import json
import requests
# Import smtplib for the email sending function
import smtplib
from concurrent.futures import ThreadPoolExecutor
response = ''

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        print("inside action search restaurant")
        config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)

        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget_min = tracker.get_slot('budgetmin')
        budget_max = tracker.get_slot('budgetmax')

        print('location; {}, cuisine: {}, budgetmin: {}, budgetmax: {}'.format(loc, cuisine, budget_min, budget_max))

        if not loc:
            return [SlotSet('location', loc), SlotSet('restaurant_exist', False)]

        results, lat, lon = self.get_location_suggestions(loc, zomato)
        print('result {}'.format(results))

        if results == 0:
            restaurant_exist = False
            dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
        else:
            restaruant_list = self.get_restaurants(lat, lon, budget_min, budget_max, cuisine)

            budget_restaurant = [restaurant for restaurant in restaruant_list if ((restaurant['restaurant']['average_cost_for_two'] > budget_min) & (restaurant['restaurant']['average_cost_for_two'] < budget_max))]

            budget_restaurant_sorted = sorted(budget_restaurant, key = lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse = True)

            global response
            if response:
                response = ''
            
            restaurant_exist = False

            if len(budget_restaurant_sorted) == 0:
                dispatcher.utter_message("no results")
                return
            else:
                top5_restaurant = budget_restaurant_sorted[:5]

            for restaurant in top5_restaurant:
                response = response + "Found " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"

            dispatcher.utter_message("-----\n{}-----\n".format(response))
        return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]
    

    def get_location_suggestions(self, loc, zomato):
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        results = len(d1["location_suggestions"])

        return results, lat, lon

    def get_restaurants(self, lat, lon, budgetmin, budgetmax, cuisine):
        cuisines_dict = {
            'american': 1, 
            'chinese': 25, 
            'italian': 55,
            'mexican': 73, 
            'north indian': 50, 
            'south indian': 85
        }
        d_rest = []
        executor = ThreadPoolExecutor(max_workers=5)
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
        executor.shutdown()
        return d_rest

def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json', 'user-key': '5787bb8301dd97fbe86ec40febf7e03b'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
        cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    d_rest.extend(d['restaurants'])

class ActionValidateCityName(Action):
    """This action is to validate user provided city name"""

    def name(self):
        # identifier of the action
        return 'action_validate_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        print('location name: {}'.format(loc))

        if not loc:
            dispatcher.utter_message("Please enter a location")
            return [SlotSet('location_ok', False)]

        allowed_cities = ['Agra', 'Ahmedabad', 'Ajmer', 'Aligarh', 'Allahabad', 'Amravati', 'Amritsar',
            'Asansol', 'Aurangabad', 'Bangalore', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhilai', 'Bhiwandi', 'Bhopal', 
            'Bhubaneswar', 'Bikaner', 'Bokaro Steel City', 'Chandigarh', 'Chennai', 'Coimbatore', 'Cuttack', 'Dehradun', 
            'Delhi', 'Dhanbad', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Goa', 'Gorakhpur', 'Gulbarga', 
            'Guntur', 'Gurgaon', 'Guwahati', 'Gwalior', 'Hubli-Dharwad', 'Hyderabad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 
            'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Kochi', 'Kolhapur', 
            'Kolkata', 'Kollam', 'Kota', 'Kottayam', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 
            'Mangalore', 'Mathura', 'Meerut', 'Moradabad', 'Mumbai', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 
            'Palakkad', 'Patna', 'Pondicherry', 'Pune', 'Raipur', 'Rajahmundry', 'Rajkot', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 
            'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 
            'Tiruppur', 'Ujjain', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vellore', 'Vijayapura', 'Vijayawada', 
            'Visakhapatnam', 'Warangal']

        if not (loc.title() in allowed_cities):
            dispatcher.utter_message("sorry, we don't operate in this city")
            return [SlotSet('location_ok', False)]
        return [SlotSet('location_ok', True), SlotSet('location', loc)]

class SendEmailAction(Action):
    def name(self):
        return 'action_send_email'
    
    def run(self, dispatcher, tracker, domain):
        to_email_id = tracker.get_slot("email_id")

        if not to_email_id:
            #dispatcher.utter_message('Good Bye')
            return

        location = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')

        global response
        email_sub = self.get_email_subject(location, cuisine)
        email_body = 'Hi User,\nPlease find top {} restaurants in {}.\n\n{}Sincerely,\nFoodie Chatbot'.format(cuisine, location, response)

        self.send_email(to_email_id, email_sub, email_body)

        dispatcher.utter_message('Restaurants list has been sent to your email id. Enjoy!!')

    def send_email(self, to_email_id, email_sub, email_body):
        sender_email_add = 'chatbotfoodie1@gmail.com'
        passowrd = 'V3BpvmqeaEgy8RC'

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email_add, passowrd)

        email = EmailMessage()
        email['Subject'] = email_sub
        email['To'] = to_email_id
        email['From'] = 'Foodie <{}>'.format(sender_email_add)
        email.set_content(email_body)

        server.send_message(email)
        server.quit()
    
    def get_email_subject(self, location, cuisine):
        return 'Top {} restaurants in {}'.format(cuisine.title(), location.title())



        


