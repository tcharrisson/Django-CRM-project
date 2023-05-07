'''
working with renders
'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):
    '''check to see if logging in
    '''
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username =username, password =password)
        if user is not None:
            login(request, user)
            messages.success(request, message= 'you have been logged in!')
            return redirect("home")
        else:
            messages.success(request, message= "There was an error while logging in, Try again ")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    '''logoout function
    '''
    logout(request)
    messages.success(request, 'You have been logged out!...')
    return redirect('home')

def register_user(request):
    '''users registration function
    '''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been successfully Registered. welcome!...")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    '''Look up record'''
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page!...")
        return redirect('home')
