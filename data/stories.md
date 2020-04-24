## story_1
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location":"bengaluru"}
  - slot{"location":"bengaluru"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "bengaluru"}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"south indian"}
  - slot{"cuisine":"south indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"0", "budgetmax":"300"}
  - slot{"budgetmin":"0"}
  - slot{"budgetmax":"300"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"abc@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

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
  - slot{"location": "bengaluru"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
  - slot{"budgetmax": "300"}
  - slot{"budgetmin": "0"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"efg.cdf@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_3
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "agra"}
  - slot{"location": "agra"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "agra"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - slot{"cuisine": "american"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
  - slot{"budgetmax": "700"}
  - slot{"budgetmin": "300"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"efg.cdf@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_4
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "kolkata"}
  - slot{"location": "kolkata"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "kolkata"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
  - slot{"cuisine": "north indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "1000"}
  - slot{"budgetmax": "1000"}
  - slot{"budgetmin": "700"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"efg.cdf@yahoo.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_5
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "delhi"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - slot{"cuisine": "south indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "1000"}
  - slot{"budgetmax": "1000"}
  - slot{"budgetmin": "700"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"sam123@outlook.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

  ## story_6
* greet
  - utter_greet
* restaurant_search{"location":"bengaluru"}
  - slot{"location":"bengaluru"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "bengaluru"}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"indian"}
  - slot{"cuisine":"indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": false}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"north indian"}
  - slot{"cuisine":"north indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"0", "budgetmax":"300"}
  - slot{"budgetmin":"0"}
  - slot{"budgetmax":"300"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"sam123@outlook.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_7
* greet
  - utter_greet
* restaurant_search{"location":"agra"}
  - slot{"location":"agra"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "agra"}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"italian"}
  - slot{"cuisine":"italian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine":"italian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax":"700"}
  - slot{"budgetmin":"300"}
  - slot{"budgetmax":"700"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"asha@yahoo.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_8
* greet
  - utter_greet
* restaurant_search{"location":"kolkata"}
  - slot{"location":"kolkata"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "kolkata"}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"american"}
  - slot{"cuisine":"american"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine":"american"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"700", "budgetmax":"1000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"1000"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"shan@yahoo.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

  ## story_9
* greet
  - utter_greet
* restaurant_search{"location":"agra","cuisine":"italian"}
  - slot{"location":"agra"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "agra"}
  - slot{"cuisine":"italian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"0", "budgetmax":"300"}
  - slot{"budgetmin":"0"}
  - slot{"budgetmax":"300"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"srk@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_10
* greet
  - utter_greet
* restaurant_search{"location":"surat","cuisine":"mexican"}
  - slot{"location":"surat"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "surat"}
  - slot{"cuisine":"mexican"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "mexican"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"700", "budgetmax":"1000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"1000"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"aamir@outlook.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_11
* greet
  - utter_greet
* restaurant_search{"location":"mumbai","cuisine":"north indian"}
  - slot{"location":"mumbai"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "mumbai"}
  - slot{"cuisine":"north indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"700", "budgetmax":"1000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"1000"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"amit@in.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_12
* greet
  - utter_greet
* restaurant_search{"location":"delhi","cuisine":"japenese"}
  - slot{"location":"delhi"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "delhi"}
  - action_validate_cuisine
  - slot{"location_ok": false}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"south indian"}
  - slot{"cuisine":"south indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"700", "budgetmax":"1000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"1000"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"amit123@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_13
* greet
  - utter_greet
* restaurant_search{"location":"koorg","cuisine":"italian"}
  - slot{"location": "koorg"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"dumri"}
  - slot{"location":"dumri"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"jamtara"}
  - slot{"location":"jamtara"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"suri"}
  - slot{"location":"suri"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"birbhum"}
  - slot{"location":"birbhum"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"kolkata"}
  - slot{"location":"kolkata"}
  - action_validate_location
  - slot{"location_ok":true}
  - slot{"location":"kolkata"}
  - slot{"cuisine":"italian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"700", "budgetmax":"1000"}
  - slot{"budgetmax":1000}
  - slot{"budgetmin":700}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"salaman@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_14
* greet
  - utter_greet  
* restaurant_search{"location":"koorg","cuisine":"chines"}
  - slot{"location":"koorg"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"ooty"}
  - slot{"location":"ooty"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"gaya"}
  - slot{"location":"gaya"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"lahore"}
  - slot{"location":"lahore"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"karachi"}
  - slot{"location":"karchi"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"kolkata"}
  - slot{"location":"kolkata"}
  - action_validate_location
  - slot{"location_ok":true}
  - slot{"location":"kolkata"}
  - slot{"cuisine":"south indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok":true}
  - slot{"cuisine":"south indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax":"700"}
  - slot{"budgetmax":700}
  - slot{"budgetmin":300}
  - action_search_restaurants
  - utter_ask_email_id
  * restaurant_search{"email_id":"aamir@yahoo.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## story_15
* greet
  - utter_greet
* restaurant_search{"location":"koorg","cuisine":"Italian"}
  - slot{"location":"koorg"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location":"bombay"}
  - slot{"location":"mumbai"}
  - action_validate_location
  - slot{"location_ok":true}
  - slot{"cuisine":"Italian"}
  - action_validate_cuisine
  - slot{"cuisine_ok":true}
  - slot{"cuisine":"Italian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"0", "budgetmax":"300"}
  - slot{"budgetmax":300}
  - slot{"budgetmin":0}
  - action_search_restaurants
  - utter_ask_email_id
  * restaurant_search{"email_id":"aamir1234@yahoo.com"}
  - action_send_email
  - utter_goodbye
  - action_restart


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
  - slot{"location": "bengaluru"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - action_validate_cuisine
  - slot{"cuisine_ok":true}
  - slot{"cuisine":"chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
  - slot{"budgetmax": "300"}
  - slot{"budgetmin": "0"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"srk@yahoo.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

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
  - slot{"location": "delhi"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
  - slot{"budgetmax": "700"}
  - slot{"budgetmin": "300"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"srk@outlook.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

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
  - slot{"location": "agra"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "1000"}
  - slot{"budgetmax": "1000"}
  - slot{"budgetmin": "700"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"srk@outlook.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

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
  - slot{"location": "warangal"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - slot{"cuisine": "chinese"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
  - slot{"budgetmax": "300"}
  - slot{"budgetmin": "0"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"sid@outlook.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

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
  - slot{"location": "kolkata"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - slot{"cuisine": "american"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
  - slot{"budgetmax": "700"}
  - slot{"budgetmin": "300"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"sid@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

  ## fail_story_6
* greet
  - utter_greet
* restaurant_search{"location":"koorg","cuisine":"south indian"}
  - slot{"location":"koorg"}
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
  - slot{"location": "kolkata"}
  - slot{"cuisine":"thai"}
  - action_validate_cuisine
  - slot{"cuisine_ok": false}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - slot{"cuisine": "south indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax":"700"}
  - slot{"budgetmin":"300"}
  - slot{"budgetmax":"700"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"srk@yahoo.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

  ## fail_story_7
* greet
  - utter_greet
* restaurant_search{"location":"asansol","cuisine":"north indian"}
  - slot{"location":"asansol"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "jharia"}
  - slot{"location": "jharia"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "hampi"}
  - slot{"location": "hampi"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "Lucknow"}
  - slot{"location": "Lucknow"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "Lucknow"}
  - slot{"cuisine":"north indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"700", "budgetmax":"1000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"1000"}
  - action_search_restaurants
  - utter_ask_email_id
* restaurant_search{"email_id":"jhantu@outlook.com"}
  - action_send_email
  - utter_goodbye
  - action_restart