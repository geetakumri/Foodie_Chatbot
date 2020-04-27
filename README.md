# Foodie_Chatbot

# Problem Statement

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product.

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

### The bot takes the following inputs from the user:

- **City:** Take the input from the customer as a text field.
	- Assume that Foodie works only in Tier-1 and Tier-2 cities. 
    - We have used the provided link :  https://en.wikipedia.org/wiki/Classification_of_Indian_cities .Under the   section 'current classification' on this page, the table categorizes cities as X, Y and Z. Consider 'X ' cities as tier-1 and 'Y' as tier-2. 
	- The bot should be able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.

- **Cuisine Preference:** Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that. 

- **Average budget for two people:** Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories.


Based on the given input by user for  location, cuisine and budget, bot will show top 5 restaurants with decreasing restaurant rating.

- **Email with top 10 restaurant:** 
user can agree to get the restaurant details or can deny . So, bot will send the mail only if the user agrees.
Note: We have created a dummy email it to send emails for Foodie. 


-**A sample coversation with the bot :**

Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  hello
hey there! How may i help you?
Your input ->  looking for restaurant in Dilli
? what kind of cuisine would you like?  3: South Indian (South Indian)
? What price range are you looking for?  3: More than 700 (/restaurant_search{"budgetmin":700,"budgetmax":10000})
Showing you top rated restaurants in your desired location :

Restaurant Name: Master Koii's
Address: Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon
The average price for two people: Rs. 1800
Rating: 4.8

Restaurant Name: Cafe Wink
Address: G-1, Plot 9, Sikka Galaxy, Shreshtha Vihar, Anand Vihar, New Delhi
The average price for two people: Rs. 800
Rating: 4.7

Restaurant Name: Nona's Kitchen
Address: A 224, Ground Floor, Supermart 1, DLF Phase 4, Gurgaon
The average price for two people: Rs. 1000
Rating: 4.6

Restaurant Name: Bukhara - ITC Maurya
Address: ITC Maurya, Chanakyapuri, New Delhi
The average price for two people: Rs. 6500
Rating: 4.6

Restaurant Name: Bhookemon
Address: F-329, Lado Sarai, New Delhi
The average price for two people: Rs. 800
Rating: 4.5
Should I send you details of all the restaurants on email?
Your input ->  foodiechatbot1@gmail.com
Restaurants list has been sent to your email id. Bon Appétit!!
Thank you for choosing Foodie. Good Bye

# Rasa Installation

Follow the installation guide at https://rasa.com/docs/rasa/user-guide/installation/

# Training and testing NLU model
 - 'rasa train' command to train the model
 - 'run rasa action' command in another window to keep the server up
 - 'rasa shell' to test the model . We can also use 'rasa interactive' command to validate and create stories.

# List of updater version used in this project

- Python 3.7.4
- pip 20.0.2
- Rasa 1.9.6