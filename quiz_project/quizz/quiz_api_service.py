import requests
import html
from datetime import datetime


class QuizEntryInformation:
    def __init__(self, information):
        self.date_of_quiz = information['date_of_quiz']
        self.username = information['username']
        self.amount = information['amount']
        self.category = information['category']
        self.difficulty = information['difficulty']
        self.type = information['type']


class QuizzQuestion:
    def __init__(self, question):
        self.category = question['category']
        self.type = question['type']
        self.difficulty = question['difficulty']
        self.question = question['question']
        self.answers = question['answers']


class QuizzSolution:
    def __init__(self, solution):
        self.question = solution['question']
        self.correct_answer = solution['correct_answer']


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
    datetime.strftime(quiz_information['date_of_quiz'], '%H:%M:%S %d-%b-%Y')
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


# use random to generate the index where the correct answer will be placed
import random

# print(random.randrange(1, 10))
