import requests

# Trivia API URL
api_url = 'https://opentdb.com/api.php'
categories = 'https://opentdb.com/api_category.php'

categories_response = requests.get(url = categories)
categories= categories_response.json()

# Use List Comprehension to return just the category options

#categories_list = [dic['name'] for dic in categories['trivia_categories']]

categories_list = ["General Knowledge", "Animals", "Art", "Politics","History"]
categories_dict ={
"General Knowledge" : 9,
"Animals" : 10,
"Art" : 25,
"Politics" : 24,
"History" : 23


}

