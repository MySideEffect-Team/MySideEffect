#!/usr/bin/python3
from django import forms

# Sign up and Profile Settings

# General information
GENDER = [
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Other', 'Other'), ]

AGE = [
    ('under25', 'Under 25'),
    ('25-35', '25-35'),
    ('36-50', '36-50'),
    ('51-65', '51-65'),
    ('66-80', '66-80'),
    ('over80', 'Over 80'), ]

LOCATION = [
    ('Asia', 'Asia'),
    ('America', 'America'),
    ('Europa', 'Europe'),
    ('Africa', 'Africa'), ]

# Lifestlye information
SPORTS = [
    ('not', 'Not at all'),
    ('once', 'Once a week'),
    ('twice', 'Twice a week'),
    ('thrice', 'Thrice a week'),
    ('overthreetimes', 'Over thrice a week'), ]

MEAT = [
    ('not', 'Not at all'),
    ('1', '1'),
    ('2', '2'),
    ('over3', '3 or more'), ]

CHILDREN = [
    ('not', 'No child'),
    ('1', 'One child'),
    ('2', 'Two children'),
    ('3', 'Three children'),
    ('over3', 'Four or more children'), ]

WEIGHT = [
    ('under35', 'Under 35'),
    ('35-50', '35-50'),
    ('51-65', '51-65'),
    ('66-80', '66-80'),
    ('81-95', '81-95'),
    ('over95', 'Over 95'), ]


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

    gender = forms.CharField(label='What is your Gender', widget=forms.RadioSelect(choices=GENDER), required=False)
    age = forms.ChoiceField(label='How old are you', choices=AGE, required=False)
    weight = forms.ChoiceField(label='How much do you weigh', required=False, choices=WEIGHT)
    location = forms.ChoiceField(label='Where do you live', required=False, choices=LOCATION)

    # Lifestyle

    sports = forms.ChoiceField(label='How often do you do sports', required=False, choices=SPORTS)

    veggie = forms.BooleanField(label='Do you eat meat', initial=True,
                                required=False)
    eating = forms.ChoiceField(label='How often do you eat meat', required=False, choices=MEAT)

    smoking = forms.BooleanField(label='Are you a smoker', initial=False,
                                 required=False)
    drinking = forms.BooleanField(label='Do you drink alcohol', initial=False,
                                  required=False)

    # Medical history

    drugs = forms.CharField(label='List all drugs you currently take (single line for each)', widget=forms.Textarea, required=False)
    allergies = forms.CharField(label='List of allergies and chronic diseases (single line each)', widget=forms.Textarea, required=False)
    nodrugs = forms.CharField(label='Exclude following drugs / Allergic to (single line each)', widget=forms.Textarea, required=False)
    pregnant = forms.BooleanField(label='Are you pregnant', initial=False, required=False)
    children = forms.ChoiceField(label='Have children? If yes how many', required=False, choices=CHILDREN)

    # Symptoms

    # symptoms = forms.CharField(label='Symptoms', max_length=200, required=True, widget=forms.Textarea)


class SignUp(UserForm):

    # General

    username = forms.CharField(max_length=100)
    # email = forms.CharField(max_length=100)
    # email2 = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    # password2 = forms.CharField(max_length=100)
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    email = forms.EmailField()


class Search(forms.Form):
    search_drug = forms.CharField(max_length=50)
