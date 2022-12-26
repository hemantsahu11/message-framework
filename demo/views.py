from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.


def home(request):
    return HttpResponse("Home page message framework")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.SUCCESS, 'Student has been successfully registered')
            messages.success(request, 'Student has been created successfully')
            # print(messages.get_level(request))  # getting the info level
            # messages.debug(request, 'This is debug message')  # By default debug messages will not be displayed we have to change it manually
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'This is debug message')   # now debug message will be displayed 
    else:
        form = RegistrationForm()
    return render(request, 'demo/register.html', {'form': form})
