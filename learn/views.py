from django.shortcuts import render
from django.http import HttpResponse
from main.models import sectionList, titleList
from django.views.generic import DetailView
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
import re

class newDetailView(DetailView):
    model = titleList
    template_name = "learn/page.html"
    context_object_name = "article"
    print(titleList.title)


def search(request):
    # queryset = titleList.objects.all()
    valGet = request.GET.get('search', '')
    # arrTitle = []
    # for val in queryset:
    #     reg = re.search(r"\w*" + valGet + r"\w*", val.article_text, flags=re.IGNORECASE)
    #     if reg:
    #         line = val.article_text.split() # разбиение текста
    #         numInArr = line.index(reg.group()) # найти индекс элемента
    #         if numInArr < 30:
    #             arrTitle.append({"text": " ".join(line[0:numInArr+30]), "titleName": val.title})
    #         else: 
    #             arrTitle.append({"text": " ".join(line[numInArr-30:numInArr+30]), "titleName": val.title})
    queryset = titleList.objects.filter(Q(title__contains=valGet) | Q(article_text__contains=valGet))
    return render(request, 'learn/search.html', {"queryset": queryset})



def index(request):
    sections = sectionList.objects.all()
    titles = titleList.objects.all()
    return render(request, 'learn/mainMenu.html', {"sections": sections, "titles": titles})

def profile(request):
    user = 1
    return render(request, 'account/profile.html')