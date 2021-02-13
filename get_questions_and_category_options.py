import json
import random
from session_variables import update_used_categories

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '×': lambda x, y: x * y,
    '%': lambda x, y: x % y,
    '÷': lambda x, y: x // y
}

# function runs once
def get_data_from_json_file():
    data = open('questions.json')
    quotes_dict = json.load(data) 
    
    # close the connection to json file
    data.close()
    return quotes_dict 

# function runs once
def get_question_categories(data):
    question_categories_list = [] 
    for item in data:
        question_categories_list.append(item)

    return question_categories_list 

def shuffle_button_options(question_dict):
    # create the options
    options_list = ["correctAnswer", "firstIncorrectAnswer", "secondIncorrectAnswer"]
    random.shuffle(options_list)
    options_dict = {}
    for item in options_list:
        options_dict[item] = question_dict[item]

    return options_dict

def create_question_dict(quotes_dict, question_categories_list, session):
    
    question_dict = {}

    # Get the category for the question object (randomly)
    question_category = ' '.join(random.choices(question_categories_list))
    while question_category in session['used_categories']:
        # Get the category for the question object (randomly)
        question_category = ' '.join(random.choices(question_categories_list))

    # update list in session[used_categories]
    update_used_categories(session, question_category)
    # get the dictionary object needed for index.html
    question_dict = quotes_dict[question_category][0]

    first_num = question_dict['leftAdder']
    second_num = question_dict['rightAdder']
    sign = question_dict['sign']
    
    correct_answer = operators[sign](first_num,second_num)

    return question_dict, correct_answer
    