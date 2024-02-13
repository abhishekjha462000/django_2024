from django.contrib import admin
from django.urls import path
from . import views

# view is a function -- url aane pr hit hoga
# view -- function , class


# path function is used to connect a view to url.
# named-url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about-us', views.about_us, name = 'mera_about_us') # "localhost:8000/about-us"
]


