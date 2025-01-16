import django.contrib.auth
from django.shortcuts import render
from datetime import datetime
from first_app import models
import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
def calc_page(request):
    a = int(request.GET.get('a', '0'))
    b = int(request.GET.get('b', '0'))
    res = a + b
    context = {
        "a": a,
        "b": b,
        "res": res
    }

    return render(request, "calc.html", context)
def expression_page(request):
    a1 = random.randint(10, 100)
    a2 = random.randint(10, 100)
    a3 = random.randint(10, 100)
    a4 = random.randint(10, 100)
    res = a1 + a2 - a3 - a4
    expression = models.History(
        expression = f"{a1}+{a2}-{a3}-{a4}",
        result = res
    )
    expression.save()
    context = {
        "a1": a1,
        "a2": a2,
        "a3": a3,
        "a4": a4,
        "res": res
    }

    return render(request, "expression.html", context)
def history_page(request):

    expression_history = models.History.objects.all()
    context = {
        "comment_history": expression_history
    }
    return render(request, "history.html", context)
@login_required
def word_page(request):
    if "string" in request.POST:
        text = request.POST["string"]
        text = list(map(str, text.split()))
        warr = ""
        narr = ""
        nw = 0
        nd = 0
        for x in text:
            if x.isdigit():
                narr += " " + x
                nw += 1
            if x.isalpha():
                warr += " " + x
                nd += 1
        print(text)
        row = models.WordHistory(
            wordCount=nw,
            numCount=nd,
            wordArr=warr,
            numArr=narr,
            user = request.user
        )
        row.save()
    history = models.WordHistory.objects.all()
    context = {
        "history": history
    }
    return render(request, "str2words.html", context)

def word_history_page(request):

    history = models.WordHistory.objects.all()
    context = {
        "history": history
    }
    return render(request, "str_history.html", context)


def logout_view(request):
    django.contrib.auth.logout(request)
    return redirect('/')