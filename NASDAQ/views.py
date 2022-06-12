from django.shortcuts import render

from . models import nasdaq

def index(request):
    post_nasdaq = nasdaq.objects.all()

    context = {
        'TampungNasdaq':post_nasdaq,
    }
    return render(request, 'NASDAQ/index.html', context)
