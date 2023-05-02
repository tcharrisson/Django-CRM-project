'''
working with renders
'''
from django.shortcuts import render

'''
Create a function for the home page,
'''
def home(request):
    return render(request, 'home.html', {})
