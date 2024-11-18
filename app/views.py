from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
from django.http import HttpRequest, HttpResponse

# Create your views here.


def add_recipe(request):
    form = recipe(request.POST or None)
    print(f"Hello {form}")
    if form.is_valid():
        a = form.cleaned_data["name"]
        b = form.cleaned_data["ingr"]
        c = form.cleaned_data["Desc"]
        n = recipe1(name1=a, ingr1=b, Desc1=c)
        n.save()
        return redirect("home")
    else:
        print("invalid")
        return render(request, "addrecipe.html", {"form": form})


def view_all(request):
    n = recipe1.objects.all()
    return render(request, "viewall.html", {"n": n})
