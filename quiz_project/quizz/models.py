from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=35)
    date_of_entry = models.DateField()

    def __str__(self):
        return f"Igrač, {self.username}, se prvi put prijavio {self.date_of_entry}."


class Score(models.Model):
    date_of_quiz = models.DateTimeField(auto_now_add=True)
    num_questions = models.IntegerField()

    class Category(models.TextChoices):
        NAUKA = 'NA', 'Nauka'
        MUZIKA = 'MU', 'Muzika'
        FILM = 'FM', 'Film'

    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.FILM,
    )

    class Level(models.TextChoices):
        LAKO = 'L', 'Lako'
        SREDNJE = 'S', 'Srednje'
        TESKO = 'T', 'Teško'

    difficulty = models.CharField(
        max_length=2,
        choices=Level.choices,
        default=Level.SREDNJE,
    )

    class Type(models.TextChoices):
        MULTIPLE_CHOICE = 'MC', 'Jedan od ponuđenih'
        TF = 'TF', 'Tačno/Netačno'

    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.MULTIPLE_CHOICE,
    )

    score = models.IntegerField()

    player = models.ForeignKey(Player, on_delete=models.CASCADE)



class QuizEntry(models.Model):
    date_of_quiz = models.DateTimeField(auto_now_add=True)
    # def __init__(self, username, num_of_questions, category, difficulty, quizType):
    #     self._username = username
    #     self._num_of_questions = num_of_questions
    #     self._category = category
    #     self._difficulty = difficulty
    #     self._type = quizType

    username = models.CharField(max_length=25)

    class QuestionNum(models.IntegerChoices):
        FIVE = 5, '5'
        TEN = 10, '10'
        FIFTEEN = 15, '15'

    num_of_questions = models.IntegerField(
        choices=QuestionNum.choices,
        default=QuestionNum.FIVE,
    )

    class Category(models.TextChoices):
        NAUKA = 'NA', 'Nauka'
        MUZIKA = 'MU', 'Muzika'
        FILM = 'FM', 'Film'
        OPSTE_OBRAZOVANJE = 'OO', 'Opste obrazovanje'
        ISTORIJA = 'IS', 'Istorija'

    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.FILM,
    )

    class Level(models.TextChoices):
        LAKO = 'L', 'Lako'
        SREDNJE = 'S', 'Srednje'
        TESKO = 'T', 'Teško'

    difficulty = models.CharField(
        max_length=2,
        choices=Level.choices,
        default=Level.SREDNJE,
    )

    class Type(models.TextChoices):
        MULTIPLE_CHOICE = 'MC', 'Jedan od ponuđenih'
        TF = 'TF', 'Tačno/Netačno'

    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.MULTIPLE_CHOICE,
    )


