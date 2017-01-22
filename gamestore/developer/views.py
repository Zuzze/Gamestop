from django.http import HttpResponse
from django.shortcuts import render

"""
Developer home page.
"""
def index(request):
    #return HttpResponse("Developer home page.")
    print(request.method)
    return render (request, "developer/index.html")
