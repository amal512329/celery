from django.shortcuts import render
from . tasks import go_to_sleep
# Create your views here.

def index(request):
    go_to_sleep(5)
    return render(request,'app/index.html')