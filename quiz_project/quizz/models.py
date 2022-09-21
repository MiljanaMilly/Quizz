from django.db import models


# models
class QuizResult(models.Model):
    username = models.CharField(max_length=35)
    date_of_quizz = models.DateTimeField()
    score = models.IntegerField()

    def __str__(self):
        return self.username + ' ' + str(self.score) + ' ' + str(self.date_of_quizz)


# transfer objects
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
