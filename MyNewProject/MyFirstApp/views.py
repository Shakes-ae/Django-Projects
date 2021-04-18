from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = locals()
    template = 'index.html'
    return HttpResponse("Yayyyyy")
    return render(request, template, context)