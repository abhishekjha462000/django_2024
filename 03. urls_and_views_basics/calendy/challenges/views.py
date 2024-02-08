from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is the challenges page.</h1>')


def monthly_challenge(request, month):
    challenge_text = ''
    if month == 'January':
        challenge_text = '<h1>Focus on your diet. Avoid junk food.</h1>'
    elif month == 'February':
        challenge_text = '<h1>Learn Django for 20 minutes daily.</h1>'
    else:
        challenge_text = '<h1>No challenge</h1>'
    return HttpResponse(challenge_text)