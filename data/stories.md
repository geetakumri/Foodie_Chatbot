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
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin":"0"}
  - slot{"budgetmax":"300"}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"abc@gmail.com"}
  - slot{"email_id": "abc@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
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
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin":"300"}
  - slot{"budgetmax":"700"}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"abc.com"}
  - slot{"email_id": "abc.com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"abc@gmail.com"}
  - slot{"email_id": "abc@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
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
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"srk@gmail.com"}
  - slot{"email_id": "srk@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "srk@gmail.com"}
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
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":".com"}
  - slot{"email_id": ".com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"abc@gmail.com"}
  - slot{"email_id": "abc@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
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
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"sam123@gmail.com"}
  - slot{"email_id": "sam123@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
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
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"abc@.com"}
  - slot{"email_id": "abc@.com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"abc@gmail.com"}
  - slot{"email_id": "abc@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
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
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"abc@gmail.com"}
  - slot{"email_id": "abc@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
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
* restaurant_search{"budgetmin":"700", "budgetmax":"10000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"10000"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"abc@.com"}
  - slot{"email_id": "abc@.com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"abc@gmail.com"}
  - slot{"email_id": "abc@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
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
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin":"0"}
  - slot{"budgetmax":"300"}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"am123@gmail.com"}
  - slot{"email_id": "am123@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "am123@gmail.com"}
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
* restaurant_search{"budgetmin":"700", "budgetmax":"10000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"10000"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"10000"}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"abc@.com"}
  - slot{"email_id": "abc@.com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"abc@gmail.com"}
  - slot{"email_id": "abc@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
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
* restaurant_search{"budgetmin":"700", "budgetmax":"10000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"10000"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"amit@in.com"}
  - slot{"email_id": "amit@in.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "amit@in.com"}
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
  - slot{"cuisine_ok": false}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"south indian"}
  - slot{"cuisine":"south indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"0", "budgetmax":"300"}
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"dabba@.com"}
  - slot{"email_id": "dabba@.com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"bhai@outlook.com"}
  - slot{"email_id": "bhai@outlook.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "bhai@outlook.com"}
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
* restaurant_search{"budgetmin":"700", "budgetmax":"10000"}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"salamn@yahoo.com"}
  - slot{"email_id": "salman@yahoo.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "salman@yahoo.com"}
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
  - slot{"cuisine":"chinese"}
  - action_validate_cuisine
  - slot{"cuisine_ok":true}
  - slot{"cuisine":"chinese"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax":"700"}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
  * affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"sonam@.com"}
  - slot{"email_id": "sonam@.com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"aasha@gmail.com"}
  - slot{"email_id": "aahsa@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "aasha@gmail.com"}
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
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"aamir1244@gmail.com"}
  - slot{"email_id": "aamir1244@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "aamir1244@gmail.com"}
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
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"aamir1244@gmail.com"}
  - slot{"email_id": "aamir1244@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "aamir1244@gmail.com"}
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
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"srk@outlook.com"}
  - slot{"email_id": "srk@outlook.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "srk@outlook.com"}
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
* restaurant_search{"location": "dhaka"}
  - slot{"location": "dhaka"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "ghana"}
  - slot{"location": "ghana"}
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
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"jhantu@outlook.com"}
  - slot{"email_id": "jhantu@outlook.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "jhantu@outlook.com"}
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
* restaurant_search{"location": "andaman"}
  - slot{"location": "andaman"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "sundarban"}
  - slot{"location": "sundarban"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "marathali"}
  - slot{"location": "marathali"}
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
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 0}
  - slot{"budgetmax": 300}
  - action_search_restaurants
  - utter_whether_to_email
* deny
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
* restaurant_search{"location": "meghalaya"}
  - slot{"location": "meghalaya"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "nawadih"}
  - slot{"location": "nawadih"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "bhuli"}
  - slot{"location": "bhuli"}
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
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* deny
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
* restaurant_search{"location": "bhuli"}
  - slot{"location": "bhuli"}
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
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* deny
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
* restaurant_search{"budgetmin":"700", "budgetmax":"10000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"10000"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"@.com"}
  - slot{"email_id": "@.com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"@com"}
  - slot{"email_id": "@com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"@."}
  - slot{"email_id": "@."}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"sd@.com"}
  - slot{"email_id": "sd@.com"}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"lata@gmail.com"}
  - slot{"email_id": "lata@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "lata@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## budget_fail_story
* greet
  - utter_greet
* restaurant_search{"location":"hampi","cuisine":"thai"}
  - slot{"location":"hampi"}
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
  - slot{"cuisine":"thai"}
  - action_validate_cuisine
  - slot{"cuisine_ok": false}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
  - slot{"cuisine": "north indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"1100", "budgetmax":"1700"}
  - slot{"budgetmin":"1100"}
  - slot{"budgetmax":"1700"}
  - action_validate_budget
  - slot{"budget_ok": false}
  - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax":"700"}
  - slot{"budgetmin":"300"}
  - slot{"budgetmax":"700"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* deny
  - utter_goodbye
  - action_restart

## budget_fail_story
* greet
  - utter_greet
* restaurant_search{"location":"nawada","cuisine":"thai"}
  - slot{"location":"nawada"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "jhumri"}
  - slot{"location": "jhumri"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "Gorakhpur"}
  - slot{"location": "Gorakhpur"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "Gorakhpur"}
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
* restaurant_search{"budgetmin":"1100", "budgetmax":"1700"}
  - slot{"budgetmin":"1100"}
  - slot{"budgetmax":"1700"}
  - action_validate_budget
  - slot{"budget_ok": false}
  - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax":"700"}
  - slot{"budgetmin":"300"}
  - slot{"budgetmax":"700"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* deny
  - utter_goodbye
  - action_restart

## budget_fail_story
* greet
  - utter_greet
* restaurant_search{"location":"koorg","cuisine":"south indian"}
  - slot{"location":"koorg"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "nawadih"}
  - slot{"location": "nawadih"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "warangal"}
  - slot{"location": "warangal"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "warangal"}
  - slot{"cuisine": "south indian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"1100", "budgetmax":"1700"}
  - slot{"budgetmin":"1100"}
  - slot{"budgetmax":"1700"}
  - action_validate_budget
  - slot{"budget_ok": false}
  - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax":"700"}
  - slot{"budgetmin":"300"}
  - slot{"budgetmax":"700"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"abc@gmail."}
  - slot{"email_id": "abc@gmail."}
  - action_validate_email_id
  - slot{"email_ok": false}
  - utter_email_validation_failed
* restaurant_search{"email_id":"abc_3242@gmail.com"}
  - slot{"email_id": "abc_3242@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc_3242@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## budget_fail_story
* greet
  - utter_greet
* restaurant_search{"location":"obra","cuisine":"mexican"}
  - slot{"location":"obra"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "mandi"}
  - slot{"location": "mandi"}
  - action_validate_location
  - slot{"location_ok": false}
  - utter_ask_location
* restaurant_search{"location": "warangal"}
  - slot{"location": "warangal"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location": "warangal"}
  - slot{"cuisine": "mexican"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "mexican"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"1100", "budgetmax":"1700"}
  - slot{"budgetmin":"1100"}
  - slot{"budgetmax":"1700"}
  - action_validate_budget
  - slot{"budget_ok": false}
  - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax":"700"}
  - slot{"budgetmin":"300"}
  - slot{"budgetmax":"700"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 300}
  - slot{"budgetmax": 700}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"abc@gmail.com"}
  - slot{"email_id": "abc@gmail.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "abc@gmail.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## budget_fail_story
  * greet
  - utter_greet
* restaurant_search{"location":"surat","cuisine":"italian"}
  - slot{"location":"surat"}
  - action_validate_location
  - slot{"location_ok": true}
  - slot{"location":"surat"}
  - slot{"cuisine":"italian"}
  - action_validate_cuisine
  - slot{"cuisine_ok": true}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* restaurant_search{"budgetmin":"0", "budgetmax":"30"}
  - slot{"budgetmin":"0"}
  - slot{"budgetmax":"30"}
  - action_validate_budget
  - slot{"budget_ok": false}
  - utter_ask_budget
* restaurant_search{"budgetmin":"700", "budgetmax":"10000"}
  - slot{"budgetmin":"700"}
  - slot{"budgetmax":"10000"}
  - action_validate_budget
  - slot{"budget_ok": true}
  - slot{"budgetmin": 700}
  - slot{"budgetmax": 10000}
  - action_search_restaurants
  - utter_whether_to_email
* affirm
  - utter_ask_email_id
* restaurant_search{"email_id":"sdaabc@yahoo.com"}
  - slot{"email_id": "sdaabc@yahoo.com"}
  - action_validate_email_id
  - slot{"email_ok": true}
  - slot{"email_id": "sdaabc@yahoo.com"}
  - action_send_email
  - utter_goodbye
  - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "japanese", "location": "kolkata"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "kolkata"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmax": "500"}
    - slot{"budgetmax": "500"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": 300}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - slot{"restaurant_exist": false}
    - utter_whether_to_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - utter_ask_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": false}
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": 300}
    - slot{"budgetmin": 0}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id": "srk@gmail.com"}
    - slot{"email_id": "srk@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - slot{"email_id": "srk@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "panagarh"}
    - slot{"location": "panagarh"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Pune"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": 700}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "japanese", "location": "kolkata"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "kolkata"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmax": "500"}
    - slot{"budgetmax": "500"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": 300}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - slot{"restaurant_exist": false}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id":"@"}
    - slot{"email_id": "@"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"email_id":"@6757.com"}
    - slot{"email_id": "@6757.com"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"email_id":"foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - utter_ask_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": false}
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": 300}
    - slot{"budgetmin": 0}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id":"ritu1@gmail.com"}
    - slot{"email_id": "ritu1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - slot{"email_id": "ritu1@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"cuisine": "briyani"}
    - slot{"cuisine": "briyani"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Pune"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": 700}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id":".com"}
    - slot{"email_id": ".com"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"email_id":"123.com"}
    - slot{"email_id": ".com"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"email_id":"@.com"}
    - slot{"email_id": "@.com"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed    
* restaurant_search{"email_id":"surbhi@gmail.com"}
    - slot{"email_id": "surbhi@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - slot{"email_id": "surbhi@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "idly"}
    - slot{"cuisine": "idly"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "briyani"}
    - slot{"cuisine": "briyani"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "hariyanvi"}
    - slot{"cuisine": "hariyanvi"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Agra"}
    - utter_ask_budget
* restaurant_search{"budgetmin": 300, "budgetmax": 700}
    - slot{"budgetmax": 700}
    - slot{"budgetmin": 300}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id":"rock@gmail.com"}
    - slot{"email_id": "rock@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - slot{"email_id": "rock@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_8
* greet  
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "hariyanvi"}
    - slot{"cuisine": "hariyanvi"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "bihari"}
    - slot{"cuisine": "bihari"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "800"}
    - slot{"budgetmin": "800"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmin": 700, "budgetmax": 10000}
    - slot{"budgetmax": 10000}
    - slot{"budgetmin": 700}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id":"@yahoo.com"}
    - slot{"email_id": "@yahoo.com"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"email_id":"sonali@gmail.com"}
    - slot{"email_id": "sonali@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - slot{"email_id": "sonali@gmail.com"}
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "panagarh"}
    - slot{"location": "panagarh"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300"}
    - slot{"budgetmin": 300}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id":"foodieChatbot1@gmail.com"}
    - slot{"email_id": "foodieChatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - slot{"email_id": "foodieChatbot1@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "marwari", "location": "koorg"}
    - slot{"cuisine": "marwari"}
    - slot{"location": "koorg"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Surat"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Greek"}
    - slot{"cuisine": "Greek"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Tea"}
    - slot{"cuisine": "Tea"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Healthy Food"}
    - slot{"cuisine": "Healthy Food"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "russain"}
    - slot{"cuisine": "russain"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "briyani"}
    - slot{"cuisine": "briyani"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Coffee"}
    - slot{"cuisine": "Coffee"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "1500", "budgetmax": "2000"}
    - slot{"budgetmax": "2000"}
    - slot{"budgetmin": "1500"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmin": 300, "budgetmax": 700}
    - slot{"budgetmax": 700}
    - slot{"budgetmin": 300}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Surat"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* restaurant_search{"email_id": "ahc@.com"}
    - slot{"email_id": "ahc@.com"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"emai_id": "am@."}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_21
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pond"}
    - slot{"location": "pond"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexicon"}
    - slot{"cuisine": "mexicon"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "mexicon"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0"}
    - slot{"budgetmin": 0}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id": "foodiechat1@.com"}
    - slot{"email_id": "foodiechat1@.com"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Delhi"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700"}
    - slot{"budgetmin": 700}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 100000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_23
* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "dubai"}
    - slot{"location": "dubai"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Mathura"}
    - slot{"location": "Mathura"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Mathura"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budgetmin": 300, "budgetmax": 700}
    - slot{"budgetmax": 700}
    - slot{"budgetmin": 300}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - utter_whether_to_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_24
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Agra", "budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Agra"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Agra"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "North Indian"}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_25
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Jaipur", "budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Jaipur"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Jaipur"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "South Indian"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_26
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "location": "Kolkata", "budgetmax": "300"}
    - slot{"budgetmin": 0}
    - slot{"budgetmax": "300"}
    - slot{"cuisine": "American"}
    - slot{"location": "Kolkata"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Kolkata"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "American"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_27
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Jaipur", "budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Jaipur"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Jaipur"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "Mexican"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_28
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai", "location": "Delhi", "budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - slot{"cuisine": "Thai"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "North Indian"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_29
* greet
    - utter_greet
* restaurant_search{"cuisine": "Japanese", "location": "Surat", "budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - slot{"cuisine": "Japanese"}
    - slot{"location": "Surat"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Surat"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "North Indian"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_30
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai", "location": "Delhi", "budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - slot{"cuisine": "Thai"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "North Indian"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_31
* greet
    - utter_greet
* restaurant_search{"cuisine": "burger", "location": "Delhi", "budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - slot{"cuisine": "burger"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "North Indian"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_32
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai", "location": "Surat"}
    - slot{"cuisine": "Thai"}
    - slot{"location": "Surat"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Surat"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - utter_whether_to_email
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_33
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai", "location": "Delhi", "budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - slot{"cuisine": "Thai"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - action_validate_cuisine
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "Italian"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* deny
    - utter_goodbye
    - action_restart



## interactive_story_34
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Amethi", "budgetmin": "300"}
    - slot{"budgetmin": "300"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Amethi"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Ajmer"}
    - slot{"location": "Ajmer"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Ajmer"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "Italian"}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Ajmer"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* email_id{"email_id": "g1@.in"}
    - slot{"email_id": "g1@.in"}
    - action_validate_email_id
    - slot{"email_ok": false}
    - utter_email_validation_failed
* restaurant_search{"email_id": "foodiechatbot1@gmail.com"}
    - slot{"email_id": "foodiechatbot1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_35
* greet
    - utter_greet
* restaurant_search{"location": "Bhilai", "cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Bhilai"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Bhilai"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budgetmin": 300, "budgetmax": 700}
    - slot{"budgetmax": 700}
    - slot{"budgetmin": 300}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Bhilai"}
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* deny{"deny": "nop"}
    - utter_goodbye
    - action_restart

## interactive_story_36
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "koorg"}
    - slot{"location": "koorg"}
    - action_validate_location
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine_ok": true}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": 300, "budgetmax": 700}
    - slot{"budgetmax": 700}
    - slot{"budgetmin": 300}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_whether_to_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email_id": "foodiechatbo1@gmail.com"}
    - slot{"email_id": "foodiechatbo1@gmail.com"}
    - action_validate_email_id
    - slot{"email_ok": true}
    - action_send_email
    - utter_goodbye
    - action_restart
