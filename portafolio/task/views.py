from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse



class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "task/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data["tasks"]
            request.session["tasks"] += [tasks]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "task/add.html", {
                "form": form
            })
    return render(request, "task/add.html", {
        "form":NewTaskForm()
    })
