def create_session_variables(session, question_category_list):
    # 0 correct / 0 incorrect
    session['user_correct_answers'] = 0
    session['user_wrong_answers'] = 0

    # Question <num> of <num>
    session['number_of_questions'] = len(question_category_list)
    session['current_question'] = 0

    session['used_categories'] = []

    session['correct_answer'] = 0


def update_session_variables(session):
    # 0 correct / 0 incorrect
    session['user_correct_answers'] = session.get('user_correct_answers')
    session['user_wrong_answers'] = session.get('user_wrong_answers')

    # Question <num> of <num>
    # update a few session variables at once
    if session['current_question'] == session['number_of_questions']:
        session['current_question'] = 1
        session['used_categories'] = []
        session['user_correct_answers'] = 0
        session['user_wrong_answers'] = 0
    else:
        session['current_question'] = session.get('current_question') + 1
    

    session['used_categories'] = session.get('used_categories')

    session['correct_answer'] = session.get('correct_answer')


# called from get_questions_and_category_options
def update_used_categories(session, category):
    session['used_categories'] = session.get('used_categories')
    session['used_categories'].append(category)
    


