from django.shortcuts import render, HttpResponse, redirect
from .models import Users, Items

# Create your views here.


def home(request):
    user_id = request.session.get("user")["id"]
    if not user_id:
        return redirect("login")

    items = Items.objects.filter(user=user_id).all()

    return render(request, "home.html", {"items": items})


def login(request):
    if request.session.get("user"):
        return redirect("home")
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def makeUser(request):
    if request.method != "POST":
        return redirect("login")
    username = request.POST["username"]
    password = request.POST["password"]
    db_user = Users.objects.filter(username=username, password=password).first()
    if db_user:
        return redirect("register")

    # HASH PASSWORDS
    new_user = Users(username=username, password=password)
    new_user.save()
    return redirect("logout")


def logout(request):
    if "user" in request.session:
        del request.session["user"]
    return redirect("login")


def checkLogin(request):
    if request.method != "POST":
        return redirect("login")
    username = request.POST["username"]
    password = request.POST["password"]
    db_user = Users.objects.filter(username=username, password=password).first()
    if db_user:
        user = {"username": db_user.username, "id": db_user.id}
        request.session["user"] = user
        return redirect("home")
    else:
        return redirect("login")


def addItem(request):
    if request.method != "POST":
        return redirect("home")
    user_id = request.session.get("user")["id"]
    if not user_id:
        return redirect("login")

    db_user = Users.objects.filter(id=user_id).first()
    title = request.POST["title"]
    desc = request.POST["desc"]
    price = request.POST["price"]
    sold = True if "sold" in request.POST else False
    # image = request.POST["image"]
    new_item = Items(
        title=title, description=desc, price=price, sold=sold, user=db_user
    )

    new_item.save()
    return redirect("home")


def deleteItem(request, id):
    if request.method != "POST":
        return redirect("home")
    user_id = request.session.get("user")["id"]
    if not user_id:
        return redirect("login")

    Items.objects.filter(id=id, user=user_id).delete()

    return redirect("home")


def toggleSold(request, id):
    if request.method != "POST":
        return redirect("home")
    user_id = request.session.get("user")["id"]
    if not user_id:
        return redirect("login")

    db_item = Items.objects.filter(id=id, user=user_id).first()
    if db_item.sold:
        db_item.sold = False
    else:
        db_item.sold = True
    db_item.save()

    return redirect("home")
