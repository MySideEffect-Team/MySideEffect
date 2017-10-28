#!/usr/bin/python3
from django import forms

# Sign up and Profile Settings

# General information
GENDER = [
    ('female', 'Female'),
    ('male', 'Male'),
    ('other', 'Other'), ]

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
    ('over', 'More than three times a week'), ]

EATING = [
    ('meat', 'Regular'),
    ('veggie', 'Vegetarian'),
    ('vegan', 'Vegan'), ]

CHILDREN = [
    ('none', 'No children'),
    ('1', 'One child'),
    ('2', 'Two children'),
    ('3', 'Three children'),
    ('more', 'Four or more children'),
]


class UserForm(forms.Form):

    # General

    # username = forms.CharField(max_length=100)
    # email = forms.CharField(max_length=100)
    # email2 = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)
    # password2 = forms.CharField(max_length=100)
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    gender = forms.CharField(label='What is your Gender?', widget=forms.RadioSelect(choices=GENDER))
    age = forms.ChoiceField(label='How old are you?', choices=AGE, required=True)
    location = forms.ChoiceField(label='Where do you live?', required=True, choices=LOCATION)

    # Lifestyle

    sports = forms.ChoiceField(label='How often do you do sports?',
                               required=True, choices=SPORTS)

    eating = forms.ChoiceField(label='What are your eating habits?',
                               required=True, choices=EATING)
    smoking = forms.BooleanField(label='Are you a smoker?', initial=False)
    drinking = forms.BooleanField(label='Do you drink alcohol?', initial=False)

    # Medical history

    pregnant = forms.BooleanField(label='Are you pregnant', initial=False)
    drugs = forms.CharField(label='List all drugs you currently take (single line for each)', widget=forms.Textarea)
    allergies = forms.CharField(label='List of allergies and chronic diseases (single line each)', widget=forms.Textarea)
    nodrugs = forms.CharField(label='Do not include the following drugs (single line each)', widget=forms.Textarea)
    children = forms.ChoiceField(label='Do you have children', required=True, choices=CHILDREN)
