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
            form_gender = form.cleaned_data["gender"]
            form_location = form.cleaned_data["location"]

            res_list = Occurence.objects.filter(age__lte=form_age).filter(age__gte=form_age)
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
