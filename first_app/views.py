from django.shortcuts import render
from datetime import datetime
def index_page(request):
    context = {
        "name": "00"
    }

    return render(request, "index.html", context)
def time_page(request):
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    context = {
        "date": date_time_str[0:10],
        "time": date_time_str[11::]
    }

    return render(request, "time.html", context)
