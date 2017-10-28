from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import Occurence


# Create your views here.

def home(request):
    """
    homsite with two forms:
        1. personal information / medical history
        2. symptom
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form_weight = form.cleaned_data["weight"]
            form_age = form.cleaned_data["age"]

            if "-" in form_age:
                lower_age, upper_age = map(int, form_age.split("-"))
            else:
                if form_age.startswith("under"):
                    lower_age = 0
                    upper_age = int(form_age.lstrip("under"))
                elif form_age.startswith("over"):
                    lower_age = int(form_age.lstrip("under"))
                    upper_age = 1000
                else:
                    raise ValueError("Invalid age specified!")

            form_gender = form.cleaned_data["gender"]
            form_location = form.cleaned_data["location"]

            res_list = Occurence.objects.filter(age__lte=upper_age).filter(age__gte=lower_age)
            return render(request, 'MySideEffectApp/result.html', {'res_list': res_list})

    personal_info_form = UserForm()
    #symptom_form = MedicalForm()

    return render(request, 'MySideEffectApp/home.html', {
        'personal_info_form': personal_info_form,
        #'symptom_form': symptom_form,
        })

def about(request):
    return render(request, 'MySideEffectApp/about.html')

def search(request, question_id):
    pass
def results(request, question_id):
    pass
def vote(request, question_id):
    pass
