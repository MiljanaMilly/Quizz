import requests
import json


class OpenDBTriviaQuestion:
    def __init__(self, question):
        self.category = question['category']
        self.type = question['type']
        self.difficulty = question['difficulty']
        self.question = question['question']
        self.correct_answer = question['correct_answer']
        self.incorrect_answers = question['incorrect_answers']


def get_quiz_data(form_params):
    odb_trivia_url = 'https://opentdb.com/api.php'
    try:
        response = requests.get(odb_trivia_url, params=form_params)
        response.raise_for_status()
        quiz_data_json = response.json()
        convertedQuizObject = convert_quiz_to_object(quiz_data_json)
        return convertedQuizObject

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print("Something went wrong, Open Trivia API not found.Please try again!")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise print("Something went wrong.Please try again!")
    # parseQuix data and return it with quizz view


def convert_quiz_to_object(quiz_data_json):
    quiz_result = quiz_data_json['results']
    questions = [OpenDBTriviaQuestion(question) for question in quiz_result]
    return questions


# use random to generate the index where the correct answer will be placed
import random

# print(random.randrange(1, 10))
