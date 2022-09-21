import requests
import html
from datetime import datetime
from django.utils.timezone import make_aware
from quizz.models import QuizResult, QuizzQuestion, QuizEntryInformation, QuizzSolution


# Quiz Entry
def get_quiz_data(form_params):
    odb_trivia_url = 'https://opentdb.com/api.php'
    try:
        response = requests.get(odb_trivia_url, params=form_params)
        response.raise_for_status()
        quiz_data_json = response.json()
        collected_solutions = collect_solutions(quiz_data_json['results'])
        converted_quiz_questions = convert_quiz_questions(quiz_data_json)
        converted_quiz_information = convert_quiz_information(form_params)
        quiz = {'questions': converted_quiz_questions,
                'information': converted_quiz_information,
                'solution': collected_solutions}
        return quiz

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print("Something went wrong, Open Trivia API not found.Please try again!")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise print("Something went wrong.Please try again!")


def convert_quiz_information(quiz_information):
    quiz_information['date_of_quiz'] = datetime.strftime(quiz_information['date_of_quiz'], '%d %b, %Y, %I:%M:%S %p')
    return QuizEntryInformation(quiz_information)


def convert_quiz_questions(quiz_data_json):
    quiz_questions_data = transform_answers(quiz_data_json['results'])
    questions_list = [QuizzQuestion(question) for question in quiz_questions_data]
    for question in questions_list:
        question.question = html.unescape(question.question)
    return questions_list


def collect_solutions(quiz_questions_data):
    solutions_list = [QuizzSolution(question) for question in quiz_questions_data]
    return solutions_list


def transform_answers(quiz_questions_data):
    for question in quiz_questions_data:
        # creating a set of answers, because it is mutable and unordered(will randomize the answers)
        answers_set = set(question['incorrect_answers'])
        answers_set.add(question['correct_answer'])
        question['answers'] = answers_set
        # removing answers from response
        question.pop('incorrect_answers')
        question.pop('correct_answer')
    return quiz_questions_data


# Quiz Submission
def process_quiz_results(quiz_results):
    username = quiz_results['username']
    date_of_quizz = quiz_results['date_of_quiz']
    solution = {key[9:]: value for key, value in quiz_results.items() if 'solution-' in key}
    user_input = {key[11:]: value for key, value in quiz_results.items() if 'user_input-' in key}
    score = calculate_score(solution, user_input)
    save_quiz_score(username, date_of_quizz, score)
    return QuizResult(username=username, date_of_quizz=date_of_quizz,  score=score)


def calculate_score(solution, completed):
    score = 0
    for key in solution.keys() & completed.keys():
        if completed[key] == solution[key]:
            score += 10
    return score


def save_quiz_score(username, date_of_quizz, score):
    formatted_datetime = datetime.strptime(date_of_quizz, '%d %b, %Y, %I:%M:%S %p')
    aware_formatted_datetime = make_aware(formatted_datetime)
    quizz_result = QuizResult(username=username, date_of_quizz=aware_formatted_datetime, score=score)
    quizz_result.save()

