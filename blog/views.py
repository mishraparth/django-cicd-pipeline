from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to My Blog")

def posts(request):
    return HttpResponse("Here are some posts...")

def about(request):
    return HttpResponse("About this blog")
