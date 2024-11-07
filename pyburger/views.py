from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burgers

def main(request):
    #return HttpResponse("안녕하세요,파이버거입니다")
    return render(request, "main.html")

def burger_list(request):
    #return HttpResponse("파이버거집의 햄버거 목록입니다.")
    burgers = Burgers.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers":burgers,
    }
    return render(request, "burger_list.html", context)

def burger_search(request):
    keyword = request.GET.get("keyword")

    if keyword is not None:
        burgers = Burgers.objects.filter(name__contains=keyword)
    else:
        burgers = Burgers.objects.none()
    context = {
        "burgers":burgers
    }
    return render(request, "burger_search.html",context)