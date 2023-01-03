from django.shortcuts import render
from django import forms

task = ["foo","bar","baz"]

class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    return render(request, "task/index.html", {
        "tasks": task
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data["tasks"]
            task.append(tasks)
        else:
            return render(request, "task/add.html", {
                "form": form
            })
    return render(request, "task/add.html", {
        "form":NewTaskForm()
    })
