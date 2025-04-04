import django.contrib.auth
from django.shortcuts import render
from datetime import datetime
from first_app import models
import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

def index_page(request):
    context = {
        "name": "index",
        "pages": 7
    }

    return render(request, "index.html", context)
def time_page(request):
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    context = {
        "date": date_time_str[0:10],
        "time": date_time_str[11::],
        "pagename": "time"
    }

    return render(request, "time.html", context)
def calc_page(request):
    error = 0
    a, b, res = 0, 0, 0
    try:
        a = int(request.GET.get('a', '0'))
        b = int(request.GET.get('b', '0'))
        res = a + b
    except:
        error = 1
    context = {
        "pagename": "calc",
        "a": a,
        "b": b,
        "res": res,
        "error": error
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
        "res": res,
        "pagename": "exp"
    }

    return render(request, "expression.html", context)
def history_page(request):

    expression_history = models.History.objects.all()
    context = {
        "comment_history": expression_history,
        "pagename": "history"
    }
    return render(request, "history.html", context)

def word_page(request):
    if "string" in request.POST:
        text = request.POST["string"]
        text = list(map(str, text.split()))
        warr = ""
        narr = ""
        for x in text:
            if not(x.isdigit()): warr = warr + x + " "
            else: narr = narr + x + " "
        warr = warr[:-1]
        narr = narr[:-1]
        nw = 0
        nd = 0
        for x in text:
            if x.isdigit():
                nd += 1
            if x.isalpha():
                nw += 1
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
        "history": history,
        "pagename": "strInput"
    }
    return render(request, "str2words.html", context)

def word_history_page(request):

    history = models.WordHistory.objects.all()
    context = {
        "history": history,
        "pagename": "strHistory"
    }
    return render(request, "str_history.html", context)


def logout_view(request):
    django.contrib.auth.logout(request)
    return redirect('/')
@csrf_exempt
def clicker_page(request):
    last = models.ClickerSave.objects.all().order_by("-date")[0]
    context = {
        "hp": last.hp,
        "iq": last.iq,
        "happiness": last.happiness
               }
    if request.method == "POST":
        data = json.loads(request.body)

        clicker = models.ClickerSave(
            hp=data["hp"],
            iq=data["iq"],
            happiness=data["happiness"],
            date=datetime.now()
        )
        clicker.save()
    return render(request, "clicker.html", context)