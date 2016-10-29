from django.shortcuts import render

# This just returns our home.html file
def home(request):
    return render(request, 'base.html')
