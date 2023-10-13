from django.shortcuts import render
import logging

# Create your views here.
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return render(request, 'main.html')

def about(request):
    logger.info('Index page accessed')
    return render(request, 'about.html')