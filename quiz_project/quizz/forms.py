from django import forms
from datetime import datetime


class QuizEntryForm(forms.Form):
    date_of_quiz = forms.DateTimeField(initial=datetime.now,
                                       widget=forms.HiddenInput())

    username = forms.CharField(label='Korisn. ime',
                               min_length=2,
                               max_length=25,
                               required=True)

    AMOUNT_CHOICES = (
        ('5', '5'),
        ('10', '10'),
        ('15', '15')
    )

    amount = forms.ChoiceField(
        label='Broj pitanja',
        choices=AMOUNT_CHOICES,
    )

    CATEGORY_CHOICES = (
        ('17', 'Nauka'),
        ('12', 'Muzika'),
        ('11', 'Film'),
        ('9', 'Opste obrazovanje'),
        ('23', 'Istorija'),
    )

    category = forms.ChoiceField(
        label='Kategorija',
        choices=CATEGORY_CHOICES
    )

    DIFFICULTY_CHOICES = (
        ('easy', 'Lako'),
        ('medium', 'Srednje'),
        ('hard', 'Teško')
    )

    difficulty = forms.ChoiceField(
        label='Težina',
        choices=DIFFICULTY_CHOICES
    )

    type = forms.CharField(
        initial='multiple',
        max_length=8,
        widget=forms.HiddenInput()
    )
