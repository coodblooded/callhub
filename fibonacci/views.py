from django.shortcuts import render
from django.http import HttpResponseRedirect

from datetime import datetime

# Create your views here.

def my_view(request):
    # ...
    result = 0
    previous_number = 0
    total_time = 0
    if request.method == 'POST':
        before_cal = datetime.now()
        new_number = request.POST.get('finnumber')
        previous_number = new_number
        result = fib(int(new_number))
        after_cal = datetime.now()
        total_time = ((after_cal - before_cal).microseconds) / 1000000
    return render(request, "fibonacci/index.html", {'result' : result, 'per': previous_number, 'time' : total_time})


def fib(n):
    m = {}
    for i in range(1, n+1):
        if i <= 2:
            m[i] = 1
        else:
            try:
                f = m[i-1] + m[i - 2]
                m[i] = f
            except KeyError:
                pass
    return m[n]