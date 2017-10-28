#!/usr/bin/python3
from django import forms

# Sign up and Profile Settings

# General information
GENDER = [
    ('female', 'Female'),
    ('male', 'Male'), ]

AGE = [
    ('under', 'Under 25'),
    ('35', '25-35'),
    ('50', '36-50'),
    ('65', '51-65'),
    ('80', '66-80'),
    ('over', 'Over 80'), ]

LOCATION = [
    ('asia', 'Asia'),
    ('america', 'America'),
    ('europe', 'Europe'),
    ('africa', 'Africa'), ]

# Lifestlye information
SPORTS = [
    ('not', 'Not at all'),
    ('1', 'Once a week'),
    ('2', 'Twice a week'),
    ('3', 'Thrice a week'),
    ('over', 'More than three times a week'),
]


class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email1 = forms.CharField(max_length=100)
    email2 = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    gender = forms.CharField(label='What is your Gender?', widget=forms.RadioSelect(choices=GENDER))
    age = forms.CharField(label='How old are you?',
                          widget=forms.ChoiceField(choices=AGE, required=True))
    location = forms.CharField(label='Where do you live?',
                               widget=forms.ChoiceField(choices=LOCATION, required=True))
