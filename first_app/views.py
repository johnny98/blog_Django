from django.shortcuts import render
# from django.http import HttpResponse
# from first_app.models import User
from first_app.forms import NewUserForm
from . import forms
# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'first_app/users.html', context=user_dict)


def form_page(request):
    # form = forms.FormName()
    #
    # if request.method == 'POST':
    #     form = forms.FormName(request.POST)
    #
    #     if form.is_valid():
    #         print('VALIDATION SUCCESS!')
    #         print("Name: " + form.cleaned_data['name'])
    #         print("Email: " + form.cleaned_data['email'])
    #         print("Text: " + form.cleaned_data['text'])
    #
    # return render(request, 'first_app/form_page.html',{'form':form})
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'first_app/form_page.html',{'form':form})
