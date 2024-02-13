from django.http import HttpResponse
from django.urls import reverse

def home(request):
    url = reverse('mera_about_us') # localhost:8000/about-us
    response_data = f"""
        <h1>My name is Abhishek Jha</h1>
        <h2>My name is Abhishek Jha</h2>
        <h3>My name is Abhishek Jha</h1>
        <h4>My name is Abhishek Jha</h4>
        <h5>My name is Abhishek Jha</h5>
        <h6>My name is Abhishek Jha</h6>
        <h1><a href = '{url}'>About Us</a></h1>
    """
    return HttpResponse(response_data)
# localhost:8000/home/about-us -- relative path
# absolute path -- localhost:8000
def about_us(request):
    response_data = '<h1>Welcome to the about us page.</h1>'
    return HttpResponse(response_data)


