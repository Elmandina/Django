from re import template
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def appview(request):
   
    templates="index.html"

    
    information =["rrace e ardhur nga Kina Jugore","mund te peshojne 18-41 kg","mund te jetoje 11-14 vjec","arrin deri ne gjatesine 56 cm"]
    ngjyrat=['light gold','cream','light tan to brown']
    
    
    context={'information': information, 'ngjyrat': ngjyrat}

    return render(request, templates, context)