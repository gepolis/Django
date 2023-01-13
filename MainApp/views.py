from django.shortcuts import render, HttpResponse, Http404

def home(request):
    # text = f""" <h1>"Изучаем django"</h1> <strong>Автор</strong>: <i>Лазуренко Н.С.</i>"""
    # return HttpResponse(text)
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]
def items_list(request):
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse(items_result)
    context = {
        "items": items
    }
    return render(request,"items.html",context)





def item_page(request,id):
    for item in items:
        if item['id'] == id:
    #         item_str = f"товар {item['name']} количество{item['quantity']}"
    #         return HttpResponse(item_str)
    # return HttpResponse(f"Товар с id = {id} не найден")
            return render(request,"item_page.html", item)
    raise Http404(f"Товар с id = {id} не найден")