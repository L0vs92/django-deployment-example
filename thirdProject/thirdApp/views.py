from django.shortcuts import render
from . import forms


def index(request):
    return render(request, "thirdApp/index.html")


def formName(request):
    form = forms.FormFile()

    if request.method == "POST":
        form = forms.FormFile(request.POST)

        if form.is_valid():
            print("Validation success")
            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])

    return render(request, "thirdApp/form.html", {"form": form})
