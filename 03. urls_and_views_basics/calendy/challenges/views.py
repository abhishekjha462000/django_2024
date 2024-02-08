from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges = {
    'January' : 'Focus on your diet. Avoid junk food.',
    'February' : 'Learn Django and master it.',
    'March' : 'Lower down your body fat percentage.',
    'April' : "Master Js and ReactJs.",
    'May' : 'Complete Machine learning.',
    'June' : 'It\'s my birthday.',
    'July' : 'Apply for jobs.',
    'August' : 'Starts talking to Dr. Priyanka.',
    'September' : 'Propose to Priyanka.',
    'October' : 'She accepts my proposal.',
    'November' : 'We get into a relationship.',
    'December' : 'We finally start thinking of marriage. I have a great life ahead.'
}

def home(request):
    response_data = '<h1>challenges</h1><br>'

    months = list(challenges.keys())

    months_lis = '<ul>'

    for month in months:
        element = f"<li><h1><a href = '#'>{month}</a></h1></li>"
        months_lis += element

    months_lis += '</ul>'

    return HttpResponse(response_data + months_lis)

def monthly_challenge_by_integer(request, value):
    if value < 1 or value > len(challenges):
        return HttpResponseNotFound('<h1>Enter a valid month number</h1>')

    month = list(challenges.keys())[value-1]

    redirect_url = reverse('monthly-challenge', args = [month])
    
    # return HttpResponseRedirect(f'/challenges/{month}')
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        challenge = challenges[month]
        return HttpResponse(f"<h1>{challenge}</h1>")
    except KeyError as ex:
        return HttpResponseNotFound('<h1>This is an invalid month</h1>')