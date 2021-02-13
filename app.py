from flask import Flask, render_template, url_for, request, session
from get_questions_and_category_options import *
from session_variables import create_session_variables, update_session_variables

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XYZ'

data = get_data_from_json_file()
question_categories_list = get_question_categories(data)

@app.route('/', methods=['GET', 'POST'])
def start():
    if 'session_variables_created' not in globals():
        globals()['session_variables_created'] = True 
        create_session_variables(session, question_categories_list)
    
    if request.method == 'GET':
        show_answer = False
        
        update_session_variables(session)

        info = create_question_dict(data, question_categories_list, session)
        session['question_dict'] = info[0]
        # set the correct answer
        session['correct_answer'] = info[1]

        session['options'] = shuffle_button_options(info[0])
    
        return render_template('index.html', show_answer=show_answer, S=session)
        
    if request.method == 'POST':
        show_answer = True 
        # create the request dictionary
        request_dict = {}
        for item in request.form.items():
            request_dict['value'] = int(item[1])

        # set is_correct variable for answer.html file
        if request_dict['value'] == session['correct_answer']:
            session['user_correct_answers'] = session.get('user_correct_answers') + 1
            is_correct = True 
        else:
            session['user_wrong_answers'] = session.get('user_wrong_answers') + 1
            is_correct = False
        
        # set the button value to "NEXT QUESTION" or "START OVER"
        if session.get('current_question') == session['number_of_questions']:
            button_value = "START OVER"
        else:
            button_value = "NEXT QUESTION"

        return render_template('index.html', show_answer=show_answer, S=session, is_correct=is_correct, B_value=button_value)
    


if __name__ == '__main__':
    app.run(debug=True)