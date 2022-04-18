from django.shortcuts import render
from datetime import datetime


def clock(request):
    now = datetime.now()
    format = '%H:%M:%S'
    current_time = now.strftime(format)
    current_date = now.strftime('%d-%m-%Y')
    context = {'time': current_time, 'date': current_date}
    return render(request, 'home.html', context)