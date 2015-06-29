from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    response = render(request, 'music/index.html', context)
    return response
