from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# from .forms import UserForm, MedicalForm

# from .models import Symptom


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
            return render(request, )
    #personal_info_form = UserForm()
    #symptom_form = MedicalForm()

    return render(request, 'MySideEffectApp/home.html', {
        #'personal_info_form': personal_info_form,
        #'symptom_form': symptom_form,
        })



def search(request, question_id):
    pass
def results(request, question_id):
    pass
def vote(request, question_id):
    pass
