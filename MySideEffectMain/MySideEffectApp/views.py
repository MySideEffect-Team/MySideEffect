from django.shortcuts import render

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

            def format_age_weight(form_info):
                if "-" in form_info:
                    return tuple(map(int, form_info.split("-")))
                else:
                    if form_info.startswith("under"):
                        return 0, int(form_info.lstrip("under"))
                    elif form_info.startswith("over"):
                        return int(form_info.lstrip("over")), 1000
                    else:
                        raise ValueError("Invalid input specified!")

            lower_age, upper_age = format_age_weight(form_age)
            lower_weight, upper_weight = format_age_weight(form_weight)

            form_gender = form.cleaned_data["gender"]
            form_location = form.cleaned_data["location"]
            print(form_gender)
            res_list = Occurence.objects.filter(continent=form_location).filter(gender=form_gender).filter(age__lte=upper_age).filter(age__gte=lower_age).filter(weight__lte=upper_weight).filter(weight__gte=lower_weight)

            attribute_list = [
                "adverse_effects", "drug_names", "age", "weight", "gender",
                "continent", "literature_reference",
            ]
            res_list = [tuple(map(lambda x: getattr(el, x), attribute_list)) for el in res_list]
            return render(request, 'MySideEffectApp/result.html', {
                'res_list': res_list,
                'attribute_list': attribute_list,
            })

    personal_info_form = UserForm()
    return render(request, 'MySideEffectApp/home.html', {
        'personal_info_form': personal_info_form,
    })


def about(request):
    return render(request, 'MySideEffectApp/about.html')


def contact(request):
    return render(request, 'MySideEffectApp/contact.html')


def sponsors(request):
    return render(request, 'MySideEffectApp/sponsors.html')

def preferences(request):
    return render(request, 'MySideEffectApp/preferences.html')
