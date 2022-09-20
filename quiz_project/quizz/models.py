from django.db import models
from django.utils.text import slugify



class Player(models.Model):
    username = models.CharField(max_length=35)
    date_of_entry = models.DateField()


    class Meta:
        ordering = ['username']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            # we call models save method and save it to database
            # it is common
        return super(). save(*args, **kwargs)

    def __str__(self):
        return self.username


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


