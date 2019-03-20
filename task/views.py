from django.shortcuts import render
from .models import Field


def index(request):
    fields = Field.objects.all()
    context = {'fields': fields}

    if fields.count() == 0:
        Field.objects.create(data_field={
            "name_field": "Field",
            "value_field": "Value",
        })

    if request.method == "POST":
        Field.objects.create(data_field={
            "name_field": "Field",
            "value_field": "Value",
        })

    return render(request, "task/index.html", context)


def detail(request):
    fields = Field.objects.all()
    context = {'fields': fields}

    return render(request, "task/detail.html", context)
