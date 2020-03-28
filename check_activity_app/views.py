from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import *
from django.forms.models import model_to_dict
from django.views.generic import View, TemplateView, ListView, DetailView


# Create your views here.
def index(request):
    # obj = User.objects.all().values()
    obj = ActivityPeriod.objects.values('id','user__name','start_time','end_time')

    data = {
        "response": list(obj)
    }
    print(data)
    # return HttpResponse("<em>hello World!</em>")
    return JsonResponse(data)


