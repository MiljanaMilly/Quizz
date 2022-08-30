import requests


def get_quiz_data(form_params):
    odb_trivia_url = 'https://opentdb.com/api.php'
    try:
        response = requests.get(odb_trivia_url, params=form_params)
        response.raise_for_status()
        quiz_data = response.json()
        return quiz_data

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print("Something went wrong, Open Trivia API not found.Please try again!")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise print("Something went wrong.Please try again!")
    # parseQuix data and return it with quizz view

# def convert_quiz_to_object(quiz_json_data):
