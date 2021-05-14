from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, TrackerForm 

def RGAform(request):
    instruct = HttpResponse("Hello. This is an RGA cart tracker! please enter the date/time to begin. Enter as many masses as you would like. Then fill in the cold cathode pressure as well as the sum of scanned masses (total pressure the RGA sees).")
    contact = ContactForm()
    #tracker = TrackerForm()
    return(instruct) #render(request, 'forms.html', {'forms':forms}))

def History(request):
    return HttpResponse("This is a page for looking at the history of carts")

