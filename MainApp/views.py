from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
def home(request):
    # text = f""" <h1>"Изучаем django"</h1> <strong>Автор</strong>: <i>Лазуренко Н.С.</i>"""
    # return HttpResponse(text)
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def items_list(request):
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse(items_result)
    context = {
        "items": Item.objects.all()
    }
    return render(request,"items.html",context)

def items_brand_list(request,brand):
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse(items_result)
    context = {
        "items": Item.objects.all().filter(brand=brand),
        "brand": brand
    }
    return render(request,"items_brand.html",context)



def item_page(request,id):
    item = Item.objects.get(pk=id)
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse(items_result)
    context = {
        "item": item
    }
    return render(request, "item_page.html", context)

