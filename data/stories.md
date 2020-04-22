## story_1
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location":"bengaluru"}
  - slot{"location":"bengaluru"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"indian"}
  - slot{"cuisine":"indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"0", "budgetmax":"300"}
  - slot{"budgetmin":"0"}
  - slot{"budgetmax":"300"}
  - action_search_restaurants
  - utter_goodbye


## say_goodbye
* goodbye
  - utter_goodbye

## story_2
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "bengaluru"}
  - slot{"location": "bengaluru"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
  - slot{"budgetmax": "300"}
  - slot{"budgetmin": "0"}
  - action_search_restaurants
  - utter_goodbye


## story_3
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "agra"}
  - slot{"location": "agra"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
  - slot{"budgetmax": "700"}
  - slot{"budgetmin": "300"}
  - action_search_restaurants
  - utter_goodbye


## story_4
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "kolkata"}
  - slot{"location": "kolkata"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "1000"}
  - slot{"budgetmax": "1000"}
  - slot{"budgetmin": "700"}
  - action_search_restaurants
  - utter_goodbye


## story_5
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "1000"}
  - slot{"budgetmax": "1000"}
  - slot{"budgetmin": "700"}
  - action_search_restaurants
  - utter_goodbye


## fail_story_1
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "tokyo"}
  - slot{"location": "tokyo"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "bengaluru"}
  - slot{"location": "bengaluru"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
  - slot{"budgetmax": "300"}
  - slot{"budgetmin": "0"}
  - action_search_restaurants
  - utter_goodbye


## fail_story_2
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "rishikesh"}
  - slot{"location": "rishikesh"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "tokyo"}
  - slot{"location": "tokyo"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
  - slot{"budgetmax": "700"}
  - slot{"budgetmin": "300"}
  - action_search_restaurants
  - utter_goodbye


## fail_story_3
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "shantiniketan"}
  - slot{"location": "shantiniketan"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "tokyo"}
  - slot{"location": "tokyo"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "shantiniketan"}
  - slot{"location": "shantiniketan"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "tokyo"}
  - slot{"location": "tokyo"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "agra"}
  - slot{"location": "agra"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "1000"}
  - slot{"budgetmax": "1000"}
  - slot{"budgetmin": "700"}
  - action_search_restaurants
  - utter_goodbye



## fail_story_4
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "burdhmaan"}
  - slot{"location": "burdhmaan"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "shantiniketan"}
  - slot{"location": "shantiniketan"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "tokyo"}
  - slot{"location": "tokyo"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "shantiniketan"}
  - slot{"location": "shantiniketan"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "tokyo"}
  - slot{"location": "tokyo"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "warangal"}
  - slot{"location": "warangal"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
  - slot{"budgetmax": "300"}
  - slot{"budgetmin": "0"}
  - action_search_restaurants
  - utter_goodbye

## fail_story_5
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "kurg"}
  - slot{"location": "kurg"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "shantiniketan"}
  - slot{"location": "shantiniketan"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "tokyo"}
  - slot{"location": "tokyo"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "shantiniketan"}
  - slot{"location": "shantiniketan"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "tokyo"}
  - slot{"location": "tokyo"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "kolkata"}
  - slot{"location": "kolkata"}
  - action_validate_location
  - slot{"location_ok": true}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
  - slot{"budgetmax": "700"}
  - slot{"budgetmin": "300"}
  - action_search_restaurants
  - utter_goodbye
  
