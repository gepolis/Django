from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from MainApp.forms import NewUserForm
from MainApp.models import Item, Cart
from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this


def home(request):
    # text = f""" <h1>"Изучаем django"</h1> <strong>Автор</strong>: <i>Лазуренко Н.С.</i>"""
    # return HttpResponse(text)
    return render(request, "index.html")


def cart(request):
    # text = f""" <h1>"Изучаем django"</h1> <strong>Автор</strong>: <i>Лазуренко Н.С.</i>"""
    # return HttpResponse(text)

    return render(request, "cart.html", context={"cart": Cart.objects.all().filter(user=request.user.id)})


def about(request):
    return render(request, "about.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def items_list(request):
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse(items_result)
    context = {
        "items": Item.objects.all()
    }
    return render(request, "items.html", context)


def items_brand_list(request, brand):
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse(items_result)
    context = {
        "items": Item.objects.all().filter(brand=brand),
        "brand": brand
    }
    return render(request, "items_brand.html", context)


def item_page(request, id):
    item = Item.objects.get(pk=id)
    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href ='/item/{item['id']}'> " + item['name'] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse(items_result)
    context = {
        "item": item
    }
    try:
        if request.GET.msg == "1":
            messages.error(request, "Нет на складе!")
    except Exception as e:
        pass
    return render(request, "item_page.html", context)


def login_request(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have successfully logged out.")
    return redirect("index")


def add_item(request, item):
    if Item.objects.get(pk=item).count == 0:
        return redirect(f"/item/{item}?msg=1")
    if request.user.is_authenticated:
        item = Item.objects.get(pk=item)
        try:
            c = Cart.objects.get(user=request.user.id, item=item)
            c.count = c.count + 1
            c.save()
        except Cart.DoesNotExist:
            c = Cart(item=item, count=1, user=request.user.id, name=item.name)
            c.save()
        return redirect(f"/item/{item}")


def test(request):
    return render(request,"test.html")