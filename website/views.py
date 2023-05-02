'''
working with renders
'''
from django.shortcuts import render


def home(request):
    # creating home requests
    return render(request, 'home.html', {})
