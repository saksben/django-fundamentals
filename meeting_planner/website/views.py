from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        context = {}
    return render(request, "website/welcome.html",
                #   {"num_meetings": Meeting.objects.count()}) # num_meetings is a template variable. # Meeting.objects.count() counts all objects. I.e. a counting method endpoint
                    # {"meetings": Meeting.objects.all()}) # Meeting.objects.all() gets all objects. I.e. getAll() endpoint
                    context)

def about(request):
    return HttpResponse("I'm Benjamin and I'm a software engineer!")